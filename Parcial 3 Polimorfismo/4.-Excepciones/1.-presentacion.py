#Ejemplos de excepciones

'''def division(a,b):
    return a/b

division(25,0)
print("Hoy es Martes!!!")'''

'''def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    
division(25,0)
print("Hoy es Martes!!!")

#Estructura try except finally

def ejemplo():
    try:
        print("Hola")
    except:#TipoExcepción
        print("Adios")
    finally:#Opcional
        print("Adios")'''


frutas = ["0-Manzana", "1 Pera", "2-Naranja", "3-Sandia", "4-Melon"]

def seleccionarFruta (listaFrutas):
    try:
        print(listaFrutas)
        indice = int(input("Ingrese el indice de la fruta: "))
        print(F"Tu frusta favorita es {listaFrutas[indice]}")
    except IndexError:
        print(f"El indice no existe, debe estar entre 0 y {len(listaFrutas)-1}")
    except ValueError:
        print("El indice debe ser un entero")
   
seleccionarFruta(frutas)
seleccionarFruta(frutas)
seleccionarFruta(frutas)



# def division(a,b):
#     try:
#         return a/b
#     except Exception:
#         print("No se puede dividir entre 0")
   
# division(25,0)


'''def ejemploArgs(*args):
    total=sum(args)

ejemploArgs(1,2,3,A,5)'''


    





