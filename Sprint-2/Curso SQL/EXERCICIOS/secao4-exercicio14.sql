/*Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

Observação: Apenas vendas com status concluído.*/

SELECT estado,
       Round(Avg(( qtd * vrunt )), 2) AS gastomedio
FROM   tbvendas
       RIGHT JOIN tbvendedor
               ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE  status = 'Concluído'
GROUP  BY tbvendas.estado
ORDER  BY gastomedio DESC