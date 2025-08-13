number_of_computers = int(input())
number_of_connections = int(input())

network_group = [{i} for i in range(1, number_of_computers + 1)]


for _ in range(number_of_connections):
    port1, port2 = map(int, input().split())
    first_idx = second_idx = None

    for i, group in enumerate(network_group):
        if port1 in group:
            first_idx = i
        if port2 in group:
            second_idx = i

    if first_idx != second_idx:
        if first_idx > second_idx:
            first_idx, second_idx = second_idx, first_idx
        network_group[first_idx].update(network_group[second_idx])
        del network_group[second_idx]
        
print(len(network_group[0])-1)