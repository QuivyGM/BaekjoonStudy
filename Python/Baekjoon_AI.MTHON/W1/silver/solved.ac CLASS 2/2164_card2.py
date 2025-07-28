N = int(input())
for num in range(0, N+1):
	# print(2**(num-1), N)
	if N <= 2**num:
		print(2**(num-1))
		break