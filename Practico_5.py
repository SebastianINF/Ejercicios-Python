#Sucesión de fibonacci hasta el numero 1597
num_uno, num_dos = 0, 1
while num_dos <= 1597 :
    print(num_uno, num_dos, end = " ")
    num_uno += num_dos
    num_dos += num_uno
print("\n Fin ")