


class Saludo(Exception):
    def __init__(self, *args):
        if args:
            self.mensaje = args[0]
            self.mensajeDos=args[0]
        else:
            self.mensaje = None

    def __str__(self):
        if self.mensaje:
            return "Saludo: {} y {}".format(self.mensaje, self.mensajeDos)
        else:
            return "Se ha generado el error Saludo Exception"


class Tienda:
    def __init__(self):
        self.nombre = "gansito"
        self.precio = "$10 pesos"

    def __str__(self):
        return "Nombre: {}\nPrecio: {}".format(self.nombre, self.precio)

    def comprar():
        print("Entras a una tienda y deseas comprar algo")
        print("El señor esta dormido y lo tienes que despertar sin hacerlo enojar")
        print("¿Que le dirias?")
        while True:
            try:
                valor=str(input("Ingrese un valor entre {} y {}: ".format(saludo1, saludo2)))
                if valor!=saludo1 and valor!=saludo2:
                    raise Saludo("El saludo no es valido ")

                print("El valor esta correcto, esta entre {} y {}".format(saludo1, saludo2))
                print("Compraste un {} por {}".format(nombre, precio))

                break  
            except Saludo as e:
                print("Hiciste enojar al señor, no puedes comprar nada")
                print("Error:",e)
     
            print("Continuamos intentando...")

        

saludo1="hola"
saludo2="hello"
nombre="gansito"
precio="$10 pesos"

c=Tienda
c.comprar()





