from abstract import Variables
class Raiz(Variables):
    def __init__(self):
        super().__init__()
        return self.oper()

    def oper(self):
        import math
       
        print("1.Raiz de un numero\n"
              "2.Operaciones con raices\n"
              "3.Menu principal")
        p=int(input(">"))
        if p==1:
            try:  
                self.a=float(input("Escribe aqui el 1er digito >"))
                print(math.sqrt(self.a))
            except ValueError:
                print("Error, ingrese un numero valido")
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
                try:
                    self.a=float(input("Escribe aqui el 1er digito >"))
                    self.b=float(input("Escribe aqui el 2do digito >"))
                    print (math.sqrt(self.x) + math.sqrt(self.y))
                except ValueError:
                    print("Error, ingrese un numero valido")
            elif p==2:
                try:
                    self.x=float(input("Escribe aqui el 1er digito >"))
                    self.y=float(input("Escribe aqui el 2do digito >"))
                    print(math.sqrt(self.x) - math.sqrt(self.y))
                except ValueError:
                    print("Error, ingrese un numero valido")
            elif p==3:
                try:
                    self.x=float(input("Escribe aqui el 1er digito >"))
                    self.y=float(input("Escribe aqui el 2do digito >"))
                    print(math.sqrt(self.x) / math.sqrt(self.y))
                except ValueError:
                    print("Error, ingrese un numero valido")
            elif p==4:
                try:
                    self.x=float(input("Escribe aqui el 1er digito >"))
                    self.y=float(input("Escribe aqui el 2do digito >"))
                    print(math.sqrt(self.x) * math.sqrt(self.y))
                except ValueError:
                    print("Error, ingrese un numero valido")
            else:
                print("**Error**")
                self.oper()
        elif p==3:
            from main import menuprincipal
            return menuprincipal()
        else:
            print("**Error**")
            self.oper()

Raiz()
     