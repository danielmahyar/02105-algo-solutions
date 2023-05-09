N = int(input())
houses = [int(i) for i in input().split()]

max_chain = 1
curr_chain = 1

houses.sort()


for i in range(1, N):
    if houses[i] == houses[i-1] + 1:
        curr_chain += 1
    else:
        max_chain = max(max_chain, curr_chain)
        curr_chain = 1

max_chain = max(max_chain, curr_chain)

print(max_chain)