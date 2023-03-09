#----------COMANDO DA QUESTÃO:----------
    #Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
    #É obrigatório aplicar as seguintes funções:
    #len, filter E lambda
    #Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

def conta_vogais(palavra):
    #quantidade de vogais utilizando o filter em conjunto com o lambda, armazenar em uma lista apenas com as vogais e len() para contar a quantidade de itens da lista.
    quant_vogais = len(list(filter(lambda x: x in 'AEIOUaeiou', palavra)))
    return quant_vogais

print(conta_vogais)