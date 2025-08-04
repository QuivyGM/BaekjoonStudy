N = int(input())
P = list(map(int, input().split()))

P.sort()

total = 0
current = 0

for time in P:
    current += time
    total += current

print(total)
