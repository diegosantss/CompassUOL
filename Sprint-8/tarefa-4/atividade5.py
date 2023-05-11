from pyspark.sql.functions import when, rand
from pyspark.sql import SparkSession


# Criando a Spark Session
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Lendo o arquivo nomes_aleatorios.txt e carregando para um DataFrame
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

# Renomeando a coluna para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adicionando a Coluna Escolaridade com os valores aleatorios.
df_nomes = df_nomes.withColumn("Escolaridade",  when(rand() < 1/3, "Fundamental")
                                               .when(rand() < 2/3, "Médio")
                                               .otherwise("Superior"))

# Adicionando a coluna "Pais" com valores aleatórios
paises = ['Brasil', 'Argentina', 'Colômbia', 'Venezuela', 'Peru', 'Chile', 'Equador', 'Bolívia', 'Paraguai', 'Uruguai', 'Suriname', 'Guiana', 'Guiana Francesa']

df_nomes = df_nomes.withColumn("Pais", when(rand() < 1/13, paises[0])
                                         .when(rand() < 2/13, paises[1])
                                         .when(rand() < 3/13, paises[2])
                                         .when(rand() < 4/13, paises[3])
                                         .when(rand() < 5/13, paises[4])
                                         .when(rand() < 6/13, paises[5])
                                         .when(rand() < 7/13, paises[6])
                                         .when(rand() < 8/13, paises[7])
                                         .when(rand() < 9/13, paises[8])
                                         .when(rand() < 10/13, paises[9])
                                         .when(rand() < 11/13, paises[10])
                                         .when(rand() < 12/13, paises[11])
                                         .otherwise(paises[12]))

# Adicionando a coluna AnoNascimento com valores aleatórios entre 1945 e 2010
df_nomes = df_nomes.withColumn("AnoNascimento", (1945 + (rand() * (2010 - 1945))).cast("integer"))

# Imprimindo o esquema do DataFrame
df_nomes.printSchema()
# Mostrando as 10 primeiras linhas do DataFrame
df_nomes.show(10)