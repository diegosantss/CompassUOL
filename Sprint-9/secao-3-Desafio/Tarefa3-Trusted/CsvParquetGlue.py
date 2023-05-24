import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date, expr
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DataType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

movies_csv_file = 's3://bucket-ingestao-dados/Raw/Local/CSV/Movies/2023/4/21/movies.csv'
movies_parquet_path = 's3://bucket-ingestao-dados/Trusted/Local/Parquet/Movies'

series_csv_file = 's3://bucket-ingestao-dados/Raw/Local/CSV/Series/2023/4/21/series.csv'
series_parquet_path = 's3://bucket-ingestao-dados/Trusted/Local/Parquet/Series'

spark = SparkSession.builder.getOrCreate()


csv_schema = StructType([
    StructField("id", StringType(), nullable=False),
    StructField("tituloPincipal", StringType(), nullable=True),
    StructField("tituloOriginal", StringType(), nullable=True),
    StructField("anoLancamento", DataType(), nullable=True),
    StructField("tempoMinutos", IntegerType(), nullable=True),
    StructField("genero", StringType(), nullable=True),
    StructField("notaMedia", DoubleType(), nullable=True),
    StructField("numeroVotos", IntegerType(), nullable=True),
    StructField("generoArtista", StringType(), nullable=True),
    StructField("personagem", StringType(), nullable=True),
    StructField("nomeArtista", StringType(), nullable=True),
    StructField("anoNascimento", IntegerType(), nullable=True),
    StructField("anoFalecimento", IntegerType(), nullable=True),
    StructField("profissao", StringType(), nullable=True),
    StructField("titulosMaisConhecidos", StringType(), nullable=True)
])

movies_read = spark.read.option("header", True).option("sep", "|").csv(movies_csv_file, schema=csv_schema)

movies_read = movies_read.dropDuplicates(['id'])

movies_read = movies_read.filter((col("genero") == "Romance") & (col("anoLancamento").between(current_date() - expr("interval 20 years"), current_date())))

movies_read = movies_read.withColumnRenamed("tituloPincipal", "tituloPrincipal")

#Tratamento dos valores nulos
movies_read = movies_read.fillna(0, subset=["anoLancamento", "tempoMinutos", "notaMedia", "numeroVotos"])
movies_read = movies_read.fillna('null', subset=["tituloPrincipal", "tituloOriginal", "genero", "generoArtista", "personagem"])


movies_read.coalesce(1).write.mode("overwrite").parquet(movies_parquet_path)


series_read = spark.read.option("header", True).option("sep", "|").csv(series_csv_file, schema=csv_schema)

series_read = movies_read.dropDuplicates(['id'])

series_read = series_read.filter((col("genero") == "Romance") & (col("anoLancamento").between(current_date() - expr("interval 20 years"), current_date())))

series_read = series_read.withColumnRenamed("tituloPincipal", "tituloPrincipal")

#Tratamento dos valores nulos
series_read = series_read.fillna(0, subset=["anoLancamento", "tempoMinutos", "notaMedia", "numeroVotos"])
series_read = series_read.fillna('null', subset=["tituloPrincipal", "tituloOriginal", "genero", "generoArtista", "personagem"])


series_read.coalesce(1).write.mode("overwrite").parquet(series_parquet_path)

print('Arquivos CSV transformados em Parquet com tratamento de valores nulos.')

job.commit()