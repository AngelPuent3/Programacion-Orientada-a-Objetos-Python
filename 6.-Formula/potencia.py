class Potencia():
    def __init__(self):
        self.x=float(input("Escribe aqui el 1er digito >"))
        self.y=float(input("Escribe aqui el 2do digito >"))
        return self.oper()

    def oper(self):
         print(self.x**self.y)
         from main import menuprincipal
         return menuprincipal()


Potencia()
