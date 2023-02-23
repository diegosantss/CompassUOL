#Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
import json 

#abrindo o arquivo
abrir = open("person.json", "r")

#carregando as informações do arquivo usando um modulo de json
arq = json.load(abrir)
print(arq)