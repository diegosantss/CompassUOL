select count(*) as quantidade, editora.nome, endereco.estado, 
endereco.cidade 
from livro
left join editora on livro.editora = editora.codeditora
left join endereco on editora.endereco = endereco.codendereco 

group by livro.editora, editora.nome
order by quantidade desc
