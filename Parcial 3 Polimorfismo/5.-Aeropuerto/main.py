def main():
    print("Bienvenido al sistema de contratos")
    print("Seleccione una opcion")
    print("1.-Llenar datos\n2.-Crear contrato")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        from contrato import Contratato
        contrato = Contratato()
        contrato.llenarDatos()
    elif opcion == 2:
        from contrato import Contratato
        contrato = Contratato()
        contrato.llenarContrato()
    else:
        print("Opcion no valida")
        main()
        
main()