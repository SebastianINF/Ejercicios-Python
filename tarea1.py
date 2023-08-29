print("sistema para calcular el promedio de un alumno: ")
nombre = str(input("¿cual es tu nombre? : "))
print("okey", nombre, "voy a calcular tu promedio")
nota1 = float(input("por favor, ingrese su primer nota: "))
nota2 = float(input("por favor, ingrese su segunda nota: "))
nota3 = float(input("por favor, ingrese su tercer nota: "))

suma = nota1 + nota2 + nota3
promedio = suma / 3

if promedio >= 51 :
    print("felicidades", nombre, "aprobaste tu promedio es :", round(promedio, 2))
else :
    print("lo siento reprobaste, tu promedio es :", round(promedio, 2))