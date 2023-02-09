/*A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.
*/

-- FORMA CONFORME O ENUNCIADO PEDE

select tbvendedor.nmvdd as vendedor, SUM(qtd*vrunt) as valor_total_vendas , round((tbvendedor.perccomissao/100*SUM(qtd*vrunt)), 2) as comissao  
from tbvendas 
right join tbvendedor on tbvendas.cdvdd = tbvendedor.cdvdd 
where status ='Concluído'
GROUP BY tbvendedor.nmvdd 
order by comissao desc
-- FORMA TESTE

select tbvendedor.nmvdd as vendedor, SUM(qtd*vrunt) as valor_total_vendas , round((tbvendedor.perccomissao*SUM(qtd*vrunt)/100), 2) as comissao  
from tbvendas 
right join tbvendedor on tbvendas.cdvdd = tbvendedor.cdvdd 
where status ='Concluído'
GROUP BY tbvendedor.nmvdd 
order by comissao desc
