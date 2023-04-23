# faça um programa que conte as palavras de um arquivo README.md

with open('README.md', 'r') as f:
    arquivo = f.read()

palavras = arquivo.split()

quantidade = len(palavras)

print (quantidade)

