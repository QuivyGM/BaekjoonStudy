T = int(input())

for _ in range(T):
    pQueue = []
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    for i in range(N):
        pQueue.append((priorities[i], i))  # (priority, index)
    
    count = 0
    while pQueue:
        current = pQueue.pop(0)
        if any(current[0] < other[0] for other in pQueue):
            pQueue.append(current)
        else:
            count += 1
            if current[1] == M:
                print(count)
                break
