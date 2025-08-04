M = int(input())
S = 0

results = []

for _ in range(M):
    command = input().strip().split()

    if command[0] == "add":
        x = int(command[1])
        S |= (1 << (x - 1))

    elif command[0] == "remove":
        x = int(command[1])
        S &= ~(1 << (x - 1))

    elif command[0] == "check":
        x = int(command[1])
        results.append(str((S >> (x - 1)) & 1))

    elif command[0] == "toggle":
        x = int(command[1])
        S ^= (1 << (x - 1))

    elif command[0] == "all":
        S = (1 << 20) - 1

    elif command[0] == "empty":
        S = 0

print("\n".join(results))
