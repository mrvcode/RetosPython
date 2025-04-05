import os

"""
Ejercicio
"""

# file_name = "Miguel.txt"

# with open(file_name, "w") as file:
#     file.write("Miguel Rubio\n")
#     file.write("46\n")
#     file.write("Python")

# with open(file_name, "r") as file:
#     print(file.read())

# os.remove(file_name)


"""
Extra
"""
file_name = "Miguel.txt"

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Borrar fichero del sistema")
    print("9. Salir")

    option = input("Selecciona un opción: ")

    # ***OPCION 1****

    if option == "1":

        name = input("Nombre del producto: ")
        quantity = input("Cantidad de productos: ")
        price = input("Precio del producto: ")

        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")

    # ***OPCION 2****

    elif option == "2":
        name = input("Nombre del producto a consultar: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break

    # ***OPCION 3****

    elif option == "3":
        name = input("Nombre del producto a actualizar: ")
        quantity = input("Cantidad de productos: ")
        price = input("Precio del producto: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)

    # ***OPCION 4****

    elif option == "4":

        name = input("Nombre del producto a borrar: ")

        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)

    # ***OPCION 5****

    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())

    # ***OPCION 6****

    elif option == "6":  # Calcular venta total

        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price

        print(total)

    # ***OPCION 7****

    elif option == "7":  # Calcular venta por producto

        name = input("Nombre del producto a calcular: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break

        print(total)

    # ***OPCION 8****

    elif option == "8":
        break

    # ***OPCION 9****

    elif option == "9":
        os.remove(file_name)
        break

    else:
        print("Selecciona una opción disponibles")
