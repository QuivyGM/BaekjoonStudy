import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]

num_list.sort()

for num in sorted(num_list):
    print(num)