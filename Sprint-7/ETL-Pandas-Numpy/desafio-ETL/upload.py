import boto3
import datetime

#colocando em uma variavel o local dos arquivos de upload
movies_filename = 'data/movies.csv'
series_filename = 'data/series.csv'

#criando uma seção na AWS com o nome do perfil e região
session = boto3.Session(profile_name="310881667198_AdministratorAccess",region_name="us-east-1")

#criando um objeto para interagir com o serviço S3 da AWS, podendo realizar operações de upload
s3 = session.resource('s3')

#criando a variavel para mostrar o nome do bucket.
bucket_name = 'bucket-ingestao-dados'

#criando a variavel para instanciar a data atual no caminho do upload.
today = datetime.date.today()

#criando a variavel para armazenar o local para ser armazenado na nuvem
movies_path = f'Raw/Local/CSV/Movies/{today.year}/{today.month}/{today.day}/movies.csv'
series_path = f'Raw/Local/CSV/Series/{today.year}/{today.month}/{today.day}/series.csv'

#processo de upload para a AWS dos arquivos Movies.csv e Series.csv
s3.meta.client.upload_file(movies_filename, bucket_name, movies_path)
s3.meta.client.upload_file(series_filename, bucket_name, series_path)