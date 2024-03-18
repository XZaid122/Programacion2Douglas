print("Menu:")
print("1. Personas")
print("2. Vehiculos")
print("3. Universidades")
print("4. Notas")
print("5. Salir")

while (True):

    opcion = int(input("Selecciona una opcion (1-5): "))


    if opcion == 1:
        print("Has presionado la opcion Personas.")
    if opcion == 2:
        print("Has presionado la opcion Vehiculos.")
    if opcion == 3:
        print("Has presionado la opcion Universidades.")
    if opcion == 4:
        print("Has presionado la opcion Notas.")
    if opcion == 5:
        print("¡Hasta luego! El programa ha finalizado.")
        break
    if opcion >=6:
        print("Opcion invalida. Por favor, selecciona una opcion valida (1-5).")