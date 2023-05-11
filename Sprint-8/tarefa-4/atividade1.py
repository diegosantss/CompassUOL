from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

# Lendo o arquivo nomes_aleatorios.txt e carregando para um DataFrame
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

# Mostrando algumas linhas do DataFrame
df_nomes.show(5)
