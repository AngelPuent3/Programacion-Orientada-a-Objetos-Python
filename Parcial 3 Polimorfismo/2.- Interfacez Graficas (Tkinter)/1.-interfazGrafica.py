#libreria para manejo de ventanas
from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Ventana de prueba")#titulo de la ventana
raiz.resizable(True,True)#Da la opcion de que la ventana sea redimensionable
raiz.iconbitmap("zozo.ico")#icono de la ventana
raiz.geometry("650x350")#tamaño de la ventana
raiz.config(bg="white")#color de fondo de la ventana
raiz.mainloop() #Bucle infinito que matinene la ventana abierta
#Siempre debe ir al final del codigo


