global listJuez
global listCondena
listJuez=list()
listCondena=list()

class Juez:

    def listaJuez(self):

       j=Juez()
       j.codigoJuez(int(input("Ingrese el codigo del juez \n >")))
       j.nombreJuez(str(input("Ingrese el nombre del juez\n>")))
       j.añosServicio(int(input("Ingrese los años del servicio del juex\n")))
       listJuez.append(j)
        
    def visualizarJuez(self):
        for j in listJuez:
            print("**Registro Juez*")
            print("-------------")
            print("Codigo de Juez:", j.codigoJuez, "\nNombreJuez:", j.nombreJuez, "\n Años de servicio:", jañosServicio)
            print("-------------")

    def determinarCondena(self):
        jc=Juez()
        jc.numJuez(int(input("Ingrese el numero de Juez\n>")))
        jc.casoJuez(int(input("Ingrese el numerto de caso \n>")))
        jc.condena(str(input("¿Lo va condenar?\n")))
        jc.tipoCondena(str(input("¿Cual es su condena?\n >")))
        jc.tiempoCondena(int(input("Ingrese su condena en años \n >")))
        listCondena.append(jc)

    def visualizarCondena(self):
        for jc in listCondena:
            print("**Registro Juez*")
            print("-------------")
            print("Numero de Juez", jc.numuez, "\nCaso juez:", jc.casoJuez, "\n Lo va condenar?",jc.tipoCondena, "\n Tipo de condena:", jc.tipoCondena,
                  "\nTiempo de condena", jc.tiempoCondena)
            print("-------------")
            



