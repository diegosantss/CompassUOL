#quest 3: O ator/atriz com a maior média por filme.

import csv

with open("DESAFIO-ETL/actors.csv") as f:
    reader = csv.reader(f)
    next(reader)  # pula a primeira linha, que contém os nomes das colunas
    lista = []
    for row in reader:
        actor = row[0]
        avg_movie = float(row[3])
        lista.append({'actor': actor, 'avg_movie': avg_movie})
    
ordem_lista = sorted(lista, key=lambda x: x['avg_movie'], reverse=True)

print(ordem_lista[0]['actor'], ordem_lista[0]['avg_movie'])

#SAÍDA: Anthony Daniels 451.8