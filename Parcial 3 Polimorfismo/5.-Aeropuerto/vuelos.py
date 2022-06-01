from abstract import *
class Vuelo(DatosVuelo,Aeropuerto):
    def __init__(self,numVuelo,fecha,hora,origen,destino,plazas,plazaTurista):
        super().__init__()
        self.numVuelo = numVuelo
        self.fecha = fecha
        self.hora = hora
        self.origen = origen
        self.destino = destino
        self.plazas = plazas
        self.plazaTurista = plazaTurista

    def __str__(self):
        return "Vuelo:\nNumero de Vuelo: {0} Fecha: {1} Hora: {2} Origen: {3} Destino: {4} Plazas: {5} Plazas Turista: {6}".format(self.numVuelo,self.fecha,self.hora,self.origen,self.destino,self.plazas,self.plazaTurista)

class Vuelos(Añadir):
    def __init__(self):
        self.dichovuelos = []

    def agregarDatos(self,newvuelo):
        self.dichovuelos.append(newvuelo)

    def registroDatos(self):
        for i in self.dichovuelos:
            print(i)

class MenuVuelo(Menus):
    def __init__(self):
        self.matrizVuelo=Vuelos()

    def mainClass(self):
        while True:
            print("Menu Vuelo")
            print("--------------")
            print("1. Agregar Vuelo\n2. Mostrar Vuelos\n3. Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                self.agregarDatos()
            elif opcion == 2:
                self.mostrarDatos()
            elif opcion == 3:
                from main import main
                main()
            else:
                print("Opcion no valida")
                return self.mainClass()
        
    def agregarDatos(self):
        numVuelo = input("Ingrese el numero de vuelo: ")
        fecha = input("Ingrese la fecha del vuelo: ")
        hora = input("Ingrese la hora del vuelo: ")
        origen = input("Ingrese el origen del vuelo: ")
        destino = input("Ingrese el destino del vuelo: ")
        plazas = int(input("Ingrese el numero de plazas del vuelo: "))
        plazaTurista = int(input("Ingrese el numero de plazas turista del vuelo: "))
        newvuelo = Vuelo(numVuelo,fecha,hora,origen,destino,plazas,plazaTurista)
        self.matrizVuelo.agregarDatos(newvuelo)

    def mostrarDatos(self):
        self.matrizVuelo.registroDatos()
        