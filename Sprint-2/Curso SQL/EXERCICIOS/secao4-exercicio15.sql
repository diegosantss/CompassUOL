--Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

select cdven 
from tbvendas t
where deletado  = 1
order by cdven ASC 