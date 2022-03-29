from logging import root
from tkinter import * #libreria para manejo de ventanas
from tkinter import ttk 

raiz = Tk()
a = ttk.Frame(raiz, padding=10) #crea un marco con un padding de 10
a.grid(column=150, row=150, sticky=(N, W, E, S)) #posicionamiento del marco
ttk.Label(a, text="Hola Mundo").grid(column=0, row=0, sticky=(N, W, E, S)) #crea un label con texto
ttk.Button(a, text="Salir", command=raiz.destroy).grid(column=1, row=0, sticky=(N, W, E, S)) #crea un boton con texto y funcion
raiz.mainloop() #Bucle infinito que matinene la ventana abierta