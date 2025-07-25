import math

N = int(input())
size_list = list(map(int, input().split()))
T, P = map(int, input().split())

shirts = 0
for number in size_list:
    shirts += math.ceil(number / T)

print(shirts)
print(N // P, N % P)