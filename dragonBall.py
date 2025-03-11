import random


class Fighter:
    def __init__(self, name: str, speed: int, attack: int, defense: int) -> None:
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.health = 100

    def reset_health(self):
        self.health = 100

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int):
        attack_damage = 0
        if random.random() < 0.2:
            print(f"{self.name} ha esquivado el ataque")
        else:
            if self.defense >= damage:
                # Redondeamos a entero, asegurando un mínimo de 1 de daño
                attack_damage = max(1, int(damage * 0.1))
            else:
                # Redondeamos a entero
                attack_damage = int(damage - self.defense)
                # Aseguramos que el daño sea al menos 1
                attack_damage = max(1, attack_damage)

        self.health = max(self.health - attack_damage, 0)
        print(f"{self.name} ha recibido {attack_damage} de daño")
        print(f"{self.name} tiene {self.health} de vida")


class Battle:

    def __init__(self, fighter1: Fighter, fighter2: Fighter):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def fight(self) -> Fighter:
        print(f"\n=== {self.fighter1.name} vs. {self.fighter2.name} ===")
        while self.fighter1.is_alive() and self.fighter2.is_alive():
            if self.fighter1.speed >= self.fighter2.speed:
                self.turn(self.fighter1, self.fighter2)
                if self.fighter2.is_alive():
                    self.turn(self.fighter2, self.fighter1)
            else:
                self.turn(self.fighter2, self.fighter1)
                if self.fighter1.is_alive():
                    self.turn(self.fighter1, self.fighter2)
        if self.fighter1.is_alive():
            print(f"{self.fighter1.name} es el ganador de la batalla")
            return self.fighter1
        else:
            print(f"{self.fighter2.name} es el ganador de la batalla")
            return self.fighter2

    def turn(self, attacker: Fighter, defender: Fighter):
        print(f"\n{attacker.name} ataca a {defender.name}")
        defender.take_damage(attacker.attack)


class Tournament:

    def __init__(self, fighters: list):
        if not self.is_power_of_two(len(fighters)):
            raise ValueError("El numero de luchadores debe ser un numero potencia de 2")
        self.fighters = fighters

    def start(self):
        round = 1
        while len(self.fighters) > 1:
            print(f"\n=== Ronda {round} ===")
            random.shuffle(self.fighters)
            winners = []
            for index in range(0, len(self.fighters), 2):
                fighter1 = self.fighters[index]
                fighter2 = self.fighters[index + 1]
                battle = Battle(fighter1, fighter2)
                winner = battle.fight()
                winners.append(winner)

            self.fighters = winners
            round += 1

        print(f"\nEl ganador del torneo es {self.fighters[0].name}!!!\n")

    def is_power_of_two(self, n) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1


fighters = [
    Fighter(
        "Goku", 95, 98, 90
    ),  # Goku: Velocidad y ataque sobresalientes, defensa alta
    Fighter(
        "Vegeta", 93, 96, 92
    ),  # Vegeta: Similar a Goku, con una defensa ligeramente superior
    Fighter(
        "Piccolo", 85, 90, 95
    ),  # Piccolo: Defensa muy alta, ataque y velocidad buenos
    Fighter(
        "Freezer", 97, 94, 85
    ),  # Freezer: Velocidad excepcional, ataque alto, defensa buena
    Fighter(
        "Krillin", 88, 87, 88
    ),  # Krillin: Equilibrado en velocidad, ataque y defensa
    Fighter("Célula", 96, 97, 93),  # Célula: Casi perfecto en todas las áreas
    Fighter(
        "Son Gohan", 92, 95, 87
    ),  # Gohan: Potencial enorme, equilibrado con picos en ataque
    Fighter("Trunks", 94, 91, 89),  # Trunks: Velocidad y ataque altos, defensa buena
]

tournament = Tournament(fighters)
tournament.start()
