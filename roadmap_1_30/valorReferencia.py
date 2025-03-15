"""
valor y referencia
"""

#  tipos de dato por valor

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)
print()


# tipos de datos por referencia


my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
# my_list_b = [30, 40]
print(my_list_a)
print(my_list_b)
print()

# funciones con datos por valor


def my_int_func(my_int: int):
    my_int = 90
    print(my_int)


my_int_c = 50
print(my_int_c)
my_int_func(my_int_c)
print()

# funciones por datos por referencia


def my_list_func(my_list: list):
    my_list_e = my_list

    my_list_e.append(30)

    my_list_d = my_list_e
    my_list_d.append(40)

    print(my_list_e)
    print(my_list_d)


my_list_c = [40, 70]
my_list_func(my_list_c)
print(my_list_c)
print()
"""
extra
"""
# por valor


def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_int_d = 72
my_int_e = 43
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")
print()
print()
print()
# referencia


def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    # temp.append(50)
    value_a = value_b
    value_b = temp
    # value_b.append(50)
    # value_a.append(50)
    return value_a, value_b


my_list_h = [10, 20]
my_list_i = [30, 40]
my_list_j, my_list_k = ref(my_list_h, my_list_i)

print(f"{my_list_h}, {my_list_i}")
print(f"{my_list_j}, {my_list_k}")
