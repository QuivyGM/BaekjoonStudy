if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        R, S = input().split()
        for char in S:
            for _ in range(int(R)):
                print(char, end = "")
        print()