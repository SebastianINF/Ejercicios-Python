longitud = int(input("¿Cuántos números enteros contendra la lista?: "))
lista = []
for contador in range(1,longitud + 1) :
    elementoN = int(input("Introduce un número entero: "))
    lista.append(elementoN)
print(f"\nLista: {lista}")
print(f"La suma total de los elemntos es: {sum(lista)}")



