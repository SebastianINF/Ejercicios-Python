#Conjuncion
print("Conjuncion(and)")

num_uno = int(input("escribe un numero mayor a 2 y menor a 5: "))
if num_uno > 2 and num_uno < 5 :
    print("El numero", num_uno, " cumple con la condicion.\n")
else :
    print("El numero ",num_uno, " NO cumple con la condicion.\n")
#Disyuncion
print("Disyuncion(or)")
palabra = str(input("Para cumplir la condicion escribe escribe 'si' o 'yes': "))
if palabra == "si" or palabra == "yes" :
    print("La condicion se ha cumplido.\n")
else :
    print("la condicion NO se ha cumplido.\n")
#Negacion
print("Negacion(not)")
num_dos = int(input("Introduce un numero igual a 5 : "))
if not num_dos == 5 :
    print("\n El numero es diferente de cinco y SI cumple la condicion.\n") 
else :
    print("\n El numero es igual a cinco y NO cumple la condicion.\n")