import os
import csv
import random


def read_csv_data() -> list:
    file_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = f"{file_dir}/participantes.csv"
    data = []
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] == "activo":
                data.append(row)
    return data


def select_winners(data: list) -> list:
    if len(data) < 3:
        raise ValueError("No hay suficientes datos para seleccionar ganadores.")
    return random.sample(data, 3)


def display_winners(winners):
    prizes = ["Suscripción Anual", "Descuento Especial", "Libro Mas vendido"]
    for winner, prize in zip(winners, prizes):
        print(f"{prize}: {winner["email"]} (ID:{winner["id"]})")


try:
    display_winners(select_winners(read_csv_data()))
except ValueError as e:
    print(f"Error: {e}")
