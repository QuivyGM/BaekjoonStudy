fib = { 0: [1, 0], 1: [0, 1] }

def fibonacci(n):
    if n not in fib:
        a = fibonacci(n - 1)
        b = fibonacci(n - 2)
        fib[n] = [a[0] + b[0], a[1] + b[1]]

    return fib[n]

fibonacci(40)

n = int(input())
for _ in range(n):
    m = int(input())
    print(fibonacci(m)[0], fibonacci(m)[1])