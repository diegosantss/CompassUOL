#Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

import pandas as pd

arquivo = pd.read_csv("Sprint-7/ETL-Pandas-Numpy/Exercicios/Tarefa1/actors.csv")

maximo_filme = arquivo["Number of Movies"].idxmax()

ator = arquivo.loc[maximo_filme, "Actor"]
quant_filme = arquivo.loc[maximo_filme, "Number of Movies"]

print (ator, quant_filme)

'''
import pandas as pd

arquivo = pd.read_csv("Sprint-7/ETL-Pandas-Numpy/Exercicios/Tarefa1/actors.csv")

max_filme = arquivo["Number of Movies"].max()

linha_max = arquivo.loc[arquivo["Number of Movies"] == max_filme, ["Actor", "Number of Movies"]]

print(linha_max["Actor"].values[0], linha_max["Number of Movies"].values[0])

'''

