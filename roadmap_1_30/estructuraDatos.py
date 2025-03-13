"""
# lista
my_list: list = ["coki", "ma", "co", "pli"]
print(my_list)
my_list.append("tor")
my_list.append("tor")
print(my_list)
my_list.remove("tor")
print(my_list)
print(my_list[1])
my_list[1] = "muuuuu"
print(my_list)
my_list.sort()
print(my_list)
print(type(my_list))

# tuplas

my_tuple: tuple = ("Miguel", "Rubio", "644")
print(my_tuple[2])
my_tuple = sorted(my_tuple)  # aquí pasa a ser una lista
print(type(my_tuple))
my_tuple = tuple(sorted(my_tuple))  # aquí pasa a ser un tuple de nuevo
print(my_tuple)
print(type(my_tuple))


# set (no es ordenado y no se puede ordenar)
my_set = {"Paris", "francés", "1500000"}
print(my_set)
my_set.add("Francia")
my_set.add("Francia")  # no lo vuelve a añadir
my_set.remove("francés")
print(my_set)
my_set = sorted(my_set)
print(type(my_set))


my_dict: dict = {"Ciudad": "Paris", "idioma": "francés", "habitantes": "1500000"}
my_dict["web"] = "https://paris.fr"
print(my_dict)
del my_dict["web"]
print(my_dict)
print(my_dict["Ciudad"])
my_dict = dict(sorted(my_dict.items()))  # ordenación por key
print(my_dict)
print(type(my_dict))
"""

"""
extra
"""


def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el numero de teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "Debes de introducir un número de teléfono con un máximo de 12 dígitos"
            )

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción de la agenda: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(
                        f"El número de teléfono del contacto {name} es {agenda[name]}."
                    )
                else:
                    print(f"El contacto {name} no esta en la agenda")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
                print(f"el contacto {name} se ha añadido correctamente")

            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                    print(f"el contacto {name} se actualizado correctamente")
                else:
                    print(f"El contacto {name} no esta en la agenda")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    print(f"el contacto {name} se ha eliminado.")
                    del agenda[name]
                else:
                    print(f"El contacto {name} no esta en la agenda")
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción invalida. Elige del 1 al 5.")


my_agenda()
