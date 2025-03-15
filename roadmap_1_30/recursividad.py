# función recursiva


def countdown(number: int):
    if number >= 0:
        print(number, end=" ")
        countdown(number - 1)


countdown(10)
print()
print()


"""
extra
"""


def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son validos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(3))
print()

"""
extra
"""


def fibonacci(number: int) -> int:
    if number <= 0:
        print("La posición debe ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(18))  # aki se coloca la posición en la sucesión de fibonacci
