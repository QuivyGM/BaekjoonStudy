N = int(input())

apartment = []
floor = []

# 0층 세팅
for n in range(15):
    floor.append(n)

apartment.append(floor)

# 나머지 층
for story in range(1, 15):  # 1층부터 14층까지
    floor = []
    for room in range(15):
        temp = 0
        for i in range(room + 1):
            temp += apartment[story - 1][i]
        floor.append(temp)
    apartment.append(floor)

for _ in range(N):
    k = int(input())
    n = int(input())
    print(apartment[k][n])