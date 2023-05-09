from queue import PriorityQueue
import math

N,M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
lengths = [None for _ in range(N + 1)]

queue = PriorityQueue()
queue.put((0,1))

for _ in range(M):
    u,v,w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

while queue.empty() is not True:
    d, vertex = queue.get()
    if lengths[vertex] is None:
        lengths[vertex] = d
        for v,w in adj[vertex]:
            queue.put((d + w, v))

print(*lengths[1:]) # use this for exercise 1