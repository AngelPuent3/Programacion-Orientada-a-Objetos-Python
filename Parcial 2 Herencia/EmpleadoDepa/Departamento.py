from main import imprimir

class Departament0:

    claveDepto = int
    nombre = str
    jefe = str
    telefono = int


def añadirDep():
    print("**Añadir Departamento**")

    d = Departament0()

    d.claveDepto = int(input("Ingresa la clave\n>"))
    d.nombre = str(input("Ingresa el nombre\n>"))
    d.jefe = str(input("Ingresa el nombre del jefe\n>"))
    d.telefono = int(input("Ingresar telefono\n>"))

    departamento.append(d)


def visualizarDep():
    for d in departamento:
       print("**Registro departamentos**")
       print("-------------")
       print("\nClave:", d.claveDepto,"\nNombre:",d.nombre,"\nJefe:",d.jefe,"\nTelefono:",d.telefono)
       print("-------------")
       f=input("Enterr>>>")

def menuD():
    print("**Menu**\n"
          "1.Añadir departamento\n"
          "2.Visualizar departamento\n"
          "3.Regresar\n"
          "4.Salir")
    opE = int(input(">"))
    if opE == 1:
        añadirDep()
    elif opE == 2:
        visualizarDep()
    elif opE ==3:
        imprimir()
    elif opE == 4:
        exit("Adios! ☺")
    else:
        print("*Error*")

departamento = list()