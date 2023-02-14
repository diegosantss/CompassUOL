/*A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.
*/

SELECT tbvendedor.nmvdd                                               AS
       vendedor,
       Sum(qtd * vrunt)                                                AS
       valor_total_vendas,
       Round((perccomissao/100.0) * Sum(qtd *vrunt), 2) AS
       comissao
FROM   tbvendas
       RIGHT JOIN tbvendedor
               ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE  status = 'Concluído'
GROUP  BY tbvendedor.nmvdd
ORDER  BY comissao DESC
