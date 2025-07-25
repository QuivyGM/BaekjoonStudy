N = int(input())
name_dict = {}

for _ in range(N):
    age, name = input().split()
    age = int(age)
    
    if age not in name_dict:
        name_dict[age] = []
    name_dict[age].append(name)

for age in sorted(name_dict.keys()):
    for name in name_dict[age]:
        print(age, name)