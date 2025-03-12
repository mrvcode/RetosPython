import random
import time

deadpool_health = int(input("Introduce la vida de Deadpool: "))
wolverine_health = int(input("Introduce la vida de Wolverine: "))

turn = 0
regenerate = False

while deadpool_health > 0 and wolverine_health > 0:

    turn += 1
    print(f"\nTurno {turn}")

    # Deadpool ataca a Wolverine
    if regenerate:
        print("Deadpool se esta regenerando y no ataca.")
        regenerate = False
    elif random.random() > 0.2:

        deadpool_damage = random.randint(10, 100)
        print(f"Deadpool ataca a Wolverine con {deadpool_damage} de daño.")

        if deadpool_damage == 100:
            regenerate = True
            print("Golpe crítico Deadpool! Wolverine no atacara en el siguiente turno")

        wolverine_health -= deadpool_damage

        if wolverine_health <= 0:
            print(f"La vida de Wolverine ha llegado a cero.")
            break
        else:
            print(f"Vida restante de Wolverine: {wolverine_health}")

    else:
        print("Wolverine esquiva el ataque de Deadpool!")

    # Wolverine ataca a Deadpool

    if regenerate:
        print("Wolverine se esta regenerando y no ataca.")
        regenerate = False

    elif random.random() > 0.25:

        wolverine_damage = random.randint(10, 120)
        print(f"Wolverine ataca a Deadpool con {wolverine_damage} de daño.")

        if wolverine_damage == 120:
            regenerate = True
            print(
                "Golpe crítico de Wolverine! Deadpool no atacara en el siguiente turno")

        deadpool_health -= wolverine_damage

        if deadpool_health <= 0:
            print(f"La vida de Deadpool ha llegado a cero.")
            break
        else:
            print(f"Vida restante de Deadpool: {deadpool_health}")

    else:
        print("Deadpool esquiva el ataque de Wolverine!")

    time.sleep(1)

if deadpool_health > 0:
    print("\nDeadpool ha ganado la batalla")
else:
    print("\nWolverine ha ganado la batalla")
