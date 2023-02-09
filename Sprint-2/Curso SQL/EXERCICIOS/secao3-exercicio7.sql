--Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

select autor.nome
from autor
left join livro on autor.codautor = livro.autor 
where livro.autor is NULL
order by autor.nome asc