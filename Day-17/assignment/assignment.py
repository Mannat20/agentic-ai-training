queue = []

queue.append("A")
queue.append("B")
queue.append("C")

print(queue)
# ['A', 'B', 'C']

item = queue.pop(0)
print(item)
# A

print(queue)
# ['B', 'C']

print(queue[0])
# B

print(queue[-1])
# C

if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")

print(len(queue))