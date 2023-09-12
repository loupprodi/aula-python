class Pessoa:

    def __init__(self,nome,idade):

        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

if __name__ == "__main__":

    pessoa1 = Pessoa("João", 20)
    print(pessoa1.getNome(),pessoa1.getIdade())

    pessoa1.setNome("Raul")
    pessoa1.setIdade(33)

    print(pessoa1.getNome(),pessoa1.getIdade())

    

        
