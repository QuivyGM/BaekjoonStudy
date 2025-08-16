T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    # create group set
    cabbages = []
    group_set = []

    for _ in range(K):
        x, y = map(int, input().split())
        cabbages.append((x, y))

    for x, y in cabbages:
        touching_groups = []
        for group in group_set:
            if (x+1, y) in group or (x-1, y) in group or (x, y+1) in group or (x, y-1) in group:
                touching_groups.append(group)

        if not touching_groups:
            # new group
            group_set.append({(x, y)})
        else:
            # merge all touching groups
            merged = {(x, y)}
            for g in touching_groups:
                merged |= g
                group_set.remove(g)
            group_set.append(merged)

    print(len(group_set))
