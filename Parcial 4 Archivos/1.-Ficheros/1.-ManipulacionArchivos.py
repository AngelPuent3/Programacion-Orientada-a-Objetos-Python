#creacio y manipulacion de archivos
#creacion de archivos
newArchivo=("archivo.txt")

archivo=open(newArchivo,"w")
archivo.write("Hola Mundo\nsegunda linea")
archivo.close()

#leer archivos
archivo=open(newArchivo,"r")
contenidoArchivo=archivo.read()
# print(contenidoArchivo)

#Leer lineas


#agregar lineas a un archivo extistente
archivo=open(newArchivo,"a")
archivo.write("\nTercera linea")
archivo.close()

archivo=open(newArchivo,"r")
for l in archivo:
    print(l)
print("\n")
archivo.close()

#eliminar archivos
import os
os.remove(os.getcwd()+"\\"+str(newArchivo))
# write=escribir archivo
# r=leer archivo