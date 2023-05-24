import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql import SparkSession
import datetime

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# json origem
json_detach = 's3://bucket-ingestao-dados/Raw/TMDB/JSON/detach/2023/5/9/'
json_find = 's3://bucket-ingestao-dados/Raw/TMDB/JSON/find/2023/5/9/'

# parquet-json destino
trusted_json_detach = 's3://bucket-ingestao-dados/Trusted/TMDB/Parquet_detach/'
trusted_json_find = 's3://bucket-ingestao-dados/Trusted/TMDB/Parquet_find/'

today = datetime.datetime.today()

parquet_detach_path = f'{trusted_json_detach}/{today.year}/{today.month}/{today.day}/'

parquet_find_path = f'{trusted_json_find}/{today.year}/{today.month}/{today.day}/'


spark = SparkSession.builder.getOrCreate()


df_detach = spark.read.option("multiline","true").json(json_detach)

df_find = spark.read.option("multiline","true").json(json_find)


df_detach.coalesce(1).write.mode("overwrite").parquet(parquet_detach_path)

df_find.coalesce(1).write.mode("overwrite").parquet(parquet_find_path)
print('Arquivo JSON combinado e tratado, e salvo como Parquet.')

job.commit()