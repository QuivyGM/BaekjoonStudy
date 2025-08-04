N, A, B = map(int, input().split())

if N > B:
    print("Bus")
else:
    if A < B:
        print("Bus")
    elif A > B:
        print("Subway")
    else:
        print("Anything")
