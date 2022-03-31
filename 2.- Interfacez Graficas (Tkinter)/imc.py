from abc import ABC, abstractmethod

class Persona(ABC):
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



class Alumno(Persona):
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

    def recomendaciones(self):
        print("Estas son sus recomendaciones")
        if self.imc < 18.5:
            print("Consumir mas productos de origen animal")  
        elif self.imc >= 18.5 and self.imc < 25:
            print("Consumir mas lacteos ademas de hacer rutinas que impliquen fuerza")
        elif self.imc >= 25 and self.imc < 30:
            print("Consumir mas frutas y verduras, ademas de aumentar el ejercico")
        else:
            exit("Adios")
