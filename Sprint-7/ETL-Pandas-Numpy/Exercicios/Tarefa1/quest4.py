#Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd

arquivo = pd.read_csv("Sprint-7/ETL-Pandas-Numpy/Exercicios/Tarefa1/actors.csv")

frequencia = arquivo["#1 Movie"].value_counts()

filme_mais_frequente = frequencia.index[0]
frenquencia_max = frequencia.max()

print(f'Filme: {filme_mais_frequente}\nFrequência: {frenquencia_max}')
