N = int(input())
for _ in range(N):
    input_list = input()
    input_count = 0

    for paranthesis in input_list:
        if paranthesis == "(":
            input_count += 1
        else:
            if input_count > 0:
                input_count -= 1
            else:
                input_count = -1
                break

    if input_count == 0:
        print("YES")
    else:
        print("NO")
