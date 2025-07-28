from collections import Counter

N = int(input())
input_num = set(map(int, input().split()))

M = int(input())
search_input = list(map(int, input().split()))

search_count = Counter(search_input)


for num in input_num:
    print(f"search_count[num]")