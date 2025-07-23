import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    
    print(min(numbers), max(numbers))