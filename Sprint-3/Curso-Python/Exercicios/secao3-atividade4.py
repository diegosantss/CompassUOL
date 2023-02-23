#Escreva um código Python que imprime todos os números primos de 1 até 100. Abaixo uma imagem de exemplo dos números primos entre 1 e 1000

primos = []

for num in range(2, 101):
    # verificando se o número é primo
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        primos.append(num)
        print(num)
        