class   Main:
    def menu(self):
        from alumno import Alumno
        from materia import Materia
        from calificaciones import Calificaciones
        from undoFile import UndoFile
        print("Bienvenido al programa")
        print("1. Llenar datos")
        print("2. Leer datos del fichero principal")
        print("3. Salir")
        while True:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
               print("¿De quien desea llear datos?")
               print("1. Alumno")
               print("2. Materia")
               print("3. Calificaciones")
               opcion = int(input("Ingrese una opcion: "))
                if opcion == 1:
                    print("¿Que desea hacer en el fichero alumno?")
                    print("1. Llenar fichero")
                    print("2. Leer fichero")
                    print("3. Mostrar datos")
                    print("4. Modificar fichero")
                    opcion = int(input("Ingrese una opcion: "))
                    if opcion == 1:
                        alumno = Alumno()
                        alumno.llenarFichero()
                    elif opcion == 2:
                        alumno = Alumno()
                        alumno.leerFichero()
                    elif opcion == 3:
                        alumno = Alumno()
                        alumno.mostrarDatos()
                    elif opcion == 4:
                        alumno = Alumno()
                        alumno.modificarFichero()
                    else:
                        print("Opcion incorrecta")
                elif opcion == 2:
                    print("¿Que desea hacer en el fichero materia?")
                    print("1. Llenar fichero")
                    print("2. Leer fichero")
                    print("3. Mostrar datos")
                    print("4. Modificar fichero")
                    opcion = int(input("Ingrese una opcion: "))
                    if opcion == 1:
                        materia = Materia()
                        materia.llenarFichero()
                    elif opcion == 2:
                        materia = Materia()
                        materia.leerFichero()
                    elif opcion == 3:
                        materia = Materia()
                        materia.mostrarDatos()
                    elif opcion == 4:
                        materia = Materia()
                        materia.modificarFichero()
                    else:
                        print("Opcion incorrecta")
                elif opcion == 3:
                    print("¿Que desea hacer en el fichero calificaciones?")
                    print("1. Llenar fichero")
                    print("2. Leer fichero")
                    print("3. Mostrar datos")
                    print("4. Modificar fichero")
                    opcion = int(input("Ingrese una opcion: "))
                    if opcion == 1:
                        calificaciones = Calificaciones()
                        calificaciones.llenarFichero()
                    elif opcion == 2:
                        calificaciones = Calificaciones()
                        calificaciones.leerFichero()
                    elif opcion == 3:
                        calificaciones = Calificaciones()
                        calificaciones.mostrarDatos()
                    elif opcion == 4:
                        calificaciones = Calificaciones()
                        calificaciones.modificarFichero()
                    else:
                        print("Opcion incorrecta")
                else:
                    print("Opcion incorrecta")
            elif opcion == 2:
              pass