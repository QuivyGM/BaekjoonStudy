N = int(input())
cord_list = []
for _ in range(N):
	x, y = map(int, input().split())
	cord_list.append([x, y])
    
cord_list.sort(key=lambda a: (a[1], a[0]))

for i in range(N):
	print(f"{cord_list[i][0]} {cord_list[i][1]}")

#------------------------------

# N = int(input())
# cord_list = [tuple(map(int, input().split())) for _ in range(N)]

# cord_list.sort(key=lambda a: (a[1], a[0]))

# for x, y in cord_list:
#     print(x, y)