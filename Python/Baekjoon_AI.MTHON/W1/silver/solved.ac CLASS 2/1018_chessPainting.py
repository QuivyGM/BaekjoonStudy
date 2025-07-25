if __name__ == "__main__":
    # get input
    Y, X = map(int, input().split())

    full_board = []

    # get board
    for DOWN in range(Y):
        line = input()
        full_board.append(list(line))

    min_count = float('inf')  # track the minimum repaint count

    # find 8x8 board areas
    for start_y in range(Y - 7):  # FIXED: Y - 7 for inclusive 8 rows
        for start_x in range(X - 7):  # FIXED: X - 7 for inclusive 8 cols
            w_count = 0

            for i in range(8):
                for j in range(8):
                    current = full_board[start_y + i][start_x + j]
                    # expected color for (i, j) in W-start and B-start
                    if (i + j) % 2 == 0:
                        if current != 'W':
                            w_count += 1
                    else:
                        if current != 'B':
                            w_count += 1

            min_count = min(min_count, w_count, 64-w_count)

    print(min_count)
