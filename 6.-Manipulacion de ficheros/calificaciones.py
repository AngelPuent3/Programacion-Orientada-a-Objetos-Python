class Calificaciones:
    def __init__(self):
        self.matricula = str
        self.clave = str
        self.calificacion = int

    def leerFichero(self):
        try:
            fichero = open("calificaciones.txt", "r")
            self.matricula = int(fichero.readline())
            self.clave = fichero.readline()
            self.calificacion = int(fichero.readline())
            fichero.close()
            print("Fichero leido")
        except FileNotFoundError:
            print("No se encontro el fichero")
        except ValueError:
            print("Error en el fichero")
        except Exception:
            print("Error desconocido")

    def llenarFichero(self):
        self.matricula = str(input("Ingrese su matricula: "))
        self.clave = str(input("Ingrese su clave: "))
        self.calificacion = int(input("Ingrese su calificacion: "))
        #creacion del fichero
        fichero = open("calificaciones.txt", "w")
        fichero.write(str(self.matricula) + "\n")
        fichero.write(self.clave + "\n")
        fichero.write(str(self.calificacion) + "\n")
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
        print("Matricula: {}\nClave: {}\nCalificacion: {}".format(self.matricula, self.clave, self.calificacion))