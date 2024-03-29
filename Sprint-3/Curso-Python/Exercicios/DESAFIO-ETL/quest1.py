#quest 1: O ator/atriz com maior número de filmes e o respectivo número de filmes.


import csv

with open("DESAFIO-ETL/actors.csv") as f:
    arquivo = csv.reader(f)
    next(arquivo)  # pula a primeira linha, que contém os nomes das colunas
    lista = []
    for row in arquivo:
        actor = row[0]
        num_movies = int(row[2])
        lista.append({'actor': actor, 'num_movies': num_movies})
    
ordem_lista = sorted(lista, key=lambda x: x['num_movies'], reverse=True)

print(ordem_lista[0]['actor'], ordem_lista[0]['num_movies'])

#SAÍDA: Robert DeNiro 79