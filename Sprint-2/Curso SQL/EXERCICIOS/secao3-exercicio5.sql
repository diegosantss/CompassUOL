--Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente.

SELECT autor.nome
FROM   autor
       RIGHT JOIN livro
               ON autor.codautor = livro.autor
       RIGHT JOIN editora
               ON livro.editora = editora.codeditora
       RIGHT JOIN endereco
               ON editora.endereco = endereco.codendereco
WHERE  autor.nome IS NOT NULL
       AND endereco.estado NOT BETWEEN "PARANÁ" and "RIO GRANDE DO SUL"
ORDER  BY autor.nome ASC 