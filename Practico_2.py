print("Programa que determina si un numero es par o impar\n")
numero = int(input("Introduzca un numero entero: "))
resto = numero % 2
if resto == 0:
    print("El numero", numero, "es par.")
else:
    print("El numero", numero, "es impar.")
