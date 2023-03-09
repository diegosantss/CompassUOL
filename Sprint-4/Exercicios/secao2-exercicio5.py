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
