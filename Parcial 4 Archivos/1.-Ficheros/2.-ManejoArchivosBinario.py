#Manipulacion de archivos binarios
introRobo="C:\Users\loki\Desktop\Programacion Orientada a Objetos\Parcial 4 Archivos\introRobo.jpg"

with open(introRobo, "rb") as f:
    data = f.read()
    print(data)
#lognitud de archivo
print(len(data))
#tipo de archivo
print(type(data))
