from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# Configuração do Spark
spark = SparkSession.builder \
    .appName('Check Zero Budget') \
    .getOrCreate()

# Carrega o DataFrame
df = spark.read.parquet('destino/fato_filme')

# Verifica quantos valores na coluna 'budget' são iguais a 0
zero_budget_count = df.filter(col('revenue') == 0).count()

# Exibe o resultado
print('Quantidade de valores na coluna "budget" iguais a 0:', zero_budget_count)
