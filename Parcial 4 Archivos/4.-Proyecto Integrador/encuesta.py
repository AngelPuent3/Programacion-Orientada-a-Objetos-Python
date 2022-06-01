import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter
from mediaModaMediana import *
from diagrama import *
class Encuesta(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializarMain()
        self.validaciones()

    def inicializarMain(self):
        self.title('Dulceria "Los XUXES"')
        self.minsize(600, 550)
        self.iconbitmap('descarga.ico')
        tituloLabel = tk.Label(self, text='Encuesta de satisfacción', fg='black', font=('Wide Latin', 18))
        tituloLabel.grid(row=0, column=1, pady=10)
        frameMain = tk.Frame(self, bd=8, relief='groove', bg='gray2')
        frameMain.grid(row=1, column=1, padx=10, pady=10)
        # Nombre
        nombreLabel = tk.Label(frameMain, text='1. ¿Cuál es su nombre?',fg='green3',bg='gray2',font=('Comic Sans MS',15))
        nombreLabel.grid(row=0, column=0, sticky=tk.W)
        self.nombreEntry = tk.Entry(frameMain, width=20, bg='gray2', fg='green3', font=('Comic Sans MS',15))
        self.nombreEntry.grid(row=0, column=1, sticky=tk.W)
        # Edad
        edadLabel = tk.Label(frameMain, text='2. ¿Cuál es su edad?',fg='green3',bg='gray2',font=('Comic Sans MS',15,))
        edadLabel.grid(row=1, column=0, sticky=tk.W)
        self.edadEntry = tk.Entry(frameMain, width=20, bg='gray2', fg='green3', font=('Comic Sans MS',15))
        self.edadEntry.grid(row=1, column=1, sticky=tk.W)
        # mes
        mesLabel = tk.Label(frameMain, text='3. ¿Mes de su visita?',fg='green3',bg='gray2',font=('Comic Sans MS',15))
        mesLabel.grid(row=2, column=0, sticky=tk.W)
        self.mesEntry = tk.Entry(frameMain, width=20, bg='gray2', fg='green3', font=('Comic Sans MS',15))
        self.mesEntry.grid(row=2, column=1, sticky=tk.W)
        # Email
        emailLabel = tk.Label(frameMain, text='4. ¿Cuál es su email?',fg='green3',bg='gray2',font=('Comic Sans MS',15))
        emailLabel.grid(row=3, column=0, sticky=tk.W)
        self.emailEntry = tk.Entry(frameMain, width=20, bg='gray2', fg='green3', font=('Comic Sans MS',15))
        self.emailEntry.grid(row=3, column=1, sticky=tk.W)
        # residencia
        residenciaLabel = tk.Label(frameMain, text='5. ¿Estado donde vive?',fg='green3',bg='gray2',font=('Comic Sans MS',15))
        residenciaLabel.grid(row=4, column=0, sticky=tk.W)
        self.residenciaEntry = tk.Entry(frameMain, width=20, bg='gray2', fg='green3', font=('Comic Sans MS',15))
        self.residenciaEntry.grid(row=4, column=1, sticky=tk.W)
        # pago
        pagoLabel = tk.Label(frameMain, text='6. ¿Método de pago utilizado?',fg='green3',bg='gray2',font=('Comic Sans MS',15))
        pagoLabel.grid(row=5, column=0, sticky=tk.W)
        self.pagoCombox = ttk.Combobox(frameMain, width=19, values=['Tarjeta de crédito', 'Tarjeta de débito', 'Efectivo'], background="green3",font=('Comic Sans MS',14))
        pagos=('Tarjeta de crédito', 'Tarjeta de débito', 'Efectivo')
        self.pagoCombox['values'] = pagos
        self.pagoCombox.current(0)
        self.pagoCombox.grid(row=5, column=1, sticky=tk.W)
        # experiencia
        experienciaLabel = tk.Label(frameMain, text='7. ¿Cómo fue la experiencia en su visita?',fg='green3',bg='gray2',font=('Comic Sans MS',15))
        experienciaLabel.grid(row=6, column=0, sticky=tk.W)
        self.experienciaEntry = tk.Entry(frameMain, width=20, bg='gray2', fg='green3', font=('Comic Sans MS',15))
        self.experienciaEntry.grid(row=6, column=1, sticky=tk.W)
        # compra
        compraLabel = tk.Label(frameMain, text='8. ¿Nombre del último producto que compro?',fg='green3',bg='gray2',font=('Comic Sans MS',15))
        compraLabel.grid(row=7, column=0, sticky=tk.W)
        self.compraEntry = tk.Entry(frameMain, width=20, bg='gray2', fg='green3', font=('Comic Sans MS',15))
        self.compraEntry.grid(row=7, column=1, sticky=tk.W)
        # sabor
        saborLabel = tk.Label(frameMain, text='9. ¿Sabor de su último producto?',fg='green3',bg='gray2',font=('Comic Sans MS',15))
        saborLabel.grid(row=8, column=0, sticky=tk.W)
        self.saborCombox = ttk.Combobox(frameMain, width=19, values=['Dulce', 'Salado', 'Aromático'], background="green3",font=('Comic Sans MS',14))
        sabores=('Dulce', 'Salado', 'Aromático')
        self.saborCombox['values'] = sabores
        self.saborCombox.current(0)
        self.saborCombox.grid(row=8, column=1, sticky=tk.W)
        # escala
        escalaLabel = tk.Label(frameMain, text='10. Del 1-10. ¿Cuánto nos recomendaria?',fg='green3',bg='gray2',font=('Comic Sans MS',15))
        escalaLabel.grid(row=9, column=0, sticky=tk.W)
        self.escalaEntry = tk.Entry(frameMain, width=20, bg='gray2', fg='green3', font=('Comic Sans MS',15))
        self.escalaEntry.grid(row=9, column=1, sticky=tk.W)
        # botones media moda y mediana
        # media
        mediaTituloLabel = tk.Label(frameMain, text='Media -',fg='white',bg='blue2',font=('Comic Sans MS',14))
        media= tkinter.Label(frameMain, text=c.media(),fg='white',bg='gray2',font=('Comic Sans MS',14,'bold'))
        mediaTituloLabel.grid(row=1, column=5, )
        media.grid(row=2, column=5)
        #mediaa
        medianaTituloLabel = tk.Label(frameMain, text='Mediana -',fg='white',bg='blue2',font=('Comic Sans MS',14))
        mediana= tkinter.Label(frameMain, text=c.mediana(),fg='white',bg='gray2',font=('Comic Sans MS',14,'bold'))
        medianaTituloLabel.grid(row=1, column=6 )
        mediana.grid(row=2, column=6)
        #moda
        modaTituloLabel = tk.Label(frameMain, text='Moda',fg='white',bg='blue2',font=('Comic Sans MS',14),)
        moda= tkinter.Label(frameMain, text=c.moda(), fg='white',bg='gray2',font=('Comic Sans MS',14,'bold'))
        modaTituloLabel.grid(row=1, column=7,sticky=tk.EW)
        moda.grid(row=2, column=7)
        #espacio
        
        mediana= tkinter.Label(frameMain, text="           ",bg='gray2')
        mediana.grid(row=2, column=8)
        # DIAGRAMA LISTBOX

        # diagramaTituloLabel = tk.Label(frameMain, text='Diagrama Tallo Hoja:')
        # diagrama= tkinter.Listbox(frameMain)
        # diagrama.insert(0, d.imprimirDiagrama())
        # diagramaTituloLabel.grid(row=3, column=2 )
        # diagrama.grid(row=4, column=2)

        # comentario
        # comentarioLabel = tk.Label(frameMain, text='Comentario:')
        # comentarioLabel.grid(row=10, column=0, sticky=tk.W)
        # self.comentarioEntry = tk.Entry(frameMain, width=20)
        # self.comentarioEntry.grid(row=10, column=1)

        # BOTONES

        #botones de espaciado
        spaceButton = tk.Label(frameMain, text=' ',bg='gray2',)
        spaceButton.grid(row=2, column=2)

        space2Button= tk.Label(frameMain, text=' ',bg='gray2')
        space2Button.grid(row=2, column=3)

        space3Button= tk.Label(frameMain, text=' ',bg='gray2')
        space3Button.grid(row=2, column=4)
        #guardar
        guadarButton = tk.Button(frameMain, text='Guardar', bg='gray3',fg='green3',font=('Comic Sans MS',13),activebackground="green2" ,command=self.guardar)
        guadarButton.grid(row=10, column=2,)
        #limpiar
        limpiarButton = tk.Button(frameMain, text='Limpiar', bg='gray3',fg='green3',font=('Comic Sans MS',13),activebackground="green2", command=self.limpiar)
        limpiarButton.grid(row=10, column=3,)
        #salir
        salirButton = tk.Button(frameMain, text='Salir', bg='gray3',fg='green3',font=('Comic Sans MS',13),activebackground="green2" , command=self.salir)
        salirButton.grid(row=10, column=4, )

    def validaciones(self):
        nombreValidacion = r'^[^\s]+( [^\s]+)+$'
        self.nombreRegex = re.compile(nombreValidacion)
        #edad
        edadValidacion  = r'^(\d{1,99})'
        self.edadRegex = re.compile(edadValidacion)
        #mes
        mesValidacion = r'^(\d{1,12})'
        self.mesRegex = re.compile(mesValidacion)
        #email
        emailValidacion =  r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        self.emailRegex = re.compile(emailValidacion)
        #residencia
        residenciaValidacion = r'^[^\s]'
        self.residenciaRegex = re.compile(residenciaValidacion)
        #compra
        compraValidacion = r'^[^\s]'
        self.compraRegex = re.compile(compraValidacion)
        #experiencia
        experienciaValidacion = r'^[^\s]'
        self.experienciaRegex = re.compile(experienciaValidacion)
        #escala
        escalaValidacion = r'^(\d{1,10})'
        self.escalaRegex = re.compile(escalaValidacion)
        #comenaario
        comentarioValidacion = r'^[^\s]+( [^\s]+)+$'
        self.comentarioRegex = re.compile(comentarioValidacion)

    def guardar(self):
        #nombre
        nombre = self.nombreEntry.get().strip()
        if re.match(self.nombreRegex, nombre) is None:
            messagebox.showinfo('Error', 'Campo debe incluir nombre y apellido')
            return
        #edad
        edad = self.edadEntry.get().strip()
        if re.match(self.edadRegex, edad) is None:
            messagebox.showinfo('Error', 'Edad deber ser un numero entre 1 y 99')
            return
        #email
        email = self.emailEntry.get().strip()
        if re.match(self.emailRegex, email) is None:
            messagebox.showinfo('Error', 'Formato email no valido:ejemplo@gmail.com')
            return
        #mes
        mes = self.mesEntry.get().strip()
        if re.match(self.mesRegex, mes) is None:
            messagebox.showinfo('Error', 'Mes deber ser un numero entre 1 y 12')
            return
        #residencia
        residencia = self.residenciaEntry.get().strip()
        if re.match(self.residenciaRegex, residencia) is None:
            messagebox.showinfo('Error', 'Estado donde vive debe incluir solo letras')
            return
        #experiencia
        experiencia = self.experienciaEntry.get().strip()
        if re.match(self.experienciaRegex, experiencia) is None:
            messagebox.showinfo('Error', 'Experiencia debe incluir solo letras')
            return
        #compra
        compra = self.compraEntry.get().strip()
        if re.match(self.compraRegex, compra) is None:
            messagebox.showinfo('Error', 'Compra debe incluir solo letras')
            return
        #escala
        escala = self.escalaEntry.get().strip()
        if re.match(self.escalaRegex, escala) is None:
            messagebox.showinfo('Error', 'Escala debe ser un numero entre 1 y 10')
            return
        #comentario
    
        pago=self.pagoCombox.get().strip()
        sabor=self.saborCombox.get().strip()



        #CREACION DE LOS FICHEROS
        #fichero de los datos de la encuesta
        file=open('datos.txt','a')
        file.write(nombre+'\n')
        file.write(edad+'\n')
        file.write(mes+'\n')
        file.write(email+'\n')
        file.write(residencia+'\n')
        file.write(pago+'\n')
        file.write(experiencia+'\n')
        file.write(compra+'\n')
        file.write(sabor+'\n')
        file.write(escala+'\n')
        file.close()
        #fichero para solo datos numericos
        file=open('numeros.txt','a')
        file.write(edad+'\n')
        file.write(mes+'\n')
        file.write(escala+'\n')
        file.close()

        messagebox.showinfo('Guardado', 'Datos guardados correctamente')
        self.limpiar()

    def limpiar(self):
        self.nombreEntry.delete(0,'end')
        self.edadEntry.delete(0,'end')
        self.mesEntry.delete(0,'end')
        self.emailEntry.delete(0,'end')
        self.residenciaEntry.delete(0,'end')
        self.pagoCombox.delete(0)
        self.experienciaEntry.delete(0,'end')
        self.compraEntry.delete(0,'end')
        self.saborCombox.delete(0)
        self.escalaEntry.delete(0,'end')

    def salir(self):
        self.destroy()

    def main():
        app=Encuesta()
        app.mainloop()

if __name__ == '__main__':
    Encuesta.main()



    












