import heapq

# Read input
N = int(input())
M = int(input())
R = int(input())
removals = []
for i in range(R):
    n, m = map(int, input().split())
    removals.append((n, m, i+1))

# Create graph
graph = {}
for i in range(N):
    for j in range(M):
        node = i * M + j
        neighbors = []
        if i > 0:
            neighbors.append((node-M, 1))
        if i < N-1:
            neighbors.append((node+M, 1))
        if j > 0:
            neighbors.append((node-1, 1))
        if j < M-1:
            neighbors.append((node+1, 1))
        graph[node] = neighbors

# Sort removals by time
removals.sort(key=lambda x: x[2])

# Find shortest path
start_node = 0
end_node = N*M-1
dist = [float('inf')] * (N*M)
dist[start_node] = 0
pq = [(0, start_node)]
visited = set()
removal_idx = 0
while pq:
    curr_dist, curr_node = heapq.heappop(pq)
    if curr_node == end_node:
        print(curr_dist)
        break
    if curr_dist > dist[curr_node]:
        continue
    if curr_node in visited:
        continue
    visited.add(curr_node)
    # Check if we can remove a stone at this time
    while removal_idx < R and removals[removal_idx][2] <= curr_dist:
        n, m, t = removals[removal_idx]
        node = n * M + m
        if t < dist[node]:
            dist[node] = t
            heapq.heappush(pq, (t, node))
        removal_idx += 1
    for neighbor, weight in graph[curr_node]:
        alt_dist = curr_dist + weight
        if alt_dist < dist[neighbor]:
            dist[neighbor] = alt_dist
            heapq.heappush(pq, (alt_dist, neighbor))