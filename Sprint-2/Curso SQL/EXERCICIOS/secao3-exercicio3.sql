--Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

select count(*) as quantidade, editora.nome, endereco.estado, 
endereco.cidade 
from livro
left join editora on livro.editora = editora.codeditora
left join endereco on editora.endereco = endereco.codendereco 

group by livro.editora, editora.nome
order by quantidade desc
