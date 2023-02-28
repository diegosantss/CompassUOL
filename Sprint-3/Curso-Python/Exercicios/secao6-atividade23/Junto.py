class Calculo:
    def soma(x, y):
        return x + y

    def subtracao (x, y):
        return x - y
    
x = 4
y = 5

soma = Calculo.soma(x,y)
subtracao = Calculo.subtracao(x,y)

print(f"Somando: {x}+{y} = {soma}")
print(f"Subtraindo: {x}-{y} = {subtracao}")