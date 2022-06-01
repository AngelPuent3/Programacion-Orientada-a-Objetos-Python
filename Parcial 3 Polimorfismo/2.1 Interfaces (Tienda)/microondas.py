from tienda import *
class Microondas(Electro,Tienda):
    def __init__(self):
        super().__init__()
        

    def capturarInfo(self):
        global listaMicro
        listaMicro=[]
        print("Cuantos microndas desea agregar?")
        numMicro=int(input())#Agregar excepciones
        for i in range(numMicro):
            m={}
            print("Numero de microondas: ",i+1)
            m["codigo"]=int(input("Ingrese el codigo del microondas: "))
            m["nombre"]=str(input("Ingrese el nombre del microondas: "))
            m["tamaño"]=float(input("Ingrese el tamaño del microondas: "))
            m["precio"]=float(input("Ingrese el precio al publico del microondas: "))
            m["costo"]=float(input("Ingrese el costo del microondas: "))
            listaMicro.append(m) 
        return self.menu()
        
    
    def imprimirInfo(self):
        print(listaMicro)
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

        
        # global microlist
        # microlist=[]
        # m=Microondas()
        # print("Ingrese la informacion del microondas")
        # m.codigo=int(input("Ingrese el codigo del microondas: "))
        # m.nombre=str(input("Ingrese el nombre del microondas: "))
        # m.tamaño=float(input("Ingrese el tamaño del microondas: "))
        # m.precio=float(input("Ingrese el precio del microondas: "))
        # m.costo=float(input("Ingrese el costo del microondas: "))
        # microlist.append(m)
        # return self.menu()

    #imprimo mi lista creada
    # def __str__(self):
    #     print("Microondas: <Codigo: {0},Nombre: {1}, Tamaño: {2},Precio: {3}, Costo: {4}>".format(microlist[0].codigo,microlist[0].nombre,microlist[0].tamaño,microlist[0].precio,microlist[0].costo))
        
   

# class Microondas:
#     def __init__(self,codigo,nombre,tamaño,precio,costo):
#         self.codigo=codigo
#         self.nombre=nombre
#         self.tamaño=tamaño
#         self.precio=precio
#         self.costo=costo
    
#     def __str__(self):
#         return "Codigo: "+str(self.codigo)+"\nNombre: "+str(self.nombre)+"\nTamaño: "+str(self.tamaño)+"\nPrecio: "+str(self.precio)+"\nCosto: "+str(self.costo)

# class ListMicro():
#     def __init__(self):
#         self.listmicro=[]
    
#     def agrergarmicroondas(self,m):
#         self.listmicro.append(m)
    
#     def registroMicro():
#         print("Registro de Microondas")
#         for micro in self.listmicro:
#             print(micro)
            
       
# class MenuMicro():
#     def __init__(self):
#         self.matrizMicroondas = ListMicro()
        
#     def mainMicro(self):
#         print("1. Agregar informacion")
#         print("2. Imprimir informacion")
#         print("3. Salir")
#         opcion=int(input("Ingrese una opcion: "))
#         if opcion==1:
#             self.capturarInfo()
#         elif opcion==2:
#             self.imprimirInfo()
#         elif opcion==3:
#             return
#         else:
#             print("Opcion no valida")
#             self.mainMicro()

#     def capturarInfo(self):
#         codigo=int(input("Ingrese el codigo del microondas: "))
#         nombre=str(input("Ingrese el nombre del microondas: "))
#         tamaño=float(input("Ingrese el tamaño del microondas: "))
#         precio=float(input("Ingrese el precio del microondas: "))
#         costo=float(input("Ingrese el costo del microondas: "))
#         m=Microondas(codigo,nombre,tamaño,precio,costo)
#         self.matrizMicroondas.capturarInfo(m)

#     def imprimirInfo(self):
#         self.matrizMicroondas.registroMicro()


# class Juez:
#     def __init__(self,codigo,nombre,experiencia):
#         self.codigo=codigo
#         self.nombre=nombre
#         self.experiencia=experiencia

#     def __str__(self):
#         return "Juez: <Codigo juez: {0}, Nombre juez: {1}, Años de experiencia: {2}>".format(self.codigo,self.nombre,self.experiencia)

# class Jueces:
#     def __init__(self):
#         self.diccionarioJuez=[]

#     def agregarJuez(self,newJuez):
#         self.diccionarioJuez.append(newJuez)

#     def registroJuez(self):
#         print("Registro Juez\n")
#         for juez in self.diccionarioJuez:
#             print(juez)

# class MenuJuez:
#     def __init__(self):
#         self.matrizJuez=Jueces()

#     def mainJuez(self):
#         while True:
#             print("Menu Juez")
#             print("---------")
#             print("1.-Añadir Juez\n2.-Visualizar Juez\n3.-Determinar condena\n4.-Visualizar Condena\n5. Menu ladron \n6.Regresar a menu principal")

#             opcion = int(input("> "))
#             if 1 == opcion:
#                 self.agregarJuez()
#             elif 2 == opcion:
#                 self.printJuez()
#             elif 3 == opcion:
#                 from Sucursal import MenuSucursal
#                 menu=MenuSucursal()
#                 menu.mainSucursal()
#             elif 4 == opcion:
#                 from Ladron import MenuLadron
#                 menuJuez=MenuLadron()
#                 menuJuez.mainLadron()
#             elif 5 == opcion:
#                 from main import mainP
#                 mainP()
#             else:
#                 print('Esa opcion no existe')

#     def agregarJuez(self):
#         codigo = input("Ingrese el codigo del juez:")
#         nombre = input("Ingrese el nombre del juez:\n")
#         experiencia = input("Ingrese los años de experiecia\n>")
#         newJuez = Juez(codigo, nombre,experiencia)
#         self.matrizJuez.agregarJuez(newJuez)

#     def printJuez(self):
#         self.matrizJuez.registroJuez()
        