--Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.


select cdcli , nmcli , SUM(qtd*vrunt) as gasto
from tbvendas
where status ='Concluído'
GROUP by nmcli 
order by gasto DESC 
limit 1