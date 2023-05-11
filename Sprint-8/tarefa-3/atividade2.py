

animais = ["gato", "cachorro", "leão", "elefante", "girafa", "tigre", "rato", "pato", "coelho", "macaco", "cobra", "papagaio", "galo", "vaca", "ovelha", "porco", "cavalo", "sapo", "urso", "camelo"]

animais.sort()

for animal in animais:
    print(animal)

with open("animais.csv", "w") as file:
    for animal in animais:
        file.write(animal + "\n")
