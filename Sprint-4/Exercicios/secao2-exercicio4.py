def calcular_valor_maximo(operadores, operandos) -> float:
    
    # usar o map para aplicar a função eval a cada par de operando e operador
    #x[0] é a tupla, x[0][0] é o primeiro elemento da tupla e x[0][1] é o segundo elemento da tupla
    resultados = list(map(lambda x: eval(str(x[0][0]) + x[1] + str(x[0][1])), zip(operandos, operadores)))
    return max(resultados)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores,operandos))




