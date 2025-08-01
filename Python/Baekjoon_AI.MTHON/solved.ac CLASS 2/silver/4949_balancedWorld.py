while True:
	
	stack = []
	
	sentence = input()

	if sentence == '.':
		break

	for letter in sentence:

		# square brackets
		if letter == '[':
			stack.append("[")

		if letter == ']':
			if len(stack) < 1 or stack[-1] != '[':
				stack.append("no")
				break
			else:
				stack.pop()
		
		# parenthesis
		if letter == '(':
			stack.append("(")

		if letter == ')':
			if len(stack) < 1 or stack[-1] != '(':
				stack.append("no")
				break
			else:
				stack.pop()

	if len(stack) == 0:
		print("yes")
	else:
		print("no")
