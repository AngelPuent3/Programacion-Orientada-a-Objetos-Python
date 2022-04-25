#Codigo para resolver una formula cuadratica
from math import sqrt
class Ecuacion():
    def __init__(self):
        self.interfaz()

    def calcular(self, A, B, C):
        if ((B**2)-4*A*C) < 0:
            print("La solución de la ecuación es con números complejos")
        else:
            x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
            x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
            print("""\
Las soluciones de la ecuación son:
x1 = {}
x2 = {} """.format(x1, x2))
    def interfaz(self):
        A = int(input("Ingrese el numero que esta al cuadrado\n"))
        B = int(input("Ingrese el numero lineal\n"))
        C = int(input("Ingrese el término independiente\n"))
        
        self.calcular(A, B, C)
        f = input("Enter >>")
        from main import menuprincipal
        return menuprincipal()

Ecuacion()

