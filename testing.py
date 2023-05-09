from queue import PriorityQueue

queue = PriorityQueue()

queue.put((0,1))
queue.put((100, 2))
queue.put((9, 3))

while queue:
    print(queue.get())