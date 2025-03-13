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
print(f"my_new_number is my_new_number es {my_number is not my_new_number}\n")

# operadores de pertenencia

print(
    f"'x' in 'Miguel' = {'x' in 'Miguel'}"
)  # en este caso mira si x esta dentro de Miguel
print(
    f"'x' in 'Miguel' = {'x' not in 'Miguel'}"
)  # Es igual que el anterior. Mira si x esta dentro de Miguel
print(
    f"'x' in 'Miguel' = {'x' is not 'Miguel'}\n"
)  # Este caso es diferente ya que comparar la identidad si x es igual a Miguel

"""
Estructuras de
Control
"""

# condicionales

my_string = "MoureDev"
if my_string == "MoureDev":
    print("my_string es 'MoureDev'")
else:
    print("my_string no es 'MoureDev'")


my_string = "MoureDev"
if my_string == "MoureDeveeeee":
    print("my_string es 'MoureDev'")
else:
    print("my_string no es 'MoureDev'")


my_string = "Brais"
if my_string == "MoureDeveeeee":
    print("my_string es 'MoureDev'")
elif my_string == "Brais":
    print("my_string es 'Brais'")
else:
    print("my_string no es 'MoureDev'")

print("\n")
# iterativas
for i in range(11):
    print(i, end=" ")
print("\n")

i = 0

while i <= 10:
    print(i, end=" ")
    i += 1
print("\n")

# manejo de excepciones

try:
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones\n")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number, end=" ")
