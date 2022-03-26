from personas import Persona
def main():
    print("------------------------")
    print("Calculadora de salarios")
    print("------------------------")
    print("¿Quien esta usando?...")
    print("1.-Obrero\n2.-Ingeniero\n3.-Medico\n4.-Salir")
    fmain=int(input(">"))
    if fmain==1:
        from obrero import Obrero
        o=Obrero()
        o.calcularSalario()
    elif fmain==2:
        from ingeniero import Ingeniero
        i=Ingeniero()
        i.calcularSalario()
    elif fmain==3:
        from medico import Medico
        m=Medico()
        m.calcularSalario()
    elif fmain==4:
        exit("Adios :)")
    else:
        print("Error, vuelve a intentarlo")
        main()
main()
