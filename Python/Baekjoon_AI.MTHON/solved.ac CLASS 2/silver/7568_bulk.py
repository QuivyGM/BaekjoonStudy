N = int(input())
data = []
for _ in range(N):
    weight, height = map(int, input().split())
    data.append([weight, height, 1])

for a in range(N):
	for b in range(a+1, N):
		if data[a][0] < data[b][0] and data[a][1] < data[b][1]:
			data[a][2] += 1
		elif data[a][0] > data[b][0] and data[a][1] > data[b][1]: 
			data[b][2] += 1
	print(data[a][2])