from queue import PriorityQueue
N = int(input())
tasks = PriorityQueue()

for _ in range(N):
    req = input().split()
    if req[0] == "R":
        print(tasks.get()[1])
    elif req[0] == "N":
        id = int(req[1])
        diff = int(req[2])
        tasks.put((-diff, id))


