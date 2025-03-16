"""
# pila/stack (LIFO)

stack = []
# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
# pop
# mecanismo manual
stack_items = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_items)
print(stack)
# mecanismo propio del lenguaje
print(stack.pop())

print(stack)
print()
# cola/queue(FIFO)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
# dequeue
# mecanismo manual
dequeue_items = queue[0]
del queue[0]

print(dequeue_items)
print(queue)
# mecanismo propio del lenguaje
print(queue.pop(0))
print(queue)
"""

"""
extra
"""

# web


def web_navigation():

    stack = []

    while True:

        action = input("Añade una url o interactúa con palabras adelante/atrás/salir: ")

        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            pass  # con el elemento stack puro no se puede realizar
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}")
        else:
            print("Estas en la pagina de inicio.")


# web_navigation()


def share_printed():

    queue = []

    while True:

        action = input("Añade un documento o selecciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)

        if len(queue) == 0:
            print("La cola de impresión esta vacía.")
        else:
            print(f"Cola de impresión: {queue}")


share_printed()
