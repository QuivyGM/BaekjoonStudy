N = int(input())
for _ in range(N):
	sheet = list(input())
	score = 0
	counter = 1
	for letter in sheet:
		if letter == "O":
			score += counter
			counter += 1
		else:
			counter = 1
	print(score)