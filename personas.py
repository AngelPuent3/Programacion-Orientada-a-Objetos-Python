class Persona:
    def __init__(self):
        self.nombre = str
        self.RFC = str
        self.tipoPaga = int
        self.paga = int

    def calcularSalario(self):
        pass


class Ingeniero(Persona):
    def calcularSalario(self):
        print("-----------------")
        print("Bienvenido Ingeniero")
        print("-----------------")
        print("Dar enter para continuar y calcular  el salario")
        f = input("Enter >>>")
        print("------------------------------")
        print("Su paga es por hora y proyecto")
        print("Hora y proyecto se pagan lo mismo")
        print("------------------------------")
        self.nombre = str(input("Ingrese su nombre\n>"))
        self.RFC = str(input("Ingrese su RFC\n>"))
        self.tipoPaga = float(input("Ingrese su paga $$$\n>"))
        hour = int(input("¿Cuanta horas trabajo esta semana?\n>"))
        print("Tuvo algun proyecto\n1.-Si\n2.-NO")
        f = int(input(">"))
        if f == 1:
            print("Cuantos proyectos tuvo?")
            proyecto = int(input(">"))
            self.paga = hour * proyecto
            self.paga = self.paga * self.tipoPaga
            print("-------------")
            print("Nombre:", self.nombre, "\nRFC:", self.RFC, "\nSu salario total es: $", self.paga)
            print("-------------")
            F = input("Enter >>>")
            from main import main
            main()
            return
        elif f == 2:
            self.paga = hour * self.tipoPaga
            print("-------------")
            print("Nombre:", self.nombre, "\nRFC:", self.RFC, "\nSu salario total es: $", self.paga)
            print("-------------")
            F = input("Enter >>>")
            from main import main
            main()
            return
        else:
            print("Error, vuelve a intentarlo")
            elsE = Ingeniero()
            elsE.calcularSalario()


class Obrero(Persona):
    def calcularSalario(self):
        print("-----------------")
        print("Bienvenido Obrero")
        print("-----------------")
        print("Dar enter para continuar y calcular  el salario")
        f = input("Enter >>>")
        print("----------------------------")
        print("Su paga es por dia")
        print("----------------------------")
        self.nombre = str(input("Ingrese su nombre\n>"))
        self.tipoPaga = float(input("Ingrese su paga $$$\n>"))
        self.RFC=str(input("Ingrese su RFC\n>"))
        day = int(input("¿Cuantos dias trabajo esta semana?\n>"))
        self.paga = self.tipoPaga * day
        print("-------------")
        print("Obrero:")
        print("Nombre:", self.nombre, "\nRFC:", self.RFC, "\nSu salario total es: $", self.paga)
        print("-------------")
        F=input("Enter >>>")
        from main import main
        main()
        return


class Medico(Persona):
    def calcularSalario(self):
        print("-----------------")
        print("Bienvenido Medico")
        print("-----------------")
        print("Dar enter para continuar y calcular  el salario\n")
        f = input("Enter >>>")
        print("----------------------------")
        print("Su paga es por consulta")
        print("Bonus de 10% si surten su receta en farmacia")
        print("----------------------------")
        self.nombre = str(input("Ingrese su nombre\n>"))
        self.tipoPaga = float(input("Ingrese su paga $$$\n>"))
        self.RFC("Ingrese su RFC \n>")
        consulte = int(input("¿Cuantas consultas tuvo esta semana?\n>"))
        recete = float(input("¿Cual fue su total en efectivo esta semana por sus recetas $$$?\n>"))
        recete = (recete / 100) * 10
        self.paga = self.tipoPaga * consulte
        self.paga = self.paga + recete
        print("-------------")
        print("Medico:")
        print("Nombre:", self.nombre, "\nRFC:", self.RFC, "\nSu salario total es: $", self.paga)
        print("-------------")
        F = input("Enter >>>")
        from main import main
        main()
        return

