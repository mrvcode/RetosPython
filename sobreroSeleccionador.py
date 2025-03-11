import random


houses = {"Frontend": 0, "Backend": 0, "Mobile": 0, "Data": 0}

questions = [
    {
        "question": "¿Qué aspecto del desarrollo te motiva más?",
        "answers": [
            {
                "option": "Implementar la lógica de negocio y la seguridad de las aplicaciones.",
                "house": "Backend",
            },
            {
                "option": "Analizar grandes conjuntos de datos para descubrir patrones y tendencias.",
                "house": "Data",
            },
            {
                "option": "Crear interfaces de usuario intuitivas y atractivas.",
                "house": "Frontend",
            },
            {
                "option": "Optimizar el rendimiento de aplicaciones para dispositivos móviles.",
                "house": "Mobile",
            },
        ],
    },
    {
        "question": "¿Qué tipo de herramientas te gusta usar?",
        "answers": [
            {
                "option": "Frameworks de desarrollo móvil y kits de desarrollo de software (SDKs).",
                "house": "Mobile",
            },
            {
                "option": "Bibliotecas de visualización de datos y herramientas de aprendizaje automático.",
                "house": "Data",
            },
            {
                "option": "Frameworks de JavaScript y bibliotecas de componentes de interfaz de usuario.",
                "house": "Frontend",
            },
            {
                "option": "Frameworks de backend y bases de datos relacionales o NoSQL.",
                "house": "Backend",
            },
        ],
    },
    {
        "question": "¿Cuál es tu enfoque preferido para la resolución de problemas?",
        "answers": [
            {
                "option": "Iterar rápidamente en el diseño de la interfaz de usuario y la experiencia del usuario.",
                "house": "Frontend",
            },
            {
                "option": "Refactorizar el código y optimizar el rendimiento del servidor.",
                "house": "Backend",
            },
            {
                "option": "Probar exhaustivamente en diferentes dispositivos y condiciones de red.",
                "house": "Mobile",
            },
            {
                "option": "Experimentar con diferentes algoritmos y modelos estadísticos.",
                "house": "Data",
            },
        ],
    },
    {
        "question": "¿En qué tipo de proyectos te sientes más realizado?",
        "answers": [
            {
                "option": "Sistemas de análisis de datos que informan decisiones estratégicas.",
                "house": "Data",
            },
            {
                "option": "Aplicaciones web interactivas y dinámicas.",
                "house": "Frontend",
            },
            {"option": "Servicios backend escalables y seguros.", "house": "Backend"},
            {
                "option": "Aplicaciones móviles que resuelven problemas del mundo real.",
                "house": "Mobile",
            },
        ],
    },
    {
        "question": "¿Qué tecnologías te resultan más interesantes?",
        "answers": [
            {"option": "Lenguajes de programación como Python o R.", "house": "Data"},
            {
                "option": "Lenguajes de programación como Java o Node.js.",
                "house": "Backend",
            },
            {
                "option": "Lenguajes de programación como Swift o Kotlin.",
                "house": "Mobile",
            },
            {
                "option": "Lenguajes de programación como HTML, CSS y JavaScript.",
                "house": "Frontend",
            },
        ],
    },
    {
        "question": "¿Qué tipo de desafíos te atraen más?",
        "answers": [
            {
                "option": "Desafíos relacionados con la adaptación a diferentes tamaños de pantalla y sistemas operativos.",
                "house": "Mobile",
            },
            {
                "option": "Desafíos relacionados con la creación de experiencias de usuario fluidas y atractivas.",
                "house": "Frontend",
            },
            {
                "option": "Desafíos relacionados con la seguridad y la escalabilidad de las aplicaciones.",
                "house": "Backend",
            },
            {
                "option": "Desafíos relacionados con la optimización de algoritmos y el manejo de grandes volúmenes de datos.",
                "house": "Data",
            },
        ],
    },
    {
        "question": "¿Cómo prefieres colaborar con otros desarrolladores?",
        "answers": [
            {
                "option": "Contribuyendo a la creación de modelos de datos y algoritmos de análisis.",
                "house": "Data",
            },
            {
                "option": "Participando en sesiones de diseño de interfaces de usuario y pruebas de usabilidad.",
                "house": "Frontend",
            },
            {
                "option": "Colaborando en la construcción de aplicaciones móviles multiplataforma.",
                "house": "Mobile",
            },
            {
                "option": "Trabajando en la implementación de APIs y servicios web.",
                "house": "Backend",
            },
        ],
    },
    {
        "question": "¿Qué tipo de aprendizaje te resulta más efectivo?",
        "answers": [
            {
                "option": "A través de la visualización de datos y la exploración de conjuntos de datos.",
                "house": "Data",
            },
            {
                "option": "A través de la lectura de documentación técnica y la participación en comunidades en línea.",
                "house": "Backend",
            },
            {
                "option": "A través de la experimentación práctica y la construcción de prototipos.",
                "house": "Mobile",
            },
            {
                "option": "A través del análisis de ejemplos de código y la resolución de problemas de programación.",
                "house": "Frontend",
            },
        ],
    },
    {
        "question": "¿Qué aspecto del ciclo de vida del desarrollo te gusta más?",
        "answers": [
            {
                "option": "La recopilación, limpieza y análisis de datos.",
                "house": "Data",
            },
            {
                "option": "El diseño de la arquitectura de la aplicación y la implementación de la lógica de negocio.",
                "house": "Backend",
            },
            {
                "option": "La prueba y el despliegue de la aplicación en dispositivos móviles.",
                "house": "Mobile",
            },
            {
                "option": "La creación de la interfaz de usuario y la experiencia del usuario.",
                "house": "Frontend",
            },
        ],
    },
    {
        "question": "¿Qué tipo de impacto te gustaría tener con tu trabajo?",
        "answers": [
            {
                "option": "Construir aplicaciones web que sean accesibles y fáciles de usar.",
                "house": "Frontend",
            },
            {
                "option": "Ayudar a las empresas a tomar decisiones basadas en datos.",
                "house": "Data",
            },
            {
                "option": "Desarrollar servicios backend que sean confiables y eficientes.",
                "house": "Backend",
            },
            {
                "option": "Crear aplicaciones móviles que mejoren la vida de las personas.",
                "house": "Mobile",
            },
        ],
    },
]

print("Bienvenido al seleccionador de sobrero de programación.")
print("Responde las siguientes preguntas y descubre a que casa perteneces")

name = input("Cual es tu nombre?: ")

for index, question in enumerate(questions):
    print(f"Pregunta {index + 1}: {question['question']}")
    for i, answer in enumerate(question["answers"]):
        print(f"{i + 1}. {answer['option']}")
    while True:
        try:
            choice = int(input("Selecciona una respuesta entre 1 y 4: "))
            if 1 <= choice <= 4:
                break
            else:
                print("Por favor, ingresa un número entre 1 y 4.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
    selected_answer = question["answers"][choice - 1]
    houses[selected_answer["house"]] += 1

assingned_house = max(houses, key=houses.get)
scores = list(houses.values())

if scores.count(max(scores)) > 1:
    possible_houses = [house for house, score in houses.items() if score == max(scores)]
    assingned_house = random.choice(possible_houses)
    print(
        f"""Hmmmmm... Ha sido mu complicado la decision, pero {name} perteneces a la casa {assingned_house}"""
    )
else:
    print(f"""{name} perteneces a la casa {assingned_house}""")
