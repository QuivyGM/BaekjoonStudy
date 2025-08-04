n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
operations = []
current = 1

for target in sequence:
    while current <= target:
        stack.append(current)
        operations.append('+')
        current += 1

    if stack[-1] == target:
        stack.pop()
        operations.append('-')
    else:
        current = -10
        break

if current != -10:
    for op in operations:
        print(op)
else:
    print("NO")
