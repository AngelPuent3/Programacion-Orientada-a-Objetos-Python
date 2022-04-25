# class Turista:
#     def __init__(self,codigo,nombre,direccion,telefono):
#         self.codigo = codigo
#         self.nombre = nombre
#         self.direccion = direccion
#         self.telefono = telefono

#     def __str__(self):
#         return "Turista:\nCodigo: {0},Nombre: {1},Direccion: {2} , Telefono: {3}".format(self.codigo,self.nombre,self.direccion,self.telefono)

# class Turistas:
#     def __init__(self):
#         self.dicTuristas = []

#     def agregarTurista(self,newTurista):
#         self.dicTuristas.append(newTurista)

#     def registroTuristas(self):
#         print("Registro Turista")
#         for i in self.dicTuristas:
#             print(i)

# class MenuTurista:
#     def __init__(self):
#         self.matrizTurista=[]

#     def mainTurista(self):
#         while True:
#             print("Menu Turista")
#             print("--------------")
#             print("1. Agregar Turista\n2. Mostrar Turistas\n3. Salir")
#             opcion = int(input("Ingrese una opcion: "))
#             if opcion == 1:
#                 self.agregarTurista()
#             elif opcion == 2:
#                 self.mostrarTurista()
#             elif opcion == 3:
#                 break
#             else:
#                 print("Opcion no valida")

#     def agregarTurista(self):
#         codigo = int(input("Ingrese el codigo del turista: "))
#         nombre = str(input("Ingrese el nombre del turista: "))
#         direccion = str(input("Ingrese la direccion del turista: "))
#         telefono = int(input("Ingrese el telefono del turista: "))
#         newTurista = Turista(codigo,nombre,direccion,telefono)
#         self.matrizTurista.agregarTurista(newTurista)
#         return self.mainTurista()

#     def mostrarTurista(self):
#         self.matrizTurista.registroTuristas()
#         return self.mainTurista()

class Turista:
    def __init__(self,codigo,nombre,direccion,telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        print ("")
        return "Turista :\nCodigo: {0},Nombre: {1},Direccion: {2} , Telefono: {3}".format(self.codigo,self.nombre,self.direccion,self.telefono)

class Turistas:
    def __init__(self):
        self.diccionarioTurista=[]

    def agregarTurista(self,newTurista):
        self.diccionarioTurista.append(newTurista)

    def registroTurista(self):
        print("Registro Turista\n")
        for turista in self.diccionarioTurista:
            print(turista)

class MenuTurista:
    def __init__(self):
        self.matrizTurista=Turistas()

    def mainTurista(self):
        while True:
            print("Menu Juez")
            print("---------")
            print("1.-Añadir Turista\n2.-Visualizar Turista\n3.-Regresar a menu principal")

            opcion = int(input("> "))
            if 1 == opcion:
                self.agregarTurista()
            elif 2 == opcion:
                self.printTurista()
            elif 3 == opcion:
                from main import main
                main()
            else:
                print('Esa opcion no existe')
                return self.mainTurista()

    def agregarTurista(self):
        codigo = int(input("Ingrese el codigo del turista: "))
        nombre = str(input("Ingrese el nombre del turista: "))
        direccion = str(input("Ingrese la direccion del turista: "))
        telefono = int(input("Ingrese el telefono del turista: "))
        newTurista = Turista(codigo,nombre,direccion,telefono)
        self.matrizTurista.agregarTurista(newTurista)
      

    def printTurista(self):
        self.matrizTurista.registroTurista()

