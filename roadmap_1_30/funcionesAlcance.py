'''
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
arg_greet(name="Buenos días", greet="Laura")  # Le he cambiado los valores


def arg_greet(name, greet="Nos vemos..."):
    print(f"{greet}, {name}")


arg_greet("Que pasa....", "Miguel")
arg_greet("Carlos")
arg_greet(name="Laura", greet="Adios")
arg_greet(name="Laura")


# con argumento y retorno
def return_args_greet(greet, name):
    return f"{greet}, {name}"


print(return_args_greet("Como estamos", "tio!"))

# con retorno de varios valores


def múltiple_return_greet():
    return "Hola", "Python"


greet, name = múltiple_return_greet()
print(greet)
print(name)
print(greet, name)
print(f"{greet}, {name}")


# con un numero de variables de argumentos


def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")


variable_arg_greet("pájaro", "PC", "arbusto", "Miguel")

# con un numero variables de argumentos con palabra clave


def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola, {value} --->({key})")


variable_key_arg_greet(animal="pájaro", cosa="PC", planta="arbusto", nombre="Miguel")

"""
funciones dentro
de funciones
"""



def outer_function():
    def inner_function():
        print("Función interna: Como esta el elefante?")

    inner_function()


outer_function()


"""
funciones del lenguaje (built-in)
"""
print(len("Miguel"))
print(type("Miguel"))
print("Miguel".upper())


"""
variables locales y globales
"""

global_var = "Python"
print(global_var)


def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")


hello_python()

global_var = "Python"
resultado = None

def hello_python():
    global resultado
    local_var = "Hola"
    resultado = f"{local_var}, {global_var}"

hello_python()
print(resultado)'
'''

"""
extra
"""


def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        if number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    print("\nCantidad de veces que ha mostrado números:")
    return count


print(print_numbers("Fizz", "Buzz"))
