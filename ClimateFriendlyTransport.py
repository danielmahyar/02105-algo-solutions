# Author: Daniel Cargar Mahyar
# Date: 04-05-2023
# Strategy: Dijkstra's Algorithm to find shortest path from start to end. If the 
# shortest path is greater than 120 minutes, then keep the flight. Otherwise, cancel

from queue import PriorityQueue
N,M,F = map(int, input().split())

train_adj = [[] for _ in range(N)]
plane_adj = [None for _ in range(F)]

for _ in range(M):
    v,u,w = map(int,input().split())
    train_adj[v].append((u,w))
    train_adj[u].append((v,w))

for i in range(F):
    v,u = map(int,input().split())
    plane_adj[i] = (v,u)

def find_time(start,end):
    lengths = [None for _ in range(N)]
    queue = PriorityQueue()
    queue.put((0,start))

    while queue.empty() is not True:
        d, vertex = queue.get()
        if lengths[vertex] is None:
            lengths[vertex] = d
            for v,w in train_adj[vertex]:
                queue.put((d + w, v))
    return lengths[end]


for r in range(F):
    if find_time(plane_adj[r][0], plane_adj[r][1]) > 120:
        print("keep")
    else:
        print("cancel")