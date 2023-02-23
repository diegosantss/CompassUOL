#Escreva um código Python que lê do teclado o nome e a idade de um usuário e que imprima apenas o ano em que ele completará 100 anos.

#Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem'). Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas.

import datetime

nome = str(input('Digite seu nome'))
idade = int(input('Digite sua idade'))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
restante = 100 - idade
ano = int(date.strftime("%Y")) + restante
print(ano)