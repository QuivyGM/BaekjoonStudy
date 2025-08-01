def fac(N):
    total = 1
    for i in range(1, N + 1):
        total *= i
    return total

N, K = map(int, input().split())
print( fac(N) // (fac(K) * fac(N-K) ) )