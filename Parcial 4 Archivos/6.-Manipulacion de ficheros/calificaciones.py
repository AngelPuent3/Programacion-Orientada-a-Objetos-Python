class Calificaciones:
    def __init__(self):
        self.matricula = str
        self.clave = str
        self.calificacion = float

    def llenarFichero(self):
        self.matricula = str(input("Ingrese su matricula: "))
        self.clave = str(input("Ingrese su clave: "))
        self.calificacion = float(input("Ingrese su calificacion: "))
        #creacion del fichero
        fichero = open("calificaciones.txt", "w")
        fichero.write("matricula" + str(self.matricula) + "\n")
        fichero.write("clave :" + self.clave + "\n")
        fichero.write("calificacion : "+ str(self.calificacion) + "\n")
        fichero.close()
        print("Fichero creado")

    def modificarFichero(self):
        print("Modificar fichero")
        self.leerFichero()
        self.mostrarDatos()
        print("¿Que dato quiere modificar?")
        print("1. Matricula")
        print("2. Clave")
        print("3. Calificacion")
        fichero = open("calificaciones.txt", "w")
        opcion = int(input("Ingrese su opcion: "))
        if opcion == 1:
            self.matricula = str(input("Ingrese su matricula: "))
            fichero.write(str(self.matricula) + "\n")
        elif opcion == 2:
            self.clave = str(input("Ingrese su clave: "))
            fichero.write(self.clave + "\n")
        elif opcion == 3:
            self.calificacion = int(input("Ingrese su calificacion: "))
            fichero.write(str(self.calificacion) + "\n")
        else:
            print("Opcion no valida")
        fichero.close()

    def mostrarDatos(self):
        try:
            print(open("calificaciones.txt", "r").read())
        except Exception:
            print("Fichero inexistente o vacio")
