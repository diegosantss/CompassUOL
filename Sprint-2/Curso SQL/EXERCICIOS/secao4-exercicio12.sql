/*Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


Observação: Apenas vendas com status concluído.*/

select cddep, nmdep , dtnasc , SUM(tbvendas.qtd *tbvendas.vrunt) as valor_total_vendas  
from tbdependente
left join tbvendedor on tbdependente.cdvdd = tbvendedor.cdvdd 
left join tbvendas on tbvendedor.cdvdd  = tbvendas.cdvdd
where tbvendas.status = 'Concluído'
GROUP BY nmdep , tbvendedor.nmvdd 
order by valor_total_vendas asc
limit 1