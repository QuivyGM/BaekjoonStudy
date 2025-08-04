N, M = map(int, input().split())

hear_set = set(input().strip() for _ in range(N))
see_set = set(input().strip() for _ in range(M))

result = []

for name in hear_set:
    if name in see_set and True:
        result.append(name)

result.sort()

print(len(result))
for name in result:
    print(name)