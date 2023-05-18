from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType
import datetime

# Caminho do diretório com os arquivos JSON
json_detach = 's3://bucket-ingestao-dados/Raw/TMDB/JSON/detach/'

trusted_json = 's3://bucket-ingestao-dados/Trusted/JSON/detach'

# Definindo a data atual
today = datetime.datetime.today()

# Caminho para salvar o arquivo Parquet final
parquet_path = f'{trusted_json}/{today.year}/{today.month}/{today.day}/detach_json.parquet'

# Configuração do Spark
spark = SparkSession.builder \
    .appName('Combine JSON Files') \
    .getOrCreate()

# Define o schema dos dados JSON
schema = StructType().add("adult", "boolean") \
                     .add("backdrop_path", "string") \
                     .add("belongs_to_collection", "string") \
                     .add("budget", "long") \
                     .add("genres", "array<struct<id:long, name:string>>") \
                     .add("homepage", "string") \
                     .add("id", "long") \
                     .add("imdb_id", "string") \
                     .add("original_language", "string") \
                     .add("original_title", "string") \
                     .add("overview", "string") \
                     .add("popularity", "double") \
                     .add("poster_path", "string") \
                     .add("production_companies", "array<struct<id:long, logo_path:string, name:string, origin_country:string>>") \
                     .add("production_countries", "array<struct<iso_3166_1:string, name:string>>") \
                     .add("release_date", "string") \
                     .add("revenue", "long") \
                     .add("runtime", "integer") \
                     .add("spoken_languages", "array<struct<english_name:string, iso_639_1:string, name:string>>") \
                     .add("status", "string") \
                     .add("tagline", "string") \
                     .add("title", "string") \
                     .add("video", "boolean") \
                     .add("vote_average", "double") \
                     .add("vote_count", "integer")

# Carrega todos os arquivos JSON do diretório
df = spark.read.schema(schema).json(json_detach + "*.json")

# Realiza tratamentos nos dados JSON
df = df.withColumn("release_date", col("release_date").cast("date"))

# Preenche valores nulos com um valor específico
df = df.na.fill("N/A")

# Salva o DataFrame como um único arquivo Parquet
df.coalesce(1).write.mode("overwrite").parquet(parquet_path)

print('Arquivos JSON combinados e tratados, e salvos como Parquet.')
