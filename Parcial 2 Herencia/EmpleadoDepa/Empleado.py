global profesor
global alumno
profesor=list()
alumno=list()
class Profesor:
    rut=""
    clave=""
    pass

class Alumno:
    pass

def añadirEmpleado():
    print ("Añadir Alumno")
    e=alumno()

    e.Matricula = int(input("Ingresa la matricula\n>"))
    e.nombre = str(input("Ingresa el nombre \n>"))
    e.grupo = int(input("Ingrese eñ departamento \n>"))
    e.sueldoHr = float(input("Ingrese el sueldo por hora\n>"))
    e.numHrs = int(input("Ingrese su numero de horas trabajadas\n>"))
    e.salario = round(e.numHrs*e.sueldoHr, 2)

def menu():
    while True:
        print ("**Menu**\n"
               "1.Registrar alumno\n"
               "2.Listar alumno\n"
               "3.Buscar Alumno"
               "4. Salir")
        opE= int(input(">"))
        if opE == 1:
            registarAlumno()
        elif opE == 2:
            listarAlumno()
        elif opE == 3:
            buscarAlumno()
        elif opE == 4:
            exit("Adios! ☺")
        else:
            print("*Error*")


def mainP():
    registrarP()
    print ("Carga de sistema")
    rut = input("Rut")
    clave=input("Password")

    existe=False
    for u in profesor:
        if u.rut == rut and u.clave == clave:
            existe=True
            break
    if existe ==True:
        print ("Correcto")
    else:
        print ("Incorrecto")



def registrarP ():
    profeU = Profesor()

    profeU.rut = "1"
    profeU.clave = "123"

    profesor.append(profeU)