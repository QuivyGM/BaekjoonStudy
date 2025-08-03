low, high = map(int, input().split())

is_prime = [True] * (high + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(high**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, high + 1, i):
            is_prime[j] = False

for i in range(low, high + 1):
    if is_prime[i]:
        print(i)
