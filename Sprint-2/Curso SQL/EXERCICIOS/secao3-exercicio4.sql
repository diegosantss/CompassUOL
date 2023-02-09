--Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

select autor.nome, autor.codautor, autor.nascimento, count(livro.autor)quantidade
from livro

left join autor on livro.autor = autor.codautor 

group by autor.nome, autor.nascimento, autor.codautor

order by autor.nome  asc
