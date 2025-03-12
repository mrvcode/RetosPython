



def show_menu()
    print("\nPlanificación de objetivos:")
    print("1.Añadir objetivo")
    print("2.Calcular el plan detalla do")
    print("3.Guardar la planificación")
    print("4.Salir")


class Goal:

    def __init__(self, goal_name: str, amount: int, units: str, limit: int):
        self.goal_name = goal_name
        self.amount = amount
        self.units = units
        self.limit = limit


def add_goal():

    goal_name = input("Meta: ")
    amount = input("Cantidad: ")
    unit = input("Unidades: ")
    limit = input("Plazos en meses (máximo 12): ")




while True:

    show_menu()

    option = input("Elige una opción: ")

    if option == "1":
        add_goal()
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
        print("Saliendo del planificador....")
        break
    else:
        print("Opción invalida. Elige una opción entre 1 y 4")