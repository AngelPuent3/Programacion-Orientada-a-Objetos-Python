from tienda import *
class Refrigerador(Electro,Tienda):
    def __init__(self):
        super().__init__()

    def capturarInfo(self):
        global listaRefri
        listaRefri=[]
        print("Cuantos refrigeradores desea agregar?")
        num=int(input())#Agregar excepciones
        for i in range(num):
            r={}
            print("Numero de refrigerador: ",i+1)
            r["codigo"]=int(input("Ingrese el codigo del refrigerador: "))
            r["nombre"]=str(input("Ingrese el nombre del refrigerador: "))
            r["tamaño"]=float(input("Ingrese el tamaño del refrigerador en cm: "))
            r["precio"]=float(input("Ingrese el precio al publico del refrigerador: "))
            r["costo"]=float(input("Ingrese el costo del refrigerador: "))
            listaRefri.append(r) 
        return self.menu()

    def imprimirInfo(self):
        print(listaRefri)
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