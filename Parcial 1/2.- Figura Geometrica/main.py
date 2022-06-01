class Figura:
    def __init__(self,num1,num2):
        self.nomFigura="Rectangulo"
        self.num1=num1
        self.num2=num2
    def calcularArea(self):
        area=self.num1*self.num2
        return area
    def calcularPerimetro(self):
        perimetroR=(self.num1*2)+(self.num1*2)
        return perimetroR
def imprimirDatos():
    r=Figura(20,9)
    area=r.calcularArea()
    perimetroR=r.calcularPerimetro()
    print("El area es:",area)
    print("El perimetro es:",perimetroR)

imprimirDatos()
