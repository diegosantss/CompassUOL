#----------COMANDO DA QUESTÃO:----------
#Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.

#Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:

#Nome do estudante, Três maiores notas, em ordem decrescente, Média das três maiores notas e com duas casas decimais de precisão
#O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:
#Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
#Exemplo:
#Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
#Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
#Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
#round, map e sorted

import csv

def calcular_media(top3_notas):
    return round(sum(top3_notas) / 3, 2)

with open('estudantes.csv', newline='') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=',')

    # Criar lista de dicionários para armazenar informações dos estudantes
    estudantes = []
    for linha in arquivo:
        # Extrair nome e notas do estudante
        nome = linha[0]
        notas = list(map(int, linha[1:]))

        top3_notas = sorted(notas, reverse=True)[:3]
        media = calcular_media(top3_notas)

        # Adicionar informações do estudante à lista
        info_estudantes = {
            'nome': nome,
            'notas': top3_notas,
            'media': media
        }
        estudantes.append(info_estudantes)

# Ordenar lista de estudantes por nome
estudantes = sorted(estudantes, key=lambda x: x['nome'])

# Gerar relatório
for estudante in estudantes:
    nome = estudante['nome']
    notas = estudante['notas'][:3]
    media = estudante['media']
    print(f"Nome: {nome} Notas: {notas} Média: {media}")
