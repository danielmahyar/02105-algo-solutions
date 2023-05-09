from collections import deque

N, M = map(int, input().split(" "))


adj = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
in_degree = [0 for _ in range(N + 1)]

for _ in range(M):
    X, Y = map(int, input().split())
    adj[Y].append(X)
    in_degree[X] += 1

current_layer = []
for i in range(1, N + 1):
    if in_degree[i] == 0:
        current_layer.append(i)

n_semesters = 0

while current_layer:
    next_layer = []
    n_semesters += 1

    for course in current_layer:
        for dependend_course in adj[course]:
            in_degree[dependend_course] -= 1
            if in_degree[dependend_course] == 0:
                next_layer.append(dependend_course)
    current_layer = next_layer

print(n_semesters)
    