H, M = map(int, input().split())
M -= 45
print((H - 1) % 24 if M < 0 else H, M % 60)