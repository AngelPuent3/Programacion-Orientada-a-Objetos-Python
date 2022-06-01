from tienda import *
class Freidora(Electro,Tienda):
    def __init__(self):
        super().__init__()

    def capturarInfo(self):
        global listaFrei
        listaFrei=[]
        print("Cuantos freidora desea agregar?")
        num=int(input())#Agregar excepciones
        for i in range(num):
            fe={}
            print("Numero de freidora: ",i+1)
            fe["codigo"]=int(input("Ingrese el codigo del freidora: "))
            fe["nombre"]=str(input("Ingrese el nombre del freidora: "))
            fe["tamaño"]=float(input("Ingrese el tamaño del freidora en cm: "))
            fe["precio"]=float(input("Ingrese el precio al publico del freidora: "))
            fe["costo"]=float(input("Ingrese el costo del freidora: "))
            listaFrei.append(fe) 
        return self.menu()

    def imprimirInfo(self):
        print(listaFrei)
        f=input("Enter >>>")
        return self.menu()

    def menu(self):
        print("1. Agregar informacion")
        print("2. Imprimir informacion")
        print("3. Regresar al menu principal")
        opcion=int(input("Ingrese una opcion: "))
        if opcion==1:
            self.capturarInfo()
        elif opcion==2:
            self.imprimirInfo()
        elif opcion==3:
            from tienda import Tienda
            tienda=Tienda()
            return tienda.seleccionarArticulo()
            
        else:
            print("Opcion no valida")
            return self.menu()