n = int(input())

min_x = 10_000
max_x = -10_000
min_y = 10_000
max_y = -10_000

for _ in range(n):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

width = max_x - min_x
height = max_y - min_y
print(width * height)
