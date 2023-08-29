print("================")
print("Menu De Opciones")
print("================")

print("Presiona 1 para convertir de numero a palabra")
print("Presiona 2 para convertir de palabra a numero")

opcion = int(input("Presiona la opcion que elejiste : "))

if opcion == 1 :
    print("conversor de numero a letra")
    numero = int(input("elija el numero a convertir a letra del 1-5 : "))
    if numero == 1 :
        print("uno")
    elif numero == 2 :
        print("dos")
    elif numero == 3 :
        print("tres")
    elif numero == 4 :
        print("cuatro")
    elif numero == 5 :
        print("cinco")
    else : print("este numero esta fuera del rango")
elif opcion == 2 :
    print("conversor de numero a letra")
    palabra = str(input("escriba un numero literal del uno al cinco : "))
    if palabra == "uno" :
        print(1)
    elif palabra == "dos" :
        print(2)
    elif palabra == "tres" :
        print(3)
    elif palabra == "cuatro" :
        print(4)
    elif palabra == "cinco" :
        print(5)
    else : print("esta palabra esta fuera del rango")
else : print("esta opcion esta fuera del menu")

print('"Gracias por su atencion UwU"')
