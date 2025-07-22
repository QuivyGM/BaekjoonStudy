last_letter = ["=", "-", "j"]

line = list(input())

letter_num = len(line)

for i, letter in enumerate(line):
    if letter in last_letter and i > 0:
        # if dze then -= 2
        if letter == "=" and line[i-1] == "z" and line[i-2] == "d":
            letter_num -= 2
            # print("dz= found")
        elif letter == "j":
            if line[i-1] == "l" or line[i-1] == "n":
                letter_num -= 1
                # print("j letter")
            
        else:
            letter_num -= 1
            # print("weird alphabet")

    else:
        continue

print(letter_num)