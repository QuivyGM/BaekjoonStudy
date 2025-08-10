N, L = map(int, input().split())
zebra = [input().strip() for _ in range(N)]
stripe = [0, 0]

for i in range(N):
    temp = 0
    for j in range(L):
        if zebra[i][j] == '1':
            temp += 1
            if j > 0 and zebra[i][j-1] == '1':
                temp -= 1
    if temp > stripe[0]:
        stripe[0] = temp
        stripe[1] = 1
    elif temp == stripe[0]:
        stripe[1] += 1

print(stripe[0], stripe[1])