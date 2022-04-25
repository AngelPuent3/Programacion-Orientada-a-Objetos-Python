class Raiz():
    def __init__(self):
        self.x=float
        self.y=float
        
        return self.oper()

    def oper(self):
        import math
       
        print("1.Raiz de un numero\n"
              "2.Operaciones con raices\n"
              "3.Menu principal")
        p=int(input(">"))
        if p==1:  
           self.x=float(input("Escribe aqui el 1er digito >"))
           print(math.sqrt(self.x))
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
             self.x=float(input("Escribe aqui el 1er digito >"))
             self.y=float(input("Escribe aqui el 2do digito >"))
             print (math.sqrt(self.x) + math.sqrt(self.y))
            elif p==2:
                self.x=float(input("Escribe aqui el 1er digito >"))
                self.y=float(input("Escribe aqui el 2do digito >"))
                print(math.sqrt(self.x) - math.sqrt(self.y))
            elif p==3:
                self.x=float(input("Escribe aqui el 1er digito >"))
                self.y=float(input("Escribe aqui el 2do digito >"))
                print(math.sqrt(self.x) / math.sqrt(self.y))
            elif p==4:
                self.x=float(input("Escribe aqui el 1er digito >"))
                self.y=float(input("Escribe aqui el 2do digito >"))
                print(math.sqrt(self.x) * math.sqrt(self.y))
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
     