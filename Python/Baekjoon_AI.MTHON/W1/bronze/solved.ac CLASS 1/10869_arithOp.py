A, B = map(int, input().split())
ops = [A + B, A - B, A * B, A // B, A % B]
print(*ops, sep='\n')