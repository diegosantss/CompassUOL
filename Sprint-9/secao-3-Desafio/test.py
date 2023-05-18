from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, LongType, StringType, BooleanType, DoubleType, IntegerType, ArrayType

import datetime

# Caminho do arquivo JSON
json_file = 'data/part1.json'

trusted_json = 'parquet-json'

# Definindo a data atual
today = datetime.datetime.today()

# Caminho para salvar o arquivo Parquet final
parquet_path = f'{trusted_json}/{today.year}/{today.month}/{today.day}'

# Configuração do Spark
spark = SparkSession.builder \
    .appName('Combine JSON Files') \
    .getOrCreate()

# Define o schema dos dados JSON
schema = StructType([
    StructField("adult", BooleanType()),
    StructField("backdrop_path", StringType()),
    StructField("belongs_to_collection", StringType()),
    StructField("budget", LongType()),
    StructField("genres", ArrayType(StructType([
        StructField("id", LongType()),
        StructField("name", StringType())
    ]))),
    StructField("homepage", StringType()),
    StructField("id", LongType()),
    StructField("imdb_id", StringType()),
    StructField("original_language", StringType()),
    StructField("original_title", StringType()),
    StructField("overview", StringType()),
    StructField("popularity", DoubleType()),
    StructField("poster_path", StringType()),
    StructField("production_companies", ArrayType(StructType([
        StructField("id", LongType()),
        StructField("logo_path", StringType()),
        StructField("name", StringType()),
        StructField("origin_country", StringType())
    ]))),
    StructField("production_countries", ArrayType(StructType([
        StructField("iso_3166_1", StringType()),
        StructField("name", StringType())
    ]))),
    StructField("release_date", StringType()),
    StructField("revenue", LongType()),
    StructField("runtime", IntegerType()),
    StructField("spoken_languages", ArrayType(StructType([
        StructField("english_name", StringType()),
        StructField("iso_639_1", StringType()),
        StructField("name", StringType())
    ]))),
    StructField("status", StringType()),
    StructField("tagline", StringType()),
    StructField("title", StringType()),
    StructField("video", BooleanType()),
    StructField("vote_average", DoubleType()),
    StructField("vote_count", IntegerType())
])

# Carrega o arquivo JSON
df = spark.read.schema(schema).json(json_file)

# Realiza tratamentos nos dados JSON
df = df.withColumn("release_date", col("release_date").cast("date"))

# Preenche valores nulos com um valor específico
df = df.na.fill("N/A")

# Salva o DataFrame como um único arquivo Parquet
df.coalesce(1).write.mode("overwrite").parquet(parquet_path)

print('Arquivo JSON combinado e tratado, e salvo como Parquet.')
