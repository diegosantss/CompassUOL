--Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).
SELECT autor.nome,
       autor.codautor,
       autor.nascimento,
       Count(livro.autor)quantidade
FROM   livro
       RIGHT JOIN autor
               ON livro.autor = autor.codautor
GROUP  BY autor.nome,
          autor.nascimento,
          autor.codautor
ORDER  BY autor.nome ASC 
