## 11a+2b = c

self_number = []
LIMIT = 10001

# start with 1
def self_num(X):
    numbers = list(str(X))
    for num in numbers:
        X += int(num)
    return X

    # for digit in str(X):
    #     X += int(digit)
    # return X

if __name__ == "__main__":
    for i in range(1, LIMIT):
        new_num = self_num(i)
        if new_num < LIMIT:
            self_number.append(new_num)
    
    for i in range(1, LIMIT):
        if i not in self_number:
            print(i)
