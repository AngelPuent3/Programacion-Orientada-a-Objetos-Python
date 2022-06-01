from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def comer(self):
        pass

class Pato(Animal):
    def __init__(self, nombre, edad,color):
        super().__init__(nombre, edad)
        self.color = color
        
    def comer(self):
        print("El {} esta comiendo".format(self.nombre))