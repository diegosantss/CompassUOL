# faça um programa que conte as palavras de um arquivo README.md

with open('Sprint-7/ETL-Pandas-Numpy/Exercicios/Tarefa2/README.md', 'r') as f:
    arquivo = f.read()

palavras = arquivo.split()

quantidade = len(palavras)

print (quantidade)

