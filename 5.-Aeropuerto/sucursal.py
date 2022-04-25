


class Sucursal:
    def __init__(self,codigo,direccion,telefono):
        self.codigo = codigo
        self.direccion = direccion
        self.telefono = telefono
    
    def __str__(self):
        return "Sucursales:\nCodigo: {0} Direccion: {1} Telefono: {2}".format(self.codigo,self.direccion,self.telefono)

class Sucursales:
    def __init__(self):
        self.dicsucursales = []

    def agregarSucursal(self,newsucursal):
        self.dicsucursales.append(newsucursal)
    
    def registroSucursales(self):
        for i in self.dicsucursales:
            print(i)

class MenuSucursal:
    
    def __init__(self):
        self.matriz=Sucursales()

    def mainSucursal(self):
        while True:
            print("Menu Sucursal")
            print("--------------")
            print("1. Agregar Sucursal\n2. Mostrar Sucursales\n3. Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                self.agregarSucursal()
            elif opcion == 2:
                self.mostrarSucursal()
            elif opcion == 3:
                from main import main
                main()
            else:
                print("Opcion no valida")
                return self.mainSucursal()

    def agregarSucursal(self):
        codigo = input("Ingrese el codigo de la sucursal: ")
        direccion = input("Ingrese la direccion de la sucursal: ")
        telefono = input("Ingrese el telefono de la sucursal: ")
        newsucursal = Sucursal(codigo,direccion,telefono)
        self.matriz.agregarSucursal(newsucursal)

    def mostrarSucursal(self):
        self.matriz.registroSucursales()
