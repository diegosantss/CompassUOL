class Pessoa:
    def __init__(self, id):
        self.id = id
        self.nome = None
        
    def set_nome(self, nome):
        self.nome = nome
        
    def get_nome(self):
        return self.nome

pessoa = Pessoa(0)
pessoa.set_nome('Fulano De Tal')
print(pessoa.get_nome()) # Saída: Fulano De Tal
