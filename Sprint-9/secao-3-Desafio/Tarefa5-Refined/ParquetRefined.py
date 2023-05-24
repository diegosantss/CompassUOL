from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

# Caminho dos arquivos Parquet de origem
parquet_detach_origin = 's3://bucket-ingestao-dados/Trusted/TMDB/Parquet_detach/2023/5/22/part-00000-2862f256-b23c-40ad-818a-56d6e25cde01-c000.snappy.parquet'
parquet_find_origin = 's3://bucket-ingestao-dados/Trusted/TMDB/Parquet_find/2023/5/22/part-00000-eca5d819-697f-44a6-944a-b9167f59e638-c000.snappy.parquet'
parquet_imdb_origin = 's3://bucket-ingestao-dados/Trusted/Local/Parquet/Movies/part-00000-fb9ec7cb-5774-4bfe-96c9-506c7f089dd2-c000.snappy.parquet'

# Caminho para salvar os parquets de destino
parquet_dim_filme_tmdb = 's3://bucket-ingestao-dados/Refined/Dim_filme_tmdb'
parquet_dim_filme_imdb = 's3://bucket-ingestao-dados/Refined/Dim_filme_imdb'
parquet_fato_filme = 's3://bucket-ingestao-dados/Refined/Fato_filme'

# Configuração do Spark
spark = SparkSession.builder.getOrCreate()

# Carrega os arquivos Parquet de origem
parquet_detach = spark.read.parquet(parquet_detach_origin)
parquet_find = spark.read.parquet(parquet_find_origin)
parquet_imdb = spark.read.parquet(parquet_imdb_origin)

# Criação do parquet Dim_filme_tmdb
dim_filme_tmdb = parquet_detach.select('id', 'title', 'release_date', 'genres', 'imdb_id')
dim_filme_tmdb = dim_filme_tmdb.withColumnRenamed('id', 'id_tmdb')
dim_filme_tmdb.coalesce(1).write.mode('overwrite').parquet(parquet_dim_filme_tmdb)

# Criação do parquet Dim_filme_imdb
dim_filme_imdb = parquet_imdb.select('id', 'tituloPrincipal', 'anoLancamento', 'genero')
dim_filme_imdb = dim_filme_imdb.withColumnRenamed('id', 'id_imdb')
dim_filme_imdb.coalesce(1).write.mode('overwrite').parquet(parquet_dim_filme_imdb)

# Criação do parquet Fato_filme
fato_filme = parquet_detach.select(
    monotonically_increasing_id().alias('id_fato'),
    'id',
    'popularity',
    'vote_average',
    'vote_count',
    'budget',
    'imdb_id'
)
fato_filme = fato_filme.withColumnRenamed('id', 'id_tmdb')

# Adiciona as colunas do parquet_imdb ao parquet Fato_filme
parquet_imdb_fato = parquet_imdb.select('id', 'notaMedia', 'numeroVotos')
parquet_imdb_fato = parquet_imdb_fato.withColumnRenamed('id', 'imdb_id') 
fato_filme = fato_filme.join(parquet_imdb_fato, on='imdb_id', how='inner')

fato_filme.coalesce(1).write.mode('overwrite').parquet(parquet_fato_filme)

# Salvar as tabelas no AWS Glue
dim_filme_tmdb.write.format('parquet').option('compression', 'snappy').option('path', 's3://bucket-ingestao-dados/Refined/Dim_filme_tmdb').saveAsTable('`glue-lab`.dim_filme_tmdb')
dim_filme_imdb.write.format('parquet').option('compression', 'snappy').option('path', 's3://bucket-ingestao-dados/Refined/Dim_filme_imdb').saveAsTable('`glue-lab`.dim_filme_imdb')
fato_filme.write.format('parquet').option('compression', 'snappy').option('path', 's3://bucket-ingestao-dados/Refined/Fato_filme').saveAsTable('`glue-lab`.fato_filme')