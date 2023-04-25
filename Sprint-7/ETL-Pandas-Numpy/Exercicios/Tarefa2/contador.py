# faça um programa que conte as palavras de um arquivo README.md

#arquivo não contem import do pyspark pois é para ser executado diretamente do container que está instalado a imagem do spark completa, sendo executado direto no terminal do pyspark.

# Lê o arquivo de texto
texto = spark.sparkContext.textFile("README.md")

# Divide o texto em palavras e conta a quantidade total de palavras
quantidade_palavras = texto.flatMap(lambda linha: linha.split(" ")).count()

# Imprime o resultado
print(quantidade_palavras)

