import queue

q = queue.Queue()

numbers = list(range(0, 10))
for n in numbers:
    q.put(n)

print(q.get())
print(q.get())

q = queue.PriorityQueue()
q.put((2, "Hello World"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
    print(q.get())