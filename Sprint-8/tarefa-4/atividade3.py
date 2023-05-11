from pyspark.sql.functions import when, rand
from pyspark.sql import SparkSession


# Criando a Spark Session
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Lendo o arquivo nomes_aleatorios.txt e carregando para um DataFrame
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

# Renomeando a coluna para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adicionando a Coluna Escolaridade com os valores aleatorios.
df_nomes = df_nomes.withColumn("Escolaridade", when(rand() < 1/3, "Fundamental")
                                               .when(rand() < 2/3, "Médio")
                                               .otherwise("Superior"))
# Imprimindo o esquema do DataFrame
df_nomes.printSchema()
# Mostrando as 10 primeiras linhas do DataFrame
df_nomes.show(10)
