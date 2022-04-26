from tienda import *

class Microondas(Tienda,Electro):
    def __init__(self):
        super().__init__()

    def capturarInfo(self):
        global listaMicro
        listaMicro = []
        print("Cuantos microndas desea agregar?")
        numMicro = int(input())  # Agregar excepciones
        for i in range(numMicro):
            m = {}
            print("Numero de microondas: ", i + 1)
            m["codigo"] = int(input("Ingrese el codigo del microondas: "))
            m["nombre"] = str(input("Ingrese el nombre del microondas: "))
            m["tamaño"] = float(input("Ingrese el tamaño del microondas: "))
            m["precio"] = float(input("Ingrese el precio al publico del microondas: "))
            m["costo"] = float(input("Ingrese el costo del microondas: "))
            listaMicro.append(m)
        return self.menu()

    def imprimirInfo(self):
        print(listaMicro)
        f = input("Enter >>>")
        return self.menu()

    def menu(self):
        print("1. Agregar informacion")
        print("2. Imprimir informacion")
        print("3. Regresar al menu principal")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            self.capturarInfo()
        elif opcion == 2:
            self.imprimirInfo()
        elif opcion == 3:
            from tienda import Tienda
            tienda = Tienda()
            return tienda.seleccionarArticulo()
        else:
            print("Opcion no valida")
            self.menu()



