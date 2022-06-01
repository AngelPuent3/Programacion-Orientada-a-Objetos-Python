import math
class Calcudadora:
    def __init__(self):
        self.x=float(input("Escribe aqui el 1er digito >"))
        self.y=float(input("Escribe aqui el 2do digito >"))

class Suma(Calcudadora):
    def oper(self):
        print (self.x+self.y)

class Resta(Calcudadora):
    def oper(self):
        print (self.x-self.y)

class Div(Calcudadora):
    def oper(self):
        print (self.x/self.y)

class Multi(Calcudadora):
    def oper(self):
        print (self.x*self.y)

class Potencia(Calcudadora):
     def oper(self):
         print(self.x**self.y)

class Raiz(Calcudadora):
    def oper(self):
        print("1.Raiz de un numero\n"
              "2.Operaciones con raices\n")
        p=int(input(">"))
        if p==1:
           print(math.sqrt(self.x),math.sqrt(self.y))
        elif p==2:
            print("-------")
            print("*MENU*")
            print("1.Suma")
            print("2.Resta")
            print("3.Division")
            print("4.Multiplicacion")
            print("------")
            p = int(input(">"))
            if p==1:
             print (math.sqrt(self.x) + math.sqrt(self.y))
            elif p==2:
                print(math.sqrt(self.x) - math.sqrt(self.y))
            elif p==3:
                print(math.sqrt(self.x) / math.sqrt(self.y))
            elif p==4:
                print(math.sqrt(self.x) * math.sqrt(self.y))
            else:
                print("**Error**")
        else:
            print("**Error**")