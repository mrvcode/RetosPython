import random


class ChristmasTree:

    def __init__(self, height: int):

        self.height = height

        self.tree = [[" " for _ in range(2 * height - 1)] for _ in range(height)]

        for i in range(height):
            for j in range(height - i - 1, height + i):
                self.tree[i][j] = "*"

        self.trunk = [[" " for _ in range(2 * height - 1)] for _ in range(2)]

        for i in range(2):
            for j in range(height - 2, height + 1):
                self.trunk[i][j] = "|"

        self.star = False

    def display_tree(self):
        for index, row in enumerate(self.tree):
            if index == 0 and self.star:
                print("".join(row).replace("*", "@"))
            else:
                print("".join(row))
        for row in self.trunk:
            print("".join(row))

    def add_start(self):
        if self.star:
            print("Ya hay una estrella en el árbol.")
        else:
            self.star = True
            print("Se ha puesto la estrella en el árbol.")

    def remove_star(self):
        if not self.star:
            print("No existe una estrella en el árbol para quitar.")
        else:
            self.star = False
            print("Se ha quitado una estrella del árbol.")

    def add_balls(self):
        available = [
            (i, j)
            for i in range(1, self.height)
            for j in range(self.height - i - 1, self.height + i)
            if self.tree[i][j] == "*"
        ]

        if len(available) < 2:
            print("No hay suficiente espacio para añadir más bolas.")
        else:
            selected = random.sample(available, 2)
            for i, j in selected:
                self.tree[i][j] = "o"
            print("Se han añadido 2 bolas al árbol")

    def remove_balls(self):
        pass


height = input("Introduce la altura del árbol: ")

if height.isdigit() and int(height) > 1:

    tree = ChristmasTree(int(height))

    while True:

        tree.display_tree()

        print("\nAcciones:")
        print("1. Añadir estrella")
        print("2. Quitar estrella")
        print("3. Añadir bolas")
        print("4. Quitar bolas")
        print("5. Añadir luces")
        print("6. Quitar luces")
        print("7. Encender luces")
        print("8. Apagar luces")
        print("9. Salir")

        action = input("Selecciona una acción: ")

        match action:
            case "1":
                tree.add_start()
            case "2":
                tree.remove_star()
            case "3":
                tree.add_balls()
            case "4":
                tree.remove_balls()
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                print("Saliendo del programa...")
                break
            case _:
                print("Acción no valida")

else:
    print(f"Altura' {height}' no valida")
