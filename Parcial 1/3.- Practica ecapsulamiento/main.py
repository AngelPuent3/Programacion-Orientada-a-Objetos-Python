class Encapsulamiento:
    def __init__(self):
        __atributoPrivado="Soy un atributo privado"
        atributoPublico="Soy un atributo publico"

    def getAtributoPrivado(self):
        return self.__atributoPrivado()

    def setAtributoPrivado(self, atributoPriv):
        self.__atributoPrivado=atributoPriv

e=Encapsulamiento()
e.__atributoPrivado="Trantando de cambiar valor"
e.atributoPublico="Cambiando de valor"
print(e.__atributoPrivado)
print(e.atributoPublico)
e.setAtributoPrivado("Cambiando de  mensaje a atributoPrivado")
print(e.getAtributoPrivado())




