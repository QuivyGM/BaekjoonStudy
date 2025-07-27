ISBN = input().strip()
ISBN_check = 0
corrupt_weight = 0

for pos, number in enumerate(ISBN):
    if number != '*':
        ISBN_check += int(number) * (1 if (pos % 2 == 0) else 3)
    else:
        corrupt_weight = 1 if (pos % 2 == 0) else 3

for x in range(10):
    if (ISBN_check + corrupt_weight * x) % 10 == 0:
        print(x)
        break
