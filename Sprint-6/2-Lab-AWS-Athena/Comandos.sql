--Criação da Tabela dados para inserção das informações do CSV

CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.dados (
  nome  VARCHAR(30),
  sexo  VARCHAR(30),
  total INT,
  ano   INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
)
LOCATION 's3://teste-bucket01/dados/'

-- Criação da Query para visualizar a listagem dos 3 nomes mais usados em cada década desde o 1950 até hoje.

SELECT decada, nome, Quant_uso
FROM (
  SELECT 
    SUBSTR(CAST(ano AS VARCHAR), 1, 3) || '0s' AS decada,
    nome,
    SUM(total) AS Quant_uso,
    ROW_NUMBER() OVER (
      PARTITION BY SUBSTR(CAST(ano AS VARCHAR), 1, 3) || '0s'
      ORDER BY SUM(total) DESC, nome ASC
    ) AS top_3
  FROM 
    meubanco.dados
  WHERE 
    ano >= 1950
  GROUP BY 
    SUBSTR(CAST(ano AS VARCHAR), 1, 3) || '0s',
    nome
  HAVING 
    COUNT(DISTINCT ano) >= 10
) subquery
WHERE 
  top_3 <= 3
ORDER BY 
  decada, Quant_uso DESC;

