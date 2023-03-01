class Pessoa:
    def __init__(self, id):
        self.id = id
        self.nome = None
        
    def set_nome(self, nome):
        self.__nome = nome
        
    def get_nome(self):
        return self.__nome
