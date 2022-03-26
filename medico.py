from personas import Persona
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
        self.RFC=str(input("Ingrese su RFC \n>"))
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