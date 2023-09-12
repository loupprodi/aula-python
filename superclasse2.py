class Super:
    def hello(self):
        print("Olá, sou a superclasse!")
class Sub (Super):
    def hello(self):
        print("Olá, sou a subclasse!")
class Subsub (Sub):
    def hello(self):
        print("Olá, sou a subsubclasse!")

if __name__ == "__main__":
    mensagem = int(input(
    'digite a mensagem que deseja ver: 1 para super, 2 para sub, 3 para sub da sub'))
    if mensagem == 1:
        teste = Super()
    elif mensagem == 2:
        teste = Sub()
    elif mensagem == 3:
        teste = Subsub()
    else:
        print('opção inválida')
    teste.hello()
