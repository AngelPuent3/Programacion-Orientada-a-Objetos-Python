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

    @abstractmethod
    def __str__(self):
        pass

class Add(ABC):
    @abstractmethod
    def agregarDatos(self):
        pass
    @abstractmethod
    def registroDatos(self):
        pass

class Menus(ABC):
    @abstractmethod
    def mainClass(self):
        pass

    @abstractmethod
    def agregarDatos(self):
        pass
    @abstractmethod
    def mostrarDatos(self):
        pass

