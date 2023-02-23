#Escreva um código Python que imprime os números pares de 0 até 20 (incluso)
lista = []
for i in range(21):
    if i%2 == 0:
        lista.append(i)
        print(i)
    else:
        lista.pop