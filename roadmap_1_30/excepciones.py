"""
Ejercicio
"""

try:
    print(10 / 0)
    print("Hola")

except Exception as e:
    print(f"Se a producido un error: {e}")
print("adios")
print()

try:
    print(10 / 1)
    my_list = [1, 2, 3, 4]
    print(my_list[4])

except Exception as e:
    print(f"Se a producido un error: {e} ({type(e).__name__})")
print()


"""
Extra
"""


class StrTypeError(Exception):  # error personalizado
    pass


def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError
    # elif type(parameters[2]) == str:
    #     raise ZeroDivisionError  # no es el verdadero tipo de error
    elif type(parameters[2]) == str:
        raise StrTypeError("EL tercer elemento NO texto")

    print(parameters[2])
    print(parameters[0] / parameters[1])
    print(parameters[2] + 5)


try:
    # process_params([1, 2, 3, 4]) # no errores
    # process_params([1, 0, 3, 4]) # el segundo elemento es cero
    process_params([1, 2, "Miguel", 4])  # el tercer elemento es un texto
except IndexError as e:
    print("El numero de la lista debe ser mayor que dos.")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido errores")
finally:
    print("El programa se finaliza sin detenerse.")
