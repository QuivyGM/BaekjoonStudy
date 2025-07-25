num_stack = []

if __name__ == "__main__":

    # get number of inputs
    N = int(input())

    for _ in range(N):

        # get new number
        cmd = int(input())

        if cmd == 0 and len(num_stack) > 0:
            num_stack.pop()
        else:
            num_stack.append(cmd)
    
    # print output
    print(sum(num_stack))

    # ---------------- version 2
    # stack_sum = 0

    # for _ in range(N):

    #     # get new number
    #     cmd = int(input())

    #     if cmd == 0 and len(num_stack) > 0:
    #         stack_sum -= num_stack[-1]
    #         num_stack.pop()
    #     else:
    #         num_stack.append(cmd)
    #         stack_sum += cmd
    
    # # print output
    # print(stack_sum)