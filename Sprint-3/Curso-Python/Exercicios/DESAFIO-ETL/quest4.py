#quest 4: O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.


import csv

with open('DESAFIO-ETL/actors.csv') as f:
    arquivo = csv.DictReader(f)
    lista = [linha for linha in arquivo]

# Contar frequência dos filmes
filme_freq = {}
for linha in lista:
    filme = linha['#1 Movie']
    if filme in filme_freq:
        filme_freq[filme] += 1
    else:
        filme_freq[filme] = 1

# Encontrar o filme mais frequente
maior_freq_filme = max(filme_freq, key=filme_freq.get)
freq = filme_freq[maior_freq_filme]

print(f'O filme mais frequente é "{maior_freq_filme}", com uma frequência igual a {freq}.')

#SAÍDA: O filme mais frequente é "The Avengers", com uma frequência igual a 6.