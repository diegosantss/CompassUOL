from pyspark.sql import SparkSession

# Criando a Spark Session
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Lendo o arquivo nomes_aleatorios.txt e carregando para um DataFrame
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

# Renomeando a coluna para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Imprimindo o esquema do DataFrame
df_nomes.printSchema()

# Mostrando as 10 primeiras linhas do DataFrame
df_nomes.show(10)
