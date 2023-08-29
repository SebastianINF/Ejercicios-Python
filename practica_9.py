#Texto sin vocales forma uno: 
vocales = {"a", "e", "i", "o", "u", "A", "E", "I", "O","U"}
texto = input("Ingrese una frase: ")
texto_sin_vocales = "".join(nv for nv in texto if nv not in vocales)
print(f"Tu frase sin vocales es: {texto_sin_vocales}\n")

#Texto sin vocales forma dos:
string = str(input("Introduce una frase: "))
letter = str(input("Introduce una letra en donde se detenga el programa: "))
for character in string :
    if character.lower() == letter.lower() :
        break
    elif character.lower() =="a" :
        continue
    elif character.lower() =="e" :
        continue
    elif character.lower() =="i" :
        continue
    elif character.lower() =="o" :
        continue
    elif character.lower() =="u" :
        continue
    print(character, end="")