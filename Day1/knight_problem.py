def is_valid_move(board, row, col, N):
    return row >= 0 and row < N and col >= 0 and col < N and board[row][col] == -1


def knights_tour_util(board, row, col, move_count, N, row_moves, col_moves):
    if move_count == N * N:
        return True

    for i in range(8):
        next_row = row + row_moves[i]
        next_col = col + col_moves[i]
        if is_valid_move(board, next_row, next_col, N):
            board[next_row][next_col] = move_count
            if knights_tour_util(board, next_row, next_col, move_count + 1, N, row_moves, col_moves):
                return True
            board[next_row][next_col] = -1

    return False


def knights_tour(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    row_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    col_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    # Start at position (0, 0)
    board[0][0] = 0

    if knights_tour_util(board, 0, 0, 1, N, row_moves, col_moves):
        for row in board:
            print(row)
    else:
        print("No solution exists.")


N = int(input("Enter the value of N, i.e the chess square size: "))
knights_tour(N)

