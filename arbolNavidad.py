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

    def display_tree(self):
        for i, row in enumerate(self.tree):
            print("".join(row))
        for row in self.trunk:
            print("".join(row))

    def add_start(self):
        pass

    def remove_star(self):
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
                pass
            case "4":
                pass
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
