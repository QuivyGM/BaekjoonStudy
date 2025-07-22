## 11a+2b = c

# start with 1
def self_num(X):
    numbers = list(X)
    for num in numbers:
        X += num
    return X

if __name__ == "__main__":
    print(self_num())