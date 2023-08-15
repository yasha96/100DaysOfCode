def exist(board, word):
    if not board:
        return False

    rows = len(board)
    cols = len(board[0])

    def dfs(i, j, k):
        if not 0 <= i < rows or not 0 <= j < cols or board[i][j] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        temp = board[i][j]
        board[i][j] = '#'

        found = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)

        board[i][j] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False

