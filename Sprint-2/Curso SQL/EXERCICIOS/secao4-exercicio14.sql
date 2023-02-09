/*Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

Observação: Apenas vendas com status concluído.*/

select estado , round(AVG((qtd*vrunt)), 2) as gastomedio 
from tbvendas 
right join tbvendedor on tbvendas.cdvdd = tbvendedor.cdvdd 
where status ='Concluído'
GROUP BY tbvendas.estado 
order by gastomedio desc