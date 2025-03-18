# Superclase


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
extra
"""


class Employee:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} esta coordinado todos los proyectos de la empresa.")

class ProjectManager(Employee):
    
class Programmer(Employee):