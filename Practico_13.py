rows = int(input("¿Cuántas filas tendrá la matriz?: "))
columns = int(input("¿Cuántas columnas tendrá la matriz?: "))
matrix = []
for row_posotion in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Introduce un elemento a la fila: {row_posotion}: ")))
    matrix.append(row)
for row in matrix:
    print(row)

