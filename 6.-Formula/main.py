def menuprincipal():
    print("Bienvenido al menú de opciones\n 1.-Formula\n 2.-Potencia\n 3.-Raiz\n 4.-Salir")
    opcion=int(input(">"))
    if opcion==1:
        from formula import Ecuacion
        Ecuacion()
    elif opcion==2:
        from potencia import Potencia
        Potencia()
    elif opcion==3:
        from raiz import Raiz
        Raiz()
    elif opcion==4:
        print("Gracias por usar el programa")
    else:
        print("**Error**")  

menuprincipal()