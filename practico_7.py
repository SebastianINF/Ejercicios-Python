#invertir una cadena forma uno:
palabra = input("Introduzca una palabra: ")
indice = len(palabra)
p = indice - 1
for x in palabra :
    x =  palabra[p:indice] 
    print(x, end="")
    indice = indice - 1
    p = p - 1
print("\nFin del programa.")


#inverir una cadena forma dos:
frase = input("Introduzca una palabra: ")
print(f"Cadena invertida: {frase[::-1]} ")


#invertir una cadena forma tres
string = input("Introduzca un string para invertirlo: ")
string_reversed = ""
for character in string :
    string_reversed = character + string_reversed
print(f"string invertido: {string_reversed}")