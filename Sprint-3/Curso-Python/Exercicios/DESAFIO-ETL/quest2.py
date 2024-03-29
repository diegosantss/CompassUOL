#quest 2: A média do número de filmes por autor.

import csv

with open("DESAFIO-ETL/actors.csv") as f:
    reader = csv.reader(f)
    next(reader)  # pula a primeira linha, que contém os nomes das colunas
    lista = []
    for row in reader:
        actor = row[0]
        num_movies = int(row[2])
        lista.append({'actor': actor, 'num_movies': num_movies})

# Calcula a média do número de filmes por ator
num_ator = len(lista)
total_movies = sum([d['num_movies'] for d in lista])
avg_movies = total_movies / num_ator
print(f"Média de filmes por ator: {avg_movies:.2f}")

#SAÍDA: Média de filmes por ator: 37.88