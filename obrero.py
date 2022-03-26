from personas import Persona
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
