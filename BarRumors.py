"""
Use BFS to count the amount of neighbours of a vertex.
The vertex with the biggest amount of non-visited neighbours are the result
"""
N,M,s = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    i,j = map(int, input().split())
    adj_list[i].append(j)
    adj_list[j].append(i)

day = 0
visited = set()

queue = []
queue.append(s)

max_friends_told = 0
max_day = 0

while queue:
    vertex = queue.pop(0)
    visited.add(vertex)
    friends_told = 0
    day += 1
    for neighbour in adj_list[vertex]:
        if neighbour not in visited:
            queue.append(neighbour)
            friends_told += 1
    if max_friends_told < friends_told:
        max_friends_told = friends_told
        max_day = day

print(max_friends_told)
print(max_day)


    




