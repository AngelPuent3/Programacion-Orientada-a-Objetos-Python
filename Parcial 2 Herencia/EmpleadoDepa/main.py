empleado = list()
departamento = list()

class Emplead0:

    numControl=int
    nombre=str
    departamento=int
    sueldoHr=float
    numHrs=int
    salario=float

def añadirEmpleado():
    print ("Añadir Empleado")
    e=Emplead0()

    e.numControl = int(input("Ingresa el numero de control\n>"))
    e.nombre = str(input("Ingresa el nombre \n>"))
    e.departamento = int(input("Ingrese eñ departamento \n>"))
    e.sueldoHr = float(input("Ingrese el sueldo por hora\n>"))
    e.numHrs = int(input("Ingrese su numero de horas trabajadas\n>"))
    e.salario = round(e.numHrs*e.sueldoHr, 2)

    empleado.append(e)

def visualizarEmpleado():
    print("**Registro de emplados**")
    for e in empleado:
        print ("-------------")
        print ("Numero control:" ,e.numControl,"\nNombre:",e.nombre,
               "\nDepartamento:",e.departamento,"\nSueldo por hora",
               e.sueldoHr,"\nHoras trabajadas:",e.numHrs,"\nSu salario:",e.salario)
        print("-------------")
        f = input("Enterr>>>")

def menuE():
    while True:
        print ("**Menu**\n"
               "1.Añadir Empleado\n"
               "2.Visualizar empleado\n"
               "3.Regresar\n"
               "4. Salir")
        opE= int(input(">"))
        if opE == 1:
            añadirEmpleado()
        elif opE == 2:
            visualizarEmpleado()
        elif opE == 3:
            imprimir()
        elif opE == 4:
            exit("Adios! ☺")
        else:
            print("*Error*")

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


def imprimir():
    print("**Menu Principal\n"
          "1.- Empleados\n"
          "2.- Departamento\n"
          "3._ Salir")
    opM=int(input(">"))
    while True:
        if opM == 1:
            menuE()
        elif opM == 2:
            menuD()
        elif opM == 3:
            exit("Adios! ☺")
        else:
            print("*Error*")

imprimir()