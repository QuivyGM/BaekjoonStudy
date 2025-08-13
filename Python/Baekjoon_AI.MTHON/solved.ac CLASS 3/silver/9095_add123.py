# def comb_for(m, n):
#     result = 1
#     for a in range(m, m-n, -1):
#         result *= a
#     for a in range(2, n+1):
#         result //= a
#     return result

# T = int(input())

# for _ in range(T):
#     n = int(input())
#     count = 0
#     # 1, 2 and 3
#     for one in range(0, n + 1):  # at least 1 of "1"
#         for two in range(0, n // 2 + 1):  # at least 1 of "2"
#             for three in range(0, n // 3 + 1):  # at least 1 of "3"
#                 if one + 2*two + 3*three == n:
#                     total = one + two + three
#                     ways = comb_for(total, two) * comb_for(total - two, three)
#                     count += ways
#     print(count)


T = int(input())

# n 최대값이 10이므로 11까지 생성
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])
