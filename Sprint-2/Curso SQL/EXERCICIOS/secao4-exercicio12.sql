/*Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


Observação: Apenas vendas com status concluído.*/

SELECT cddep,
       nmdep,
       dtnasc,
       Sum(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas
FROM   tbdependente
       LEFT JOIN tbvendedor
              ON tbdependente.cdvdd = tbvendedor.cdvdd
       LEFT JOIN tbvendas
              ON tbvendedor.cdvdd = tbvendas.cdvdd
WHERE  tbvendas.status = 'Concluído'
GROUP  BY nmdep,
          tbvendedor.nmvdd
ORDER  BY valor_total_vendas ASC
LIMIT  1 