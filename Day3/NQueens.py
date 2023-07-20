def is_safe(board, row, col, N):
    # Checking to see if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Checking for the upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Checking for the  upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens_util(board, row, N, result):
    if row == N:
        result.append([''.join(['Q' if col == 1 else '.' for col in row]) for row in board])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, N, result)
            board[row][col] = 0


def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    solve_n_queens_util(board, 0, N, result)
    return result


N = int(input("Enter the number : "))
queens_solutions = solve_n_queens(N)
for solution in queens_solutions:
    for row in solution:
        print(row)
    print()

