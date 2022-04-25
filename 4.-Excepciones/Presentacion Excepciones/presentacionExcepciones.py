

class Carro:
    def __init__(self,placa):
        self.placa=placa

class FallaMecanicaException(Exception):#Clase Exception 
    def __init__(self,carro,mensaje=None):
        if mensaje is None:#Usando el atributo placa de la clase Carro
            mensaje = "Falla en la placa del carro {}".format(carro.placa)
        #Llamando el consructor de la clase padre
        super(FallaMecanicaException,self).__init__(mensaje)


if __name__ == "__main__":
    carro = Carro("ABC123")
    try:#Pasamos el objeto carro como parametro
        raise FallaMecanicaException(carro,"El sistema de frenos ha fallado")
    except FallaMecanicaException as e:
        print(e)

# import logging

# frutas = ["0-Manzana", "1 Pera", "2-Naranja", "3-Sandia", "4-Melon"]

# def seleccionarFruta (listaFrutas):
#     try:
#         print(listaFrutas)
#         indice = int(input("Ingrese el indice de la fruta: "))
#         print(F"Tu fruta favorita es {listaFrutas[indice]}")
#     except:
#         logging.error("El error es el siguiente :")
#         return seleccionarFruta(listaFrutas)
   
# seleccionarFruta(frutas)




# frutas = ["0-Manzana", "1 Pera", "2-Naranja", "3-Sandia", "4-Melon"]

# def seleccionarFruta (listaFrutas):
#     try:
#         print(listaFrutas)
#         indice = int(input("Ingrese el indice de la fruta: "))
#         print(F"Tu fruta favorita es {listaFrutas[indice]}")
#     except Exception:
#         print("Ha ocurrido un error")
#         return seleccionarFruta(listaFrutas)
   
# seleccionarFruta(frutas)



# class ValorMinimoError(Exception):
#     def __init__(self, *args):
#         if args:
#             self.mensaje = args[0]
#         else:
#             self.mensaje = None

#     def __str__(self):
#         if self.mensaje:
#             return "ValorMinimoError: {}".format(self.mensaje)
#         else:
#             return "Se ha generado el error ValorMinimoError"
 
# class ValorMinimoMaximo(Exception):
#     def __init__(self, *args):
#         if args:
#             self.mensaje = args[0]
#         else:
#             self.mensaje = None

#     def __str__(self):
#         if self.mensaje:
#             return "ValorMinimoMaximo: {}".format(self.mensaje)
#         else:
#             return "Se ha generado el error ValorMinimoError"

# minimo=10
# maximo=20

# while True:
#     try:
#         valor=int(input("Ingrese un valor entre {} y {}: ".format(minimo,maximo)))
#         if valor<minimo:
#             raise ValorMinimoError("El valor es menor que el minimo")
#         elif valor>maximo:
#             raise ValorMinimoMaximo("El valor es mayor que el maximo")

#         print("El valor esta correcto, esta entre {} y {}".format(minimo,maximo))
#         break
        
#     except ValorMinimoError as e:
#         print("Error:",e)
#     except ValorMinimoMaximo as e:
#         print("Error:",e)
#     except ValueError as e:
#         print("El valor ingresado no es un numero")

#     print("Continuamos intentando...")

   



# from ast import Return


# class FaltanPuntos(Exception):
#     def __init__(self, balance,cantidad):
       
#        super().__init__("La cantidad de puntos es {}".format(cantidad))
#        self.balance = balance
#        self.cantidad = cantidad

#     def promedio(self):
#         return self.balance / self.cantidad

# raise FaltanPuntos(100,10)

    # try:
    #     raise FaltanPuntos(100,10)
    # except FaltanPuntos as e:
    #      print(e)
    #      print(e.balance)
    #      print(e.cantidad)
    #      print(e.promedio())