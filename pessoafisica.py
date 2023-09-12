from pessoa import Pessoa

class PessoaFisica(Pessoa):

    def __init__(self, CPF, nome, idade):

        super().__init__(nome,idade)
        self.CPF = CPF

    def setCPF(self, CPF):
        self.CPF = CPF

    def getCPF(self):
        return self.CPF

if __name__ == "__main__":

    pessoa1 = Pessoa("Raul",33)
    pessoa1 = PessoaFisica("430.151.728-67", pessoa1.getNome(), pessoa1.getIdade())
    print(pessoa1.getCPF(),pessoa1.getNome(),pessoa1.getIdade())

    pessoa1.setCPF("999.999.999-99")
    pessoa1.setNome("Joao")
    pessoa1.setIdade(49)
    print(pessoa1.getCPF(),pessoa1.getNome(),pessoa1.getIdade())
