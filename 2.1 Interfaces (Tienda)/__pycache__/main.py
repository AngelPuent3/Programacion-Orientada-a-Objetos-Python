def main():
    from microondas import Microondas
    from freidora import Freidora
    from estufa import Estufa
    from refri import Refrigerador
    print("Seleccione el articulo que desea comprar")
    print("1. Microondas, 2. Freidora, 3. Estufa, 4. Refrigerador")
    op=int(input("Ingrese el codigo del articulo que desea: "))
    if op==1:
        m1=Microondas()
        m1.menu()
    elif op==2:
        f=Freidora()
        f.menu()
    elif op==3:
        e=Estufa()
        e.menu()
    elif op==4:
        r=Refrigerador()
        r.menu()
    else:
        return main()

main()