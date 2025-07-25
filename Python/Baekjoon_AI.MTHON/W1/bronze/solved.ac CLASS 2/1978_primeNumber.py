def check_prime(X):
    if X < 2:  # 0 and 1 are not prime
        return 0
    for i in range(2, int(X ** 0.5) + 1):  # Check up to sqrt(X)
        if X % i == 0:
            return 0
    return 1

N = int(input())
count = 0
for _ in range(N):
    count += check_prime(int(input()))
print(count)