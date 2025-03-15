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
