import sys
input = sys.stdin.readline

stack = []

if __name__ == "__main__":

    # get number of input
    N = int(input())

    # start loop
    for _ in range(N):
        # get input and split
        cmd = input().split()

        # carry out command
        if cmd[0] == "push":
            stack.append(int(cmd[1]))
        
        elif cmd[0] == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack) - 1])
                stack.pop()
        
        elif cmd[0] == "size":
            print(len(stack))
        
        elif cmd[0] == "empty":
            if not len(stack):
                print(1)
            else:
                print(0)
        
        else:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack) - 1])