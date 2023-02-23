#Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.

#A string deve ter valor  "1,3,4,6,10,76"

def func(x):
    separar_itens = x.split(",")
    soma = sum(int(item) for item in separar_itens)
    return soma
string = "1,3,4,6,10,76"

print(f'{func(string)}')