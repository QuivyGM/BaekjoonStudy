import sys

N = int(sys.stdin.readline())
count = [0] * 10001  # 숫자의 범위가 0~10000일 때

for _ in range(N):
    count[int(sys.stdin.readline())] += 1

write = sys.stdout.write
for i in range(10001):
    if count[i]:
        for _ in range(count[i]):
            write(f"{i}\n")