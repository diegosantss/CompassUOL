from functools import reduce

def calcula_saldo(lancamentos):
    #reduce irá aplicar a função de somar ('lambda x, y: x + y') a cada par da lista até reduzir a um unico valor.
    #map cria uma lista no qual aplica a função que irá transformar os valores igual a 'D' em negativos e aplicar a função inteira.
    saldo = reduce(lambda x, y: x + y, map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos))
    return saldo
    
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
saldo = calcula_saldo(lancamentos)
print(saldo) 
