from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Ventana de prueba")#titulo de la ventana
raiz.resizable(True,True)#Da la opcion de que la ventana sea redimensionable
#raiz.iconbitmap("zozo.ico")#icono de la ventana
#raiz.geometry("650x350")#tamaño de la ventana
raiz.config(bg="purple")#color de fondo de la ventana
miframe= Frame()
#miframe.pack(side="left" anchor="s")
miframe.pack(side="left", fill="both", )
miframe.config(bg="green") #color de fondo del marco
miframe.config(width="650", height="350") #tamaño de la ventana
miframe.config(bd=10) #ancho del borde
miframe.config(relief="groove") #relieve de la ventana

raiz.mainloop() #Bucle infinito que matinene la ventana abierta
#Siempre debe ir al final del codigo


