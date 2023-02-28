from Aviao import Aviao

avioes = []
aviao1 = Aviao('BOIENG456', '1500 km/h', 400)
avioes.append(aviao1)
aviao2 = Aviao('Embraer Praetor 600', '863 km/h', 14)
avioes.append(aviao2)
aviao3 = Aviao('Antonov An-2', '258 km/h', 12)
avioes.append(aviao3)

for aviao in avioes:
    print(f'O avião de modelo "{aviao.modelo}" possui uma velocidade máxima de "{aviao.velocidade_maxima}", capacidade para "{aviao.capacidade}" passageiros e é da cor "{Aviao.cor}".')
