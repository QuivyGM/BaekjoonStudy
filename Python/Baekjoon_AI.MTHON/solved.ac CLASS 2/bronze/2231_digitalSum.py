N = int(input())
start = max(1, N - 9 * len(str(N)))  # 음수 방지
temp = 0

for number in range(start, N):
    temp = number
    for d in str(number):
        temp += int(d)
    if temp == N:
        temp = number
        break

print(temp)
