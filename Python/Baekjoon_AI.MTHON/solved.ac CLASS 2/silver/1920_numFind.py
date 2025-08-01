N = int(input())
input_num = set()
input_num = set(map(int, input().split()))
    
M = int(input())
search_input = list(map(int, input().split()))

for search in search_input:
    print(1 if search in input_num else 0)