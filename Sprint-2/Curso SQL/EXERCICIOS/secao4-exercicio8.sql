-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.


SELECT tbvendas.cdvdd,
       tbvendedor.nmvdd
FROM   tbvendas
       RIGHT JOIN tbvendedor
               ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE  status = 'Concluído'
GROUP  BY tbvendedor.nmvdd
ORDER  BY Count(tbvendas.cdvdd) DESC
LIMIT  1 