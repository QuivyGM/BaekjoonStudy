N = int(input())

answer = 1

while N > 1:
    N -= answer * 6
    answer += 1

print(answer)