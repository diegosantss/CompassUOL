#Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd

arquivo = pd.read_csv("Sprint-7/ETL-Pandas-Numpy/Exercicios/Tarefa1/actors.csv")

dfCount = arquivo["#1 Movie"].value_counts().reset_index()
dfCount.columns = ["Filmes", "Frequência"]
dfCount = dfCount[dfCount["Frequência"] > 1]
print(dfCount)
