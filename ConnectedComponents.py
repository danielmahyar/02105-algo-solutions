N,M = map(int, input().split())
sizes = [int(i) for i in input().split()]

sizes.sort(reverse=True)

sum = 0
inc = 0

for size in sizes:
    sum += size
    inc += 1
    if sum >= N:
        print(inc)
        break
    else:
        continue
