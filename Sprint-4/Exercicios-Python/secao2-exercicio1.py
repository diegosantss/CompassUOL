# ----------COMANDO DA QUESTÃO----------
    #Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. 
    #Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
    #Você deverá aplicar as seguintes funções no exercício:
    #map, filter, sorted e sum()
    #Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
    # A lista dos 5 maiores números pares em ordem decrescente;
    # A soma destes valores.

with open("Sprint-4/Exercicios/number.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    
    #converter as linhas em inteiros e colocar em uma lista
    numeros = list(map(int, linhas))

    #nova lista com numeros pares e na ordem decrescente
    numeros_pares = sorted(filter(lambda x: x % 2 == 0, numeros), reverse=True)

    #filtrando os 5 maiores numeros da lista de pares utilizando o slicing
    cinco_maiores = numeros_pares[:5]

    #somar os 5 maiores numeros pares com a função sum()
    soma_maiores = sum(cinco_maiores)

print(cinco_maiores)
print(soma_maiores)
