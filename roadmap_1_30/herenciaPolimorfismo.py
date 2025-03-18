# Superclase
"""

class Animal:

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass


def print_sound(animal: Animal):
    animal.sound()


# Subclases


class Dog(Animal):
    def sound(self):
        print("Guau!")


class Cat(Animal):
    def sound(self):
        print("Miu!")


my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog("Boby")
print_sound(my_dog)
my_cat = Cat("Bolita")
print_sound(my_cat)
"""

"""
extra
"""


class Employee:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)


class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} esta coordinado todos los proyectos de la empresa.")


class ProjectManager(Employee):

    def coordinate_project(self):
        print(f"{self.name} esta coordinado su proyecto.")


class Programmer(Employee):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} esta programando en {self.language}")

    def add(self, employee):
        print(
            f"Un programador no tiene empleados a su cargo. {employee} no se añadirá."
        )
