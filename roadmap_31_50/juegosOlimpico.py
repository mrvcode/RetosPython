import random


class Participant:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country
        return False

    def __hash__(self) -> int:
        return hash(self.name, self.country)


class Olimpics:

    def __init__(self):
        self.events = []
        self.participants = {}
        self.event_results = {}
        self.country_results = {}

    def register_event(self):
        pass

        event = input("Ingrese el nombre del evento: ").strip()

        if event in self.events:
            print(f"El evento {event} ya se encuentra registrado.")
        else:
            self.events.append(event)
            print(f"El evento {event} registrado correctamente.")

    def register_participant(self):

        if not self.events:
            print("No hay eventos registrados. Por favor registrar un evento primero.")
            return

        name = input("Introduce el nombre del participante: ").strip()
        country = input("Introduce el país del participante: ").strip()
        participant = Participant(name, country)

        print("Eventos deportivos disponibles:")
        for index, event in enumerate(self.events):
            print(f"{index + 1}. {event}")

        event_choice = int(input(
            "Selecciona el numero del evento para asignar al participante: "))-1

        if event_choice >= 0 and event_choice < len(self.events):

            event = self.events[event_choice]

            if event in self.participants and participant in self.participants[event]:
                print(
                    f"El participante {name} de {country} ya ha sido registrado en el evento {event}.")

            else:

                if event not in self.participants:
                    self.participants[event] = []

                self.participants[event].append(participant)
                print(
                    f"El participante {name} de {country} ha sido registrado en el evento {event}.")

        else:
            print(
                "Selección de evento deportivo invalida. El participante no ha sido registrado.")

    def simulate_events(self):

        if not self.events:
            print("No hay eventos registrados. Por favor registrar un evento primero.")
            return
        for event in self.events:

            if len(self.participants[event]) < 3:
                print(
                    f"No hay participantes suficientes para simular el evento {event} (mínimo 3)")
                continue

            event_participants = random.sample(self.participants[event], 3)
            random.shuffle(event_participants)

            gold, silver, bronze = event_participants
            self.event_results[event] = [gold, silver, bronze]

            self.update_country_results(gold.country, "gold")
            self.update_country_results(silver.country, "silver")
            self.update_country_results(bronze.country, "bronze")

            print(f"Resultados simulación del evento: {event}")
            print(f"Oro: {gold.name} ({gold.country})")
            print(f"Plata: {silver.name} ({silver.country})")
            print(f"Bronce: {bronze.name} ({bronze.country})")

    def update_country_results(self, country, medal):

        if country not in self.country_results:
            self.country_results[country] = {
                "gold": 0, "silver": 0, "bronze": 0}

        self.country_results[country][medal] += 1

    def show_report(self):

        print("Informe Juegos Olímpicos: ")

        if self.event_results:

            print("Informe por eventos.")

            for event, winners in self.event_results.items():
                print(f"Evento: {event}")
                print(f"Oro: {winners[0].name} ({winners[0].country})")
                print(f"Plata: {winners[1].name} ({winners[1].country})")
                print(f"Bronce: {winners[2].name} ({winners[2].country})")

        else:
            print("No hay resultados de eventos registrados.")

        if self.country_results:

            print("Informe por país.")

            for country, medals in sorted(self.country_results.items(), key=lambda x: (x[1]["gold"], x[1]["silver"], x[1]["bronze"]), reverse=True):
                print(
                    f"{country}: Oro {medals['gold']}, Plata {medals['silver']}, Bronce {medals['bronze']}")

        else:
            print("No hay medallas por país registradas.")


olimpics = Olimpics()

print("Simulador de juegos olímpicos")

while True:

    print()

    print("1. Registro de eventos")
    print("2. Registro de participantes")
    print("3. Simulación de eventos")
    print("4. Creación de informes")
    print("5. Salir")

    option = input("Seleccione una opción: ")

    match option:
        case "1":
            olimpics.register_event()
        case "2":
            olimpics.register_participant()
        case "3":
            olimpics.simulate_events()
        case "4":
            olimpics.show_report()
        case "5":
            print("Saliendo del simulador...")
            break
        case _:
            print("Opción inválida. Por favor, seleccione una opción válida.")
