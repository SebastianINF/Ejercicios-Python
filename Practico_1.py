print('"VACIONES PARA LOS EMPLEADOS"\n')

nombre = str(input("Introduzca su nombre al sistema: "))
clave = int(input("Introduzca su clave de departamento (entre 1 - 3) : "))
años = int(input("introduca los años que lleva trabajando: "))
if clave == 1:
    print("Departamento de Atencion al Cliente.(Clave 1)\n")
    if años >= 1 and años < 2:
        print("Usted", nombre, ", tiene derecho a 6 dias de vacaciones.\n")
    elif años >= 2 and años < 7:
        print("Usted", nombre, ", tiene derecho a 14 dias de vacaciones.\n")
    elif años >= 7:
        print("Usted", nombre, ", tiene derecho a 20 dias de vacaciones.\n")
    else:
        print(nombre, ", sin derecho a vaciones.\n")
elif clave == 2:
    print("Departamento de Logística(Clave 2)\n")
    if años >= 1 and años < 2:
        print("Usted", nombre, ", tiene derecho a 7 dias de vacaciones.\n")
    elif años >= 2 and años < 7:
        print("Usted", nombre, ", tiene derecho a 15 dias de vacaciones.\n")
    elif años >= 7:
        print("Usted", nombre, ", tiene derecho a 22 dias de vacaciones.\n")
    else:
        print(nombre, ", sin derecho a vaciones.\n")
elif clave == 3:
    print("Gerencia(Clave 3)\n")
    if años >= 1 and años < 2:
        print("Usted", nombre, ", tiene derecho a 10 dias de vacaciones.\n")
    elif años >= 2 and años < 7:
        print("Usted", nombre, ", tiene derecho a 20 dias de vacaciones.\n")
    elif años >= 7:
        print("Usted", nombre, ", tiene derecho a 30 dias de vacaciones.\n")
    else:
        print(nombre, ", sin derecho a vacaciones.\n")
else:
    print("La clave no existe.\n")
print("Fin del programa.")
