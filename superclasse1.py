class Super:
    def hello(self):
        print("Olá, sou a superclasse!")
        
class Sub (Super): # herdou método 'hello' da superclasse 'Super'
    def hello(self):
        print("Olá, sou a subclasse!")
teste = Sub()
teste.hello()
