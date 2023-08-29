print("Programa para determinar el numero mas grande de los tres")
num_one = int(input("Introduzca el primer numero: "))
num_two = int(input("Introduzca el segundo numero: "))
num_three = int(input("Introduzca el tercer numero: "))
if num_one > num_two and num_one > num_three:
    print("El numero", num_one, "es mayor")
elif num_two > num_one and num_two > num_three:
    print("El numero", num_two, "es mayor")
elif num_three > num_one and num_three > num_two:
    print("El numero", num_three, "es mayor")
elif num_one == num_two and num_one == num_three:
    print("Los numeros son iguales ")
