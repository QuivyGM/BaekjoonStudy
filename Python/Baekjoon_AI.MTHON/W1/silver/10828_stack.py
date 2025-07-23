stack = []

# push: add X to stack
def push(X):
    stack.append(X)

# pop: remove most recent id
def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[len(stack) - 1])
        stack.pop()

# size: size of stack
def size():
    print(len(stack))

# empty: is stack empty?
def empty():
    if not len(stack):
        print(1)
    else:
        print(0)

# top: most recent stack
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[len(stack) - 1])

if __name__ == "__main__":

    # get number of input
    N = int(input(""))

    # start loop
    for _ in range(N):
        # get input and split
        cmd = input("").split()

        # carry out command
        if cmd[0] == "push":
            push(cmd[1])
        
        elif cmd[0] == "pop":
            pop()
        
        elif cmd[0] == "size":
            size()
        
        elif cmd[0] == "empty":
            empty()
        
        else:
            top()