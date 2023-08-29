print('"OPERADORES LOGICOS"\n')
num_uno = float(input("Inserte un numero: \n"))
num_dos = float(input("Inserte otro numero: \n"))
if num_uno > 6 and num_dos > 8 :
    print("Ambas condiciones se han cumplido")
elif num_uno == 3 or num_dos == 9 :
    print("Una de las dos condiciones se han cumplido")
elif num_uno != 1 and num_dos != 0:
    print("Las dos condiciones se han cumplido")
elif not num_uno == 4 :
    print("la condicion se ha cumplido")
else :
    print("Una o ninguna condicion se ha cumplido")