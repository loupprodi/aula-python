class Calculadora:

    def __init__(self, a, b):

        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            print("Erro: divisão por zero")
        else:
            return self.a / self.b

