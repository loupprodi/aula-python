from pessoa import Pessoa

class PessoaJuridica(Pessoa):

    def __init__(self,CNPJ,nome,idade):
        super().__init__(nome,idade)
        self.CNPJ = CNPJ

    def getCNPJ(self):
        return self.CNPJ

    def setCNPJ(self, CNPJ):
        self.CNPJ = CNPJ

if __name__ == "__main__":

    pessoa1 = Pessoa("Raul",20)
    pessoa1 = PessoaJuridica("99.999.9999/99",pessoa1.getNome(),pessoa1.getIdade())

    print(pessoa1.getNome(),pessoa1.getIdade(),pessoa1.getCNPJ())

    pessoa1.setNome("Joao")
    pessoa1.setIdade(33)
    pessoa1.setCNPJ("88.888.888/88")

    print(pessoa1.getNome(),pessoa1.getIdade(),pessoa1.getCNPJ())
