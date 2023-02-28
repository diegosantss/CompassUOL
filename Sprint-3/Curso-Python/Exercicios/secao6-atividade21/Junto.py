#Organizado apenas em um arquivo todas as classes e realizando o teste para colocar na udemy

class Passaro:
    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        pass


class Pato(Passaro):
    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")


# Teste das classes
pato = Pato()
print("Pato")
pato.voar()
pato.emitir_som()

pardal = Pardal()
print("Pardal")
pardal.voar()
pardal.emitir_som()