select autor.nome 
from autor 
right join livro on autor.codautor = livro.autor 
right join editora on livro.editora = editora.codeditora
right join endereco on editora.endereco = endereco.codendereco 
where 
endereco.estado = (select estado from endereco where  endereco.estado <> "PARANÁ" or "RIO GRANDE DO SUL") and autor.nome is not null
order by autor.nome asc