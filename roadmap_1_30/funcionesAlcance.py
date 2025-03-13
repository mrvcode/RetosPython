"""
funciones definidas por el usuario
"""

# simple


def greet():
    print("Hola, python")


greet()


# con retorno


def return_greet() -> str:
    return "Hola, python de nuevo"


return_greet()  # aki no sacaría nada
print(return_greet())  # esta pasando por aki

# con argumento


def arg_greet(name):
    print(f"Hola, {name}")


arg_greet("Miguel")
arg_greet("Carlos")
arg_greet("Laura")


def arg_greet(greet, name):
    print(f"{greet}, {name}")


arg_greet("Que pasa....", "Miguel")
arg_greet("Adios", "Carlos")
arg_greet("Buenos días", "Laura")


def arg_greet(name, greet="Nos vemos..."):
    print(f"{greet}, {name}")


arg_greet("Que pasa....", "Miguel")
arg_greet("Carlos")
arg_greet("Laura")
