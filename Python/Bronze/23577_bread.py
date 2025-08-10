N = int(input())
shop = []
for _ in range(N):
	A, B = map(int, input().split())
	if A <= B:
		shop.append(B)
print(min(shop) if len(shop) > 0 else -1)