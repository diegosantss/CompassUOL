#Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for key, i in enumerate(primeirosNomes):
    sobrenome = sobreNomes[key]
    idade = idades[key]

    print(f'{key} - {i} {sobrenome} está com {idade} anos' )