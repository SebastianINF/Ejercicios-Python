frase = input(f"Introduce una frase: ")
elim = input("Introduce la palabra que deseas elimar: ")
indice = frase.find(elim)
frase = frase[:indice] + frase[len(elim) + indice + 1 :]
print(f"La frase sin la palabra que leminaste es : {frase}")
