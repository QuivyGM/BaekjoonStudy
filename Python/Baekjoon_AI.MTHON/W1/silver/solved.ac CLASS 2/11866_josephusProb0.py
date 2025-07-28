N, K = map(int, input().split())
circle = []

for a in range(1, N+1):
	circle.append(a)
	
pos = K-1

print("<", end = "")
while (len(circle) > 0):
	pos %= len(circle)
	print(circle.pop(pos), end = ', ' if len(circle) > 0 else '')
	pos += K - 1
print(">")