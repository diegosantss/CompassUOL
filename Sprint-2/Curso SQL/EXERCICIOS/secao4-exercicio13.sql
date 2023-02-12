-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

SELECT cdpro,
       nmcanalvendas,
       nmpro,
       Sum(qtd) AS quantidade_vendas
FROM   tbvendas t
WHERE  status = 'Concluído'
       AND cdcanalvendas BETWEEN 1 AND 2
GROUP  BY nmpro,
          nmcanalvendas
ORDER  BY quantidade_vendas ASC 