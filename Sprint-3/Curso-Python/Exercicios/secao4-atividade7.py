#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Faça um programa que gere uma nova lista a partir da lista 'a', contendo apenas números ímpares.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x % 2 != 0]
print(b)