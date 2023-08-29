indice = int(input("¿Qué tabla de multiplicar quieres ver?: "))
print(f"La tabla del {indice} es:")
for multiplicador in range(0, 11):
    print(f"{indice} x {multiplicador} = {indice*multiplicador}")
