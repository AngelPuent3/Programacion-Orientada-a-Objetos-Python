from ATM import Cuenta
from ATM import a
def main():
   print("MENU\n"
      "1.- Consultar saldo\n"
      "2.- Retirar\n"
      "3.- Depositar")
   x=int(input(">"))
   if x==1:
      a.consultaSaldo()
      print ("Desea hacer algo mas?\n"
             "1.- Si\n"
             "2.- No")
      y=int(input(">"))
      if y == 1:
         main()
      else:
          exit("Adios :)")
   elif x==2:
       a.retirar()
       print("Desea hacer algo mas?\n"
             "1.- Si\n"
             "2.- No")
       y = int(input(">"))
       if y == 1:
           main()
       else:
           exit("Adios :)")
   elif x==3:
       a.depositar()
       print("Desea hacer algo mas?\n"
             "1.- Si\n"
             "2.- No")
       y = int(input(">"))
       if y == 1:
           main()
       else:
           exit("Adios :)")
   else:
       print("**Error**")

main()


