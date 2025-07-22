
import sys
input = sys.stdin.readline
stack = []

if __name__ == "__main__":

    # how many commands
    lines = int(input())

    
    for commands in range(lines):
        cmd = input().strip().split()

        if cmd[0] == "push":
            stack.append(int(cmd[1]))
            
        elif cmd[0] == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
                

        elif cmd[0] == "size":
            print(len(stack))            

        elif cmd[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)

        elif cmd[0] == "top":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
