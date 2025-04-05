import os

"""
Ejercicio
"""

file_name = "Miguel.txt"

with open(file_name, "w") as file:
    file.write("Miguel Rubio\n")
    file.write("46\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)


"""
Extra
"""

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Calcular venta total")
    print("6. Calcular venta por producto")
    print("7. Salir")

    option = input("Selecciona un opción")

    if option == "1":
        pass

    elif option == "2":
        pass

    elif option == "3":
        pass

    elif option == "4":
        pass

    elif option == "5":  # Calcular venta total
        pass

    elif option == "6":  # Calcular venta por producto
        pass

    elif option == "7":
        break

    else:
        print("Selecciona una opción disponibles")
