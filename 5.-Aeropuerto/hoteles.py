class Hotel:
    def __init__(self, codigo, direccion, telefono, plazas):
        self.codigo = codigo
        self.direccion = direccion
        self.telefono = telefono
        self.plazas = plazas

    def __str__(self):
        return "Hotel:\nCodigo: {0} Direccion: {1} Telefono: {2} Plazas: {3}".format(self.codigo, self.direccion,
                                                                                     self.telefono, self.plazas)


class Hoteles:
    def __init__(self):
        self.dichoteles = []

    def agregarDatos(self, newhotel):
        self.dichoteles.append(newhotel)

    def registroDatos(self):
        for i in self.dichoteles:
            print(i)


class MenuHotel():
    def __init__(self):
        self.matrizHotel = Hoteles()

    def mainClass(self):
        while True:
            print("Menu Hotel")
            print("--------------")
            print("1. Agregar Hotel\n2. Mostrar Hoteles\n3. Menu Principal")
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
        codigo = int(input("Ingrese el codigo del hotel: "))
        direccion = str(input("Ingrese la direccion del hotel: "))
        telefono = int(input("Ingrese el telefono del hotel: "))
        plazas = int(input("Ingrese el numero de plazas del hotel: "))
        newhotel = Hotel(codigo, direccion, telefono, plazas)
        self.matrizHotel.agregarDatos(newhotel)

    def mostrarDatos(self):
        self.matrizHotel.registroDatos()