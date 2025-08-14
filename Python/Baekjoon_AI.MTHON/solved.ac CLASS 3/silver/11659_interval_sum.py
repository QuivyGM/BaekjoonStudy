import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + num_list[i - 1]

for _ in range(M):
    start, end = map(int, input().split())
    sys.stdout.write(str(prefix[end] - prefix[start - 1]) + "\n")

