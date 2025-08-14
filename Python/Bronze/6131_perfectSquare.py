N = int(input())
count = 0

for B in range(1, 500):
    for A in range(B+1, 501):
        if (A**2 - B**2) == N:
            count += 1
            #print(A, B)
print(count)