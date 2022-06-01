from abstract import Variables
class Potencia(Variables):
    def __init__(self):
        try:
            self.x=float(input("Escribe aqui el 1er digito >"))
            self.y=float(input("Escribe aqui el 2do digito >"))
            return self.oper()
        except ValueError:
            print("Error, ingrese un numero valido")
            return self.__init__()

    def oper(self):
         print(self.x**self.y)
         from main import menuprincipal
         return menuprincipal()


Potencia()
