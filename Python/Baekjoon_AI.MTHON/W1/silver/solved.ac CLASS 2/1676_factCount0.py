def factorial(N):
	num = 1
	for i in range(2, N+1):
		num *= i
	return num

N = str(factorial(int(input())))
count = 0
# range(start, stop, step)
for i in range(len(N)-1, 1, -1):
	if N[i] == '0':
		count += 1
	else:
		break
print(count)