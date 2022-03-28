from PERSONAS import Persona
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
            print("¿Cuantos proyectos tuvo?")
            proyecto = int(input(">"))
            self.paga = hour * proyecto
            self.paga = self.paga + self.tipoPaga
            print("-------------")
            print("Nombre: Ing.", self.nombre, "\nRFC:", self.RFC, "\nSu salario total es: $", self.paga)
            print("-------------")
            F = input("Enter >>>")
            from main import main
            main()
            return
        elif f == 2:
            self.paga = hour + self.tipoPaga
            print("-------------")
            print("Nombre: Ing.",self.nombre,"\nRFC:",self.RFC,"\nSu salario total es: $",self.paga)
            print("-------------")
            F = input("Enter >>>")
            from main import main
            main()
            return
        else:
            print("Error, vuelve a intentarlo")
            elsE = Ingeniero()
            elsE.calcularSalario()
