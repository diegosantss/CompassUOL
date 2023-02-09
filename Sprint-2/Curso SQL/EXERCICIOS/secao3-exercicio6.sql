--Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

select  autor.codautor, autor.nome, count(*) as quantidade_publicacoes
from livro
left join autor on livro.autor  = autor.codautor 
 
group by autor.nome
order by quantidade_publicacoes desc
limit 1