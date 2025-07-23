if __name__ == "__main__":
    S = input()
    for char in range(97, 123):
        print(S.find(chr(char)), end=' ')