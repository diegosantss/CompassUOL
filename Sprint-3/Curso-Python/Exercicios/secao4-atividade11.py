#Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

#Comando para criar o arquivo:
arquivo = open("arquivo_texto.txt", "w")
arquivo.write('Este conteúdo está em \num\narquivo\nde texto.')
arquivo.close()

#Comandos para ler o arquivo
arquivo = open("arquivo_texto.txt")
print(arquivo.read(), end="")