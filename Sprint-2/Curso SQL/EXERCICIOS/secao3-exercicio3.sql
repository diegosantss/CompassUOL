--Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

SELECT Count(*) AS quantidade,
       editora.nome,
       endereco.estado,
       endereco.cidade
FROM   livro
       LEFT JOIN editora
              ON livro.editora = editora.codeditora
       LEFT JOIN endereco
              ON editora.endereco = endereco.codendereco
GROUP  BY livro.editora,
          editora.nome
ORDER  BY quantidade DESC 
