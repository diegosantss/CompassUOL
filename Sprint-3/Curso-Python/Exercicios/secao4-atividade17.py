#Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def func(list):
    parte = (len(lista))//3
    list1 = list[:parte]
    list2 = list[parte:2*parte] 
    list3 = list[2*parte:]
    print(f'{list1} {list2} {list3}')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

func(lista)