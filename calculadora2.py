class Calculadora:

    def soma(self, a, b):
        return a + b
    def subtrai(self, a, b):
        return a - b
    def multiplica(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            print("Erro: divisão por zero")
        else:
            return a / b
