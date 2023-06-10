import requests                                         #lib para utilização da chamada da API
import pandas as pd                                     #lib para leitura do csv no S3
import datetime                                         #Lib para adicionar ao caminho dos arquivos a data atual
import json                                             #Lib para Organizar o Json gerado
import boto3                                            #Lib para conectar com o s3
import concurrent.futures                               #lib para utilização do multithreads
from requests.adapters import HTTPAdapter               #Lib para personalizar a conexão HTTP(numero de tentativa)
from requests.packages.urllib3.util.retry import Retry  #Lib para Lidar com Erros de Conexão.

def process_movie(movie_id):
    # Definindo os parâmetros da API do TMD
    api_key = 'c4fb0f2c7c91ab69add9acc126afb031'
    params = {
        'api_key': api_key,
        'language': 'pt-BR',
        'external_source': 'imdb_id',
    }

    url = f'https://api.themoviedb.org/3/find/{movie_id}?'
    
    # Configurando as opções de retry para as requisições
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    # Realizando a primeira chamada para buscar a ID do filme no TMD
    response = requests.get(url, params=params)
    data = response.json()

    # Verificando se há resultados para a requisição
    if 'movie_results' in data and data['movie_results']:
        movie_data = data['movie_results'][0]

        # Realizando a segunda chamada para buscar informações adicionais
        url = f'https://api.themoviedb.org/3/movie/{movie_data["id"]}'
        params2 = {
            'api_key': api_key,
            'language': 'pt-BR',
        }
        response = requests.get(url, params=params2)
        data = response.json()

        return (movie_data, data)
    else:
        return None

def lambda_handler(event, context):
    # Definindo o nome do bucket S3
    bucket_name = 'bucket-ingestao-dados'
    
    # Definindo o caminho do arquivo CSV no S3
    s3_file_name = 'Raw/Local/CSV/Movies/2023/4/21/movies.csv'
    
    # Instanciando um cliente do S3
    s3 = boto3.client('s3')
    
    # Lendo o arquivo CSV diretamente do S3
    response = s3.get_object(Bucket=bucket_name, Key=s3_file_name)
    movies_df = pd.read_csv(response['Body'], sep='|', na_values=['\\N', 'NA'])
    
    # Convertendo o anoLancamento para o formato de datetime
    movies_df['anoLancamento'] = pd.to_datetime(movies_df['anoLancamento'], format='%Y')
    
    # Filtrar os filmes de romance dos últimos 20 anos
    filmes_filtrados = movies_df.loc[(movies_df['genero'].str.contains('Romance')) & (movies_df['anoLancamento'] >= datetime.datetime.now() - pd.DateOffset(years=20))]
    movie_ids = list(filmes_filtrados['id'].unique().tolist())

    
    
    # Definindo a pasta de saída dos arquivos JSON da primeira chamada da API
    find_folder = 'Raw/TMDB/JSON/find'
    
    # Definindo a pasta de saída dos arquivos JSON da segunda chamada da API
    detach_folder = 'Raw/TMDB/JSON/detach'
    
    # Definindo a data atual
    today = datetime.datetime.today()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(process_movie, movie_ids)

    batch_size = 300
    batch_number = 1
    movie_batch = []
    data_batch = []
    num_requests = 0
    num_missing_movies = 0

    for result in results:
        num_requests += 1
        if result is not None:
            movie_data, data = result
            movie_batch.append(movie_data)
            data_batch.append(data)
            if not movie_data:
                num_missing_movies += 1

        # Verificar se o lote atual atingiu o tamanho máximo
        if len(movie_batch) == batch_size:
            # Definir o caminho do arquivo da primeira chamada da API no S3
            find_filename = f'{find_folder}/{today.year}/{today.month}/{today.day}/part{batch_number}.json'

            # Definir o caminho do arquivo da segunda chamada da API no S3
            detach_filename = f'{detach_folder}/{today.year}/{today.month}/{today.day}/part{batch_number}.json'

            # Salvar os arquivos JSON no S3
            s3.put_object(Body=json.dumps(movie_batch, indent=4), Bucket=bucket_name, Key=find_filename)
            s3.put_object(Body=json.dumps(data_batch, indent=4), Bucket=bucket_name, Key=detach_filename)

            # Limpar os lotes
            movie_batch = []
            data_batch = []

            # Incrementar o número do lote
            batch_number += 1

    # Salvar os arquivos JSON restantes, se houver
    if movie_batch:
        # Definir o caminho do arquivo da primeira chamada da API no S3
        find_filename = f'{find_folder}/{today.year}/{today.month}/{today.day}/part{batch_number}.json'

        # Definir o caminho do arquivo da segunda chamada da API no S3
        detach_filename = f'{detach_folder}/{today.year}/{today.month}/{today.day}/part{batch_number}.json'

        # Salvar os arquivos JSON no S3
        s3.put_object(Body=json.dumps(movie_batch, indent=4), Bucket=bucket_name, Key=find_filename)
        s3.put_object(Body=json.dumps(data_batch, indent=4), Bucket=bucket_name, Key=detach_filename) 

    return num_requests, num_missing_movies, 'Finished processing movies data.'