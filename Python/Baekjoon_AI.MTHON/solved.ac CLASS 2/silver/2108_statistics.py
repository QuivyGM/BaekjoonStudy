import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

# 산술평균
mean = round(sum(nums) / n)

print(mean)

# 중앙값
nums_sorted = sorted(nums)
median = nums_sorted[n // 2]

print(median)

# 최빈값
freq = [0] * 8001

for num in nums:
    freq[num + 4000] += 1

max_freq = max(freq)
modes = [i - 4000 for i, f in enumerate(freq) if f == max_freq]

modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]

print(mode)

# 범위
range_val = nums_sorted[-1] - nums_sorted[0]

print(range_val)