print("Calculadora de una sola variable\n")
print("********************")
print("* Menú de opciones *")
print("********************\n")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto\n")

numero = int(input("Introduce la opción deseada: "))
if numero == 1:
    print("Elegiste suma\n")
    numero = float(input("Introduce el primer numero: "))
    numero += float(input("Introduce el segundo numero: "))
    print("\nTu resultado es:", numero)
elif numero == 2:
    print("Elegiste resta\n")
    numero = float(input("Introduce el primer numero: "))
    numero -= float(input("Introduce el segundo numero: "))
    print("\nTu resultado es:", numero)
elif numero == 3:
    print("Elegiste multiplicación\n")
    numero = float(input("Introduce el primer numero: "))
    numero *= float(input("Introduce el segundo numero: "))
    print("\nTu resultado es:", numero)
elif numero == 4:
    print("Elegiste división\n")
    numero = float(input("Introduce el primer numero: "))
    numero /= float(input("Introduce el segundo numero: "))
    print("\nTu resultado es:", numero)
elif numero == 5:
    print("Elegiste división entera\n")
    numero = float(input("Introduce el primer numero: "))
    numero //= float(input("Introduce el segundo numero: "))
    print("\nTu resultado es:", numero)
elif numero == 6:
    print("Elegiste exponente\n")
    numero = float(input("Introduce el primer numero: "))
    numero **= float(input("Introduce el segundo numero: "))
    print("\nTu resultado es:", numero)
elif numero == 7:
    print("Elegiste modulo o resto\n")
    numero = float(input("Introduce el primer numero: "))
    numero %= float(input("Introduce el segundo numero: "))
    print("\nTu resultado es:", numero)
else:
    print("La opcion que elegiste no se encuentra en el menu.\n")
print("\nFinalizado, GRACIAS por ver el programa.")