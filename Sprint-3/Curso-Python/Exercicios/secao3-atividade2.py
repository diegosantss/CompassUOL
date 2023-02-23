#Escreva um código Python que verifique se três números digitados pelo usuário são pares ou ímpares. Para cada número, imprima o Par: ou Ímpar: e o número correspondente.
cont = []
for num in range(3):
    if len(cont) == 0 : 
        num = int(input("Insira um valor"))
        num = cont.append(num)
    else:
        num = int(input("Insira mais um valor"))
        num = cont.append(num)

def impar_par(num):
    if num%2 == 0:
        return print(f'Par: {num}')
    else:
       return print(f'Ímpar: {num}')

num1 = impar_par(cont[0])
num2 = impar_par(cont[1])
num3 = impar_par(cont[2])