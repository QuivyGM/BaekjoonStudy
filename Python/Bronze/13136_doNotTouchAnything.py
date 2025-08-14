R, C, N = map(int, input().split())

if R%N:
    R+=N-R%N
if C%N:
    C+=N-C%N

print(R*C//(N**2))