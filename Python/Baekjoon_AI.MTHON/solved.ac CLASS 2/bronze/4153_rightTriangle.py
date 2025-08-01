while True:
    tri_val = sorted(map(int, input().split()))
    if tri_val == [0, 0, 0]:
        break
    print("right" if tri_val[0]**2 + tri_val[1]**2 == tri_val[2]**2 else "wrong")