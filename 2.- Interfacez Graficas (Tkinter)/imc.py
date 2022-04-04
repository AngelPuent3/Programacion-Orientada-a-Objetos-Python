from abc import ABC, abstractmethod

class Datos(ABC):
    def __init__(self):
        self.nombre = str
        self.edad = int
        self.peso = float
        self.altura = float
        self.direccion = str
        self.telefono = int
        self.sexo = str
        self.temperatura = float
        self.presionArterial = float
        self.glucosa = float
        
    @abstractmethod
    def calcularIMC(self):
        pass

    @abstractmethod
    def calcularSignos(self):
        pass

    @abstractmethod
    def recomendaciones(self):
        pass
           

class Paciente(Datos):
    def __init__(self):
        super().__init__()
        self.imc=0
        
    def calcularIMC(self):
        print("Vamos a calcular su IMC")
        self.peso = float(input("Ingrese su peso: "))
        self.altura = float(input("Ingrese su altura: "))
        self.imc = self.peso / (self.altura * self.altura)
        print("Su IMC es: ", self.imc)
        if self.imc < 18.5:
            print("Peso bajo")  # <18.5     
        elif self.imc >= 18.5 and self.imc < 25:
            print("Peso normal")
        elif self.imc >= 25 and self.imc < 30:
            print("Sobrepeso")
        elif self.imc >= 30 and self.imc < 35:
            print("Obesidad grado I")
        else:
            exit("Adios")

    def calcularSignos(self):
        print("Vamos a calcular sus signos")
        self.temperatura = float(input("Ingrese su temperatura: "))
        self.presionArterial = float(input("Ingrese su presion arterial: "))
        self.glucosa = float(input("Ingrese su glucosa: "))
        print("Su temperatura es: ", self.temperatura)
        print("Su presion arterial es: ", self.presionArterial)
        print("Su glucosa es: ", self.glucosa)

    def recomendacionesIMC(self):
        print("Estas son sus recomendaciones")
        if self.imc < 18.5:
            print("Consumir mas productos de origen animal")  
        elif self.imc >= 18.5 and self.imc < 25:
            print("Consumir mas lacteos ademas de hacer rutinas que impliquen fuerza")
        elif self.imc >= 25 and self.imc < 30:
            print("Consumir mas frutas y verduras, ademas de aumentar el ejercico")
        else:
            exit("Adios")
            
     def recomendacionesSignos(self):
        print("Estas son sus recomendaciones")
        if self.temperatura < 35 and self.presionArterial < 90 and self.glucosa < 100:
            print("Consumir mas productos de origen animal")  
        elif self.temperatura >= 35 and self.temperatura < 37:
            print("Consumir mas lacteos ademas de hacer rutinas que impliquen fuerza")
        elif self.temperatura >= 37 and self.temperatura < 39:
            print("Consumir mas frutas y verduras, ademas de aumentar el ejercico")
        else:
            exit("Adios")


def main ():
    print("Bienvenido\nCalculadora de IMC\nEnter para continuar >>>")
    f=input()
    paciente = Paciente()
    print("1.- Calcular IMC\n2.- Calcular Signos\n3.- Recomendaciones\n4.- Salir")
    while True:
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            paciente.calcularIMC()
        elif opcion == 2:
            paciente.calcularSignos()
        elif opcion == 3:
            print("1.- Recomendacion IMC 2.- Recomendaciones Signos")
            opcionFor=int(input(">"))
            if opcionFor == 1:
                paciente.recomendacionesIMC()
            elif opcionFor ==2:
                paciente.recomedacionesSignos()  
        elif opcion == 4:
            exit("Adios")
        else:
            print("Opcion no valida")
main()
 #excepcion  la clasificacion de tipos de excep´ciones, aq eu se referi la propagacion de exepciones, gestion, y crecion y manjeo de excecionbes unidad por el usuario
