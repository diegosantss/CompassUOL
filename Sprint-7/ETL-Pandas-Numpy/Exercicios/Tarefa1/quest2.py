#Apresente a média da coluna contendo o número de filmes.

import pandas as pd

arquivo = pd.read_csv("Sprint-7/ETL-Pandas-Numpy/Exercicios/Tarefa1/actors.csv")

Num_filmes = arquivo["Number of Movies"].mean()

print(f'Media do numero de filmes: {Num_filmes}')

