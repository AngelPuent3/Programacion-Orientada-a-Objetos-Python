class Calcudadora:
    """def __init__(self):
        self.x=0
        self.y=0"""
    def oper('''aelf''', s):
        suma == self.x + self.y
        return suma

    def oper(self, sum1, sum2):
        resta == self.x - self.y
        return resta

    def oper(self):
        multi == self.x * self.y
        return multi

    def oper(self):
        div == self.x / self.y
        return div

#n1=Calcudadora((float(input("Escribe aqui el 1er digito"))),(float(input("Escribe aqui el 2do digito"))))

print("Escoje la operacion que quiere realizar")
print("-------")
print("MENU")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")
print("-------")
x = int(input(">"))

if x == 1:
   suma = Calcudadora()
   suma.oper()
   print(suma)
elif x == 2:
    resta = Calcudadora()
    resta = resta.oper()

elif x == 3:
    multi = Calcudadora()
    multi = multi.oper()

elif x==4:
    div = Calcudadora()
    div = div.oper()

else:
    print("**Error**")













