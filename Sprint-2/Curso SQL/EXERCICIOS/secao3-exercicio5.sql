--Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente.

select autor.nome 
from autor 
right join livro on autor.codautor = livro.autor 
right join editora on livro.editora = editora.codeditora
right join endereco on editora.endereco = endereco.codendereco 
where 
endereco.estado = (select estado from endereco where  endereco.estado <> "PARANÁ" or "RIO GRANDE DO SUL") and autor.nome is not null
order by autor.nome asc