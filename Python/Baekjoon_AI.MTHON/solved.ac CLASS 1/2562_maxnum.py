if __name__ == "__main__":
    numbers = []
    
    for _ in range(9):
        num = int(input())
        numbers.append(num)
    
    max_value = max(numbers)
    position = numbers.index(max_value) + 1

    print(max_value)
    print(position)
