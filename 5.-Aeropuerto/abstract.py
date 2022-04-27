from abc import ABC,abstractmethod

from abc import ABC,abstractmethod

class Aeropuerto(ABC):
    def __init__(self):
        self.codigo=int
        self.direccion=str
        self.nombre=str
        self.telefono=int
        self.numVuelo=int
        self.fecha=str
        self.hora=int
        self.origen=str
        self.destino=str
        self.plazas=int
        self.plazaTurista=int

class HotelAbstract(ABC):
    def __init__(self):
        self.codigo=int
        self.direccion=str
        self.telefono=int
        self.plazas=int

class SucursalAbstract(ABC):
    def __init__(self):
        self.codigo=int
        self.direccion=str
        self.telefono=int

class TuristaAbstract(ABC):
    def __init__(self):
        self.codigo=int
        self.nombre=str
        self.direccion=str
        self.telefono=int

 class VuelosAbstract(ABC):
     def __init__(self):
         self.numVuelo = int
         self.fecha = str
         self.hora = float
         self.origen = str
         self.destino = str
         self.plazas = int
         self.plazaTurista = int



class Add ():

     def __str__(self):
         pass

class Add2():

    def agregarDatos(self):
        pass

    def registroDatos(self):
        pass

class Menus():
    def mainClass(self):
        pass

    def agregarDatos(self):
        pass

    def mostrarDatos(self):
        pass
