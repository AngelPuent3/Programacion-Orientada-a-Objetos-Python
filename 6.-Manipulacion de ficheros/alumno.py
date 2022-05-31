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
        fichero.write("nombre :" + self.nombre + "\n")
        fichero.write("matricula" + self.matricula + "\n")
        fichero.write("edad :" + str(self.edad) + "\n")
        fichero.write("semestre:" + str(self.semestre) + "\n")
        fichero.close()
        print("Fichero creado")

    def mostrarDatos(self):
        try:
            print(open("alumno.txt", "r").read())
        except Exception:
            print("Fichero inexistente o vacio")

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
      


