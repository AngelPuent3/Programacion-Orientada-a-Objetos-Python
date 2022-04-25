from cmath import e
from tienda import Tienda
class Estufa(Tienda):
    def __init__(self):
        super().__init__()

    def capturarInfo(self):
        global listaEs
        listaEs=[]
        print("Cuantos estufa desea agregar?")
        num=int(input())#Agregar excepciones
        for i in range(num):
            e={}
            print("Numero de estufa: ",i+1)
            e["codigo"]=int(input("Ingrese el codigo del estufa: "))
            e["nombre"]=str(input("Ingrese el nombre del estufa: "))
            e["tamaño"]=float(input("Ingrese el tamaño del estufa en cm: "))
            e["precio"]=float(input("Ingrese el precio al publico del estufa: "))
            e["costo"]=float(input("Ingrese el costo del estufa: "))
            listaEs.append(e) 
        return self.menu()

    def imprimirInfo(self):
        print(listaEs)
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
            self.menu()