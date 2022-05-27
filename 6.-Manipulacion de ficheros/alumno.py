class Alumno:
    def __init__(self):
        self.nombre = str
        self.matricula= str
        self.edad = int
        self.semestre = int

    
    def llenarFichero(self):
        self.nombre = str(input("Ingrese su nombre: "))
        self.matricula = str(input("Ingrese su matricula: "))
        self.edad = int(input("Ingrese su edad: "))
        self.semestre = int(input("Ingrese su semestre: "))
        #creacion del fichero
        fichero = open("alumno.txt", "w")
        fichero.write(self.nombre + "\n")
        fichero.write(self.matricula + "\n")
        fichero.write(str(self.edad) + "\n")
        fichero.write(str(self.semestre) + "\n")
        fichero.close()
        print("Fichero creado")


    def leerFichero(self):
        try:
            fichero = open("alumno.txt", "r")
            self.nombre = fichero.readline()
            self.matricula = int(fichero.readline())
            self.edad = int(fichero.readline())
            self.semestre = int(fichero.readline())
            fichero.close()
            print("Fichero leido")
        except FileNotFoundError:
            print("No se encontro el fichero")
        except ValueError:
            print("Error en el fichero")
        except Exception:
            print("Error desconocido")

    def mostrarDatos(self):
        print("Nombre: {}\nMatricula: {}\nEdad: {}\nSemestre: {}".format(self.nombre, self.matricula, self.edad, self.semestre))

    def modificarFichero(self):
        #se modifica los datos del fichero
        fichero = open("alumno.txt", "w")
        print("Ingrese los nuevos datos: ")
        print("¿Que dato desea modificar?")
        print("1. Nombre")
        print("2. Matricula")
        print("3. Edad")
        print("4. Semestre")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            self.nombre = str(input("Ingrese su nombre: "))
            fichero.write(self.nombre + "\n")
        elif opcion == 2:
            self.matricula = str(input("Ingrese su matricula: "))
            fichero.write(self.matricula + "\n")
        elif opcion == 3:
            self.edad = int(input("Ingrese su edad: "))
            fichero.write(str(self.edad) + "\n")
        elif opcion == 4:
            self.semestre = int(input("Ingrese su semestre: "))
            fichero.write(str(self.semestre) + "\n")
        fichero.close()
        print("Fichero modificado")
      


