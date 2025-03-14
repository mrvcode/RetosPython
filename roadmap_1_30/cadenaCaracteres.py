"""
cadena de caracteres
"""

s1 = "hola"
s2 = "mundo"
s3 = s1 + " " + s2
print(s3 * 3)
print(f"{s3}, " * 3)
print(f"\n{s3}" * 3)
print()

# Indexación
print(s1[3] + s1[2] + s1[3] + ".....\n")

# longitud
print(len(s2))
print()

# slicing (porción)
print(s2[2:4])
print(s2[:3] + "...")
print("..." + s2[3:])
print()

# búsqueda
print("a" in s1)
print("i" in s1)
print()

# remplazo

s2 = s2.replace("u", "a")
print(s2)
print(s2.replace("a", "i"))
print(s2)
s2 = s2.replace("a", "u")
print(s2)
print()

# división

print(s2.split("n"))  # corta y desecha el carácter que no quieres
print(s3.split(" "))  # corta los espacios en blanco
print(s2.rsplit(None, 1))
print()

# mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper() + " " + s2.upper())
print(s1.title() + " " + s2.title())
print(s3.capitalize())
print()

# Eliminación de espacios al principio a al final
s3 = "      " + s1 + " " + s2 + "           "
print(s3)
s3 = s3.strip()
print(s3)
print()

# búsqueda al principio y al final

print(s3.startswith("Ho"))  # tiene que coincidir exactamente
print(s3.startswith("ho") and s3.endswith("la"))  # las dos tienen que ser verdadera
print(s3.startswith("ho") or s3.endswith("la"))  # al menos una verdadera
print(s3.startswith("ho") and s3.endswith("do"))  # las dos son verdaderas
print()

# búsqueda por posición

print("hola mundo".find("mundo"))
print("hola mundo".upper().find("L"))
print(s3.find("hola"))
print(s3.find("Python"))
print()

# búsqueda de ocurrencias

print("hola mundo".upper().count("O"))
print("hola mundo".upper().count("mundo"))
print("hola mundo".upper().count("MUNDO"))
print()

# formateo

print(f"Saludo: {s1}, lugar: {s2}")
print("Saludo: {}, lugar: {}".format(s1, s2))
print()

# transformación en lista de caracteres

s4 = s3[::-1]  # Invierte la cadena usando slicing con paso negativo
print(list(s4))
s3 = s4[::-1]  # Invierte la cadena usando slicing con paso negativo
print(list(s3))
print(s3)
print()

# transformación de lista en cadena

l1 = [s1, " ", s2]  # esto es una lista de tres objetos
print(l1)
print("".join(l1))
print()
# transformaciones numéricas

s4 = "123456"
print(type(s4))
s4 = int(s4)
print(type(s4))

s5 = "123456.222"
s5 = float(s5)
print(type(s5))
print()

# comprobaciones varias

s5 = "123456.222"
print(s1.isalnum())
print(s1.isalpha())
print(s5.isalpha())  # no todos los caracteres son letras
print(s5.isnumeric())  # el punto no se considera numérico
print(s5.isalnum())  # el punto no se considera numérico ni letra
print()

"""
extra
"""


def check(word1: str, word2: str):

    # palíndromo

    print(f"{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # anagramas

    print(f"{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # isogramas

    def isogram(word: str) -> bool:

        word_dict = dict()

        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"{word1} es un isograma?: {isogram(word1)}")
    print(f"{word2} es un isograma?: {isogram(word2)}")


# check("radar", "python")
# check("amor", "roma")
check("radar", "pythonpythonpythonpython")
