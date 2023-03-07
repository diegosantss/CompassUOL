lista_strings = [['a', '2', '3'], ['b', '5', '6']]
lista_inteiros = [[int(item) if item.isdigit() else item for item in sublist] for sublist in lista_strings]

print(lista_inteiros)