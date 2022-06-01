#Codigo para resolver una formula cuadratica
from math import sqrt
from abstract import Variables
class Ecuacion(Variables):
    def __init__(self):
        super().__init__()
        self.interfaz()

    def calcular(self, a, b, c):
        if ((b**2)-4*a*c) < 0:
            print("La solución de la ecuación es con números complejos")
        else:
            x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
            x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
            print("""\
Las soluciones de la ecuación son:
x1 = {}
x2 = {} """.format(x1, x2))
    def interfaz(self):
        try:
            a = int(input("Ingrese el numero que esta al cuadrado\n"))
            b = int(input("Ingrese el numero lineal\n"))
            c = int(input("Ingrese el término independiente\n"))
        except ValueError:
            print("Error, ingrese un numero valido")
            self.interfaz()
        
        self.calcular(a, b, c)
        f = input("Enter >>")
        from main import menuprincipal
        return menuprincipal()

Ecuacion()

