from Fracciones import Fra
from Aritmetica import Suma
from Aritmetica import Resta
from Aritmetica import Div
from Aritmetica import Multi
from Aritmetica import Raiz
from Aritmetica import Potencia


def main():
  print( "Calcudadora\n"
       "1. Numeros Reales \n"
       "2. Fracciones ")
  o = int(input(">"))
  while True:
    if o == 1:
       print("NUMEROS REALES ☻\n"
          "Potencia-- 2^4 = 2**4 \n"
          "*Ejemplo para operar 2 potencias 2**4 + 4**2\n"
          "Raices -- 2√4 = -4/2 \n"  
          "Exponencia = 2e100\n"
          "    *Ejemplo para operar 2e10 + 3e100\n")
       print("-------")
       print("*MENU*")
       print("1.Suma")
       print("2.Resta")
       print("3.Division")
       print("4.Multiplicacion")
       print("5.Potencias")
       print("6.Raices")
       print("-------")
       x = int(input(">"))
       while True:
         if x == 1:
            a = Suma()
            a.oper()
         elif x == 2:
            b = Resta()
            b.oper()
         elif x == 3:
            c = Div()
            c.oper()
         elif x == 4:
            d = Multi()
            d.oper()
         elif x == 5:
            q = Potencia()
            q.oper()
         elif x==6:
            r=Raiz()
            r.oper()
         else:
          print("Error")
    elif o == 2:
        e = Fra()
        e.oper()
    else:
      print("**Error*")

main()