N = int(input())
path_data = [0] * (N + 1)

for i in range(2, N + 1):
    path_data[i] = path_data[i - 1] + 1

    # 2로 나뉘어 질때
    if i % 2 == 0:
        path_data[i] = min(path_data[i], path_data[i // 2] + 1)
    # 3으로 나뉘어 질때
    if i % 3 == 0:
        path_data[i] = min(path_data[i], path_data[i // 3] + 1)

print(path_data[N])