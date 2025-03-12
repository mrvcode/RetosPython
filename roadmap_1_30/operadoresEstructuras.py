# Operadores aritméticos

print(f"suma: 10 + 3 = {10+3}")
print(f"division: 10 / 3 = {10/3}")
print(f"modulo: 10 % 3 = {10%3}")
print(f"exponente: 10 ** 3 = {10**3}")
print(f"division entera: 10 // 3 = {10//3}\n")

# operadores de comparación

print(f"Igualdad: 10 == 3 es {10==3}")
print(f"Igualdad: 10 != 3 es {10!=3}")

"""
Y todos los demás 
mayor que...menor que...etc.

"""

# operadores lógicos

print(
    f"AND && -> verdadero se cumple en los dos lados sino sera falso: {10+3 == 13 and 5-1 ==4}"
)
print(f"OR || -> verdadero aunque en un lado sea falso: {10+14 == 13 or 5-1 ==4}")
print(f"NOT ! -> es lo contrario: {not 10+14 == 13}\n")


# operadores de asignación

my_number = 11
print(my_number)
my_number *= 11
print(my_number)

# operadores de identidad

my_new_number = my_number
print(f"\nmy_new_number is my_new_number es {my_number is my_new_number}")
