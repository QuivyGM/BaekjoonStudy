n, Time = map(int, input().split())
jobs = list(map(int, input().split()))

for i, job in enumerate(jobs):
    if Time < job:
        print(i)
        break
    Time -= job
else:
    print(n)