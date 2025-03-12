import os

MONTH = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]


def show_menu():
    print("\nPlanificación de objetivos:")
    print("1.Añadir objetivo")
    print("2.Calcular el plan detallado")
    print("3.Guardar la planificación")
    print("4.Salir")


class Goal:

    def __init__(self, goal_name: str, amount: int, units: str, limit: int):
        self.goal_name = goal_name
        self.amount = amount
        self.units = units
        self.limit = limit


def request_goal() -> Goal:

    goal_name = input("Meta: ")

    while True:
        try:
            amount = int(input("Cantidad: "))
            if amount <= 0:
                print("La cantidad debe de ser un número positivo.")
                continue
            break
        except:
            print("Por favor introduce un número entero valido.")

    units = input("Unidades: ")

    while True:
        try:
            limit = int(input("Plazos en meses (máximo 12): "))
            if limit <= 0 or limit > len(MONTH):
                print("Por favor introduce un número entre 1 y 12 meses.")
                continue
            break
        except:
            print("Por favor introduce un número entre 1 y 12 meses.")

    return Goal(goal_name, amount, units, limit)


def calculate_detail_plan(goals: list[Goal]) -> dict:

    plan = {month: [] for month in range(1, len(MONTH) + 1)}

    for goal in goals:

        month_amount = goal.amount / goal.limit

        for month in range(1, goal.limit + 1):

            plan[month].append(
                Goal(goal.goal_name, month_amount, goal.units, goal.amount)
            )
    return plan


def show_detailed_plan(plan: dict):

    for month in range(1, len(MONTH) + 1):

        if not plan[month]:
            # No hay objetivos en este mes
            break

        print(f"{MONTH[month - 1]}: ")

        for index, goal in enumerate(plan[month], start=1):
            print(
                f"[ ] {index}. {goal.goal_name} ({goal.amount} {goal.units}/mes). Total: {goal.limit}."
            )


def save_detail_plan(plan: dict):

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plant.txt")

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("Plan detallado")

        for month in range(1, len(MONTH) + 1):

            if not plan[month]:
                # No hay objetivos en este mes
                break

            file.write(f"{MONTH[month - 1]}:\n")

            for index, goal in enumerate(plan[month], start=1):
                file.write(
                    f"[ ] {index}. {goal.goal_name} ({goal.amount} {goal.units}/mes). Total: {goal.limit}.\n"
                )
    print(f"Plan guardado con éxito en {file_path}")


goals = []

while True:

    show_menu()

    option = input("Elige una opción: ")

    if option == "1":
        if len(goals) > 10:
            print("Has alcanzado el máximo numero de objetivos")
        else:
            goal = request_goal()
            goals.append(goal)
            print("Objetivo añadido.")

    elif option == "2":
        if len(goals) == 0:
            print("No hay objetivos añadidos.")
        else:
            plan = calculate_detail_plan(goals)
            show_detailed_plan(plan)

    elif option == "3":
        if len(goals) == 0:
            print("No hay objetivos para guardar.")
        else:
            plan = calculate_detail_plan(goals)
            save_detail_plan(plan)

    elif option == "4":
        print("Saliendo del planificador....")
        break
    else:
        print("Opción invalida. Elige una opción entre 1 y 4")
