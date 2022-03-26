class persona:
    def __init__(self):
        self.nombre=""
        self.dinero=0.0
        self.rfc=""

    def pago(self):
        pass

class obrero(persona):

    def pago(self):
        print("Su nombre")
        self.nombre=(input("Nombre >"))
        print("Su RFC")
        self.rfc=(input("RFC >"))
        print("Cuanto le pagan?")
        self.dinero=float(input("Pago >"))
        print("Dias trabajados")
        dia=int(input(">"))
        self.dinero=self.dinero*dia
        print("Su nombre -", self.nombre)
        print("Su rfc -",self.rfc)
        print("Su pago total",self.dinero)



class inge(persona):

    def pago(self):
        print("Su nombre")
        self.nombre = (input("Nombre >"))
        print("Su RFC")
        self.rfc = (input("RFC >"))
        print("Cuanto le pagan?")
        self.dinero = float(input("Pago >"))
        print("Numero hora")
        hora=int(input(">"))
        print("Numero de proyectos")
        pro=int(input(">"))
        self.dinero=(self.dinero*hora)+(self.dinero*pro)
        print("Su nombre -", self.nombre)
        print("Su rfc -", self.rfc)
        print("Su pago total", self.dinero)



class doc(persona):

    def pago(self):
        print("Su nombre")
        self.nombre = (input("Nombre >"))
        print("Su RFC")
        self.rfc = (input("RFC >"))
        print("Cuanto le pagan?")
        self.dinero = float(input("Pago >"))
        print("Numero consultas")
        con=int(input(">"))
        print("Cuanto genero en farmacia")
        far=float(input(">"))
        far= (far/100)*10
        self.dinero=(self.dinero*con)
        self.dinero=self.dinero+far
        print("Su nombre -", self.nombre)
        print("Su rfc -", self.rfc)
        print("Su pago total", self.dinero)


def menu():
    print("Hola, quien lo esta usando")
    print("1.- Obrero 2.-Ingeniero 3.-Doctor")
    op=int(input(">"))
    if op==1:
        print("Le pagan por dia")
        ob=obrero()
        ob.pago()
        print("Desea hacer algo mas?")
        print("1.- Si 2.-No")
        op2=int(input(">"))
        if op2==1:
            menu()
        else:
            exit("Adios")
    elif op==2:
        print("Le pagan por hora y proyecto")
        ing=inge()
        ing.pago()
        print("Desea hacer algo mas?")
        print("1.- Si 2.-No")
        op2 = int(input(">"))
        if op2 == 1:
            menu()
        else:
            exit("Adios")
    elif op==3:
        print("Le pagan por consulta mas una comision del 10% si su receta la compran esta farmacia")
        dr=doc()
        dr.pago()
        print("Desea hacer algo mas?")
        print("1.- Si 2.-No")
        op2 = int(input(">"))
        if op2 == 1:
            menu()
        else:
            exit("Adios")
menu()
