#Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd

arquivo = pd.read_csv("Sprint-7/ETL-Pandas-Numpy/Exercicios/Tarefa1/actors.csv")

maior_media = arquivo["Average per Movie"].idxmax()

Ator = arquivo.loc[maior_media, "Actor"]

print(Ator)