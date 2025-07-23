if __name__ == "__main__":

    # get number
    N = int(input())
    fraction_sum = 1

    while(N > fraction_sum):
        N -= fraction_sum
        fraction_sum += 1
    
    # print(N, fraction_sum)

    num, denom = 0, 0
    if (fraction_sum % 2 == 0):
        num = N
        denom = fraction_sum - N + 1
    else:
        num = fraction_sum - N + 1
        denom = N

    print(f"{num}/{denom}")
