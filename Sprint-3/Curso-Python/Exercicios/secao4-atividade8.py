#Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.

#Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.

a = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for str in a:
    if str == str[::-1]:
        print(f'A palavra: {str} é um palíndromo')
    else:
        print(f'A palavra: {str} não é um palíndromo')