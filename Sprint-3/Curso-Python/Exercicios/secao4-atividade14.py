#Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.

def func(*args, **kwargs):
    for x in args:
        print(x)
    for key, value in kwargs.items():
        print(value)

func(1, 3, 4, 'hello', parametro_nomeado ='alguma coisa', x=20)