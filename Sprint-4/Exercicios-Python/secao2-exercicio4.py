#----------COMANDO DA QUESTÃO:----------
#A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.

#Veja o exemplo:
#Entrada
#operadores = ['+','-','*','/','+']
#operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

#Aplicar as operações aos pares de operandos
#[ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 
#Obter o maior dos valores = 12
#Na resolução da atividade você deverá aplicar as seguintes funções:
#max, zip e map

def calcular_valor_maximo(operadores, operandos) -> float:
    
    # usar o map para aplicar a função eval a cada par de operando e operador
    #x[0] é a tupla, x[0][0] é o primeiro elemento da tupla e x[0][1] é o segundo elemento da tupla
    resultados = list(map(lambda x: eval(str(x[0][0]) + x[1] + str(x[0][1])), zip(operandos, operadores)))
    return max(resultados)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores,operandos))




