while True:
    N = input().strip()
    if N == "0":
        break
    if N == N[::-1]:
        print("yes")
    else:
        print("no")