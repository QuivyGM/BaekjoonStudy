N = int(input())
bag = 0
# N을 5로 나누기, 3으로 나눠지면 출력 안되면 0
for i in range(N//5, -1, -1):
	if ( (N-5*i)%3 == 0 ):
		print(i + (N-5*i)//3)
		break

else:
    print(-1)