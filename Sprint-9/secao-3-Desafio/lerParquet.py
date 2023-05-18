from pyspark.sql import SparkSession

# Caminho para o arquivo Parquet
parquet_path = 'parquet-json/2023/5/17/detach_json.parquet/part-00000-d90082cf-7b68-4b52-9de0-fcebb981d120-c000.snappy.parquet'

# Configuração do Spark
spark = SparkSession.builder \
    .appName('Read Parquet File') \
    .getOrCreate()

# Carrega o arquivo Parquet
df = spark.read.parquet(parquet_path)

# Exibe o DataFrame
df.show()
