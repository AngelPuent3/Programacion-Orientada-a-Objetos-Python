from random import *
numlist=[1,2,3,4,5,6,7,8,9,0,6,5,7,1,0,5]
class Cuenta:
    def __init__(self):
        print("***ATM**")
        print("___________")
        self._titular=str(input("¿Cual es su nombre?\n >"))
        self._Nocuenta="945 7889 4510 1024"
        self._saldo=int(29345)
        self._cantidad=float
        self._edad=int(input("¿Cual es tu edad?\n >"))
        print("___________")
        print("Bienvenido")
        print("Nombre",self._titular)
        print("Edad",self._edad,"años")
        print("Numero de cuenta\n",self._Nocuenta)
        print("___________")


    def consultaSaldo(self):
        print("Su saldo disponible es $",self._saldo,"pesos")

    def retirar(self):
        if self._edad <= 18 and self._edad >= 35:
            self._cantidad = float(input("Saldo a retirar\n >"))
            if self._cantidad > self._saldo:
                print("**Error**\n"
                      "Cantidad no valida")
            elif self._cantidad <= self._cantidad:
                self._saldo = self._saldo - self._cantidad
                print("Saldo actual")
                print(self._saldo)
        else:
            print("Edad no validad para reirar")


    def depositar(self):
        self._cantidad=int(input("Cual es su cantidad a despositar \n >"))
        if self._cantidad > 0:
           if self._edad >= 18 and self._edad <=35:
               print ("Usted tiene una bonificacion del 30% sobre su deposito")
               self._cantidad=(self._cantidad/100)*30
               print ("Su bonificacion es:", self._cantidad)
               self._saldo = self._cantidad + self._saldo
               print("Su saldo actualizado", self._saldo)
           else:
               print("No tiene bonificacion ")
               self._saldo = self._cantidad + self._saldo
               print("Su saldo actualizado", self._saldo)
        elif self._cantidad < 0 :
            print ("Cantidad no permitida")
        else:
            print("**Error**")
a = Cuenta()