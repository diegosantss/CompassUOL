-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.


select tbvendas.cdvdd , tbvendedor.nmvdd
from tbvendas
right join tbvendedor  on tbvendas.cdvdd = tbvendedor.cdvdd 
where status ='Concluído'
group by tbvendedor.nmvdd 
order by count(tbvendas.cdvdd) desc
limit 1
