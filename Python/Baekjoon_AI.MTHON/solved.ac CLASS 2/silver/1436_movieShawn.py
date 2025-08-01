N = int(input())
num = 665
while N > 0:
	num += 1
	if '666' in str(num):
		N -= 1
print(num)

'''
import heapq

def generate_doom_number(N):
    seen = set()
    heap = []

    heapq.heappush(heap, 666)
    seen.add(666)

    count = 0
    while heap:
        num = heapq.heappop(heap)
        count += 1
        if count == N:
            return num

        str_num = str(num)

        for i in range(len(str_num) + 1):
            new_str = str_num[:i] + '666' + str_num[i:]
            new_num = int(new_str)
            if new_num not in seen:
                seen.add(new_num)
                heapq.heappush(heap, new_num)

larger numbers (like 6660, 66600)
        new_num = num * 10
        if new_num not in seen:
            seen.add(new_num)
            heapq.heappush(heap, new_num)

N = int(input("Enter N: "))
print(generate_doom_number(N))
'''