from abc import ABC,abstractmethod
class Electro:
    def imprimirInfo(self):
        pass

    def capturarInfo(self):
        pass


class Tienda(ABC):
    def __init__(self):
        self.codigo=0
        self.nombre=""
        self.tamaño=""
        self.precio=0
        self.costo=0

    @abstractmethod
    def menu(self):
        pass

