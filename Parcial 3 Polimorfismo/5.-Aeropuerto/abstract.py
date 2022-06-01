#Llmao a la libreria abc
from abc import ABC, abstractmethod

#Clase abstracta para el modulo hotel
class DatosHotel(ABC):
    def __init__(self):
        self.codigo = int
        self.direccion = str
        self.telefono = int
        self.plazas = int
#Clase abstracta para el modulo sucursal
class DatosSucursal(ABC):
    def __init__(self):
        self.codigo=int
        self.direccion=str
        self.telefono=int

#Clase abstracta para el modulo vuelo
class DatosVuelo(ABC):
    def __init__(self):
        self.numVuelo=int
        self.fecha=str
        self.hora=str
        self.origen=str
        self.destino=str
        self.plazas=int
        self.plazaTurista=int

#Clase abstracta para el modulo turista
class DatosTurista(ABC):
    def __init__(self):
        self.codigo=int
        self.nombre=str
        self.direcion=str
        self.telefono=int

#interfaz para las clases singular
class Aeropuerto():
    def __str__(self):
        pass

#interfaz para las clases plural(se usara si se agrega +1)
class Añadir():
    def agregarDatos(self):
        pass

    def registroDatos(self):
        pass

#Interfaz para las clases de menus
class Menus():
    def mainClass(self):
        pass

    def agregarDatos(self):
        pass

    def printDatos(self):
        pass

    