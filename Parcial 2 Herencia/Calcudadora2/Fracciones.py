from fractions import Fraction
class Fra():
    def oper(self):
        print("-------")
        print("Fracciones ejemplo: 3/4")
        print("-------")
        self.__x=Fraction(input("Escribe aqui el 1er digito >"))
        self.__y=Fraction(input("Escribe aqui el 2do digito >"))
        print("-------")
        print("MENU FRACCIONES")
        print("1.Suma")
        print("2.Resta")
        print("3.Division")
        print("4.Multiplicacion")
        print("-------")
        f = int(input(">"))
        if f == 1:
            print (str(self.__x + self.__y))
        elif f == 2:
            print (str(self.__x - self.__y))
        elif f == 3:
            print(str(self.__x / self.__y))
        elif f == 4:
            print (str(self.__x * self.__y))
        else:
            print("**Error**")