#Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd

arquivo = pd.read_csv("Sprint-7/ETL-Pandas-Numpy/Exercicios/Tarefa1/actors.csv")

frequencia = arquivo["#1 Movie"].value_counts()

for filme, quantidade in frequencia.items():
    print(f"O filme '{filme}' aparece {quantidade} vez(es) no dataset")
