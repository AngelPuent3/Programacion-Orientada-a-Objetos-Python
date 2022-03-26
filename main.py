from personas import *
def main():
    print("------------------------")
    print("Calculadora de salarios")
    print("------------------------")
    print("¿Quien esta usando?...")
    print("1.-Obrero\n2.-Ingeniero\n3.-Medico\n4.-Salir")
    fmain=int(input(">"))
    if fmain==1:
        o=Obrero()
        o.calcularSalario()
    elif fmain==2:
        i=Ingeniero()
        i.calcularSalario()
    elif fmain==3:
        m=Medico()
        m.calcularSalario()
    elif fmain==4:
        exit("Adios :)")
    else:
        print("Error, vuelve a intentarlo")
        main()
main()
