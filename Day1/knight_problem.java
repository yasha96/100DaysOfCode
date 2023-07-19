import java.util.Arrays;

class KnightTour {
    static final int[] rowMoves = {2, 1, -1, -2, -2, -1, 1, 2};
    static final int[] colMoves = {1, 2, 2, 1, -1, -2, -2, -1};

    static boolean isValidMove(int[][] board, int row, int col, int N) {
        return row >= 0 && row < N && col >= 0 && col < N && board[row][col] == -1;
    }

    static boolean knightsTourUtil(int[][] board, int row, int col, int moveCount, int N) {
        if (moveCount == N * N) {
            return true;
        }

        for (int i = 0; i < 8; i++) {
            int nextRow = row + rowMoves[i];
            int nextCol = col + colMoves[i];
            if (isValidMove(board, nextRow, nextCol, N)) {
                board[nextRow][nextCol] = moveCount;
                if (knightsTourUtil(board, nextRow, nextCol, moveCount + 1, N)) {
                    return true;
                }
                board[nextRow][nextCol] = -1;
            }
        }

        return false;
    }

    static void knightsTour(int N) {
        int[][] board = new int[N][N];
        for (int[] row : board) {
            Arrays.fill(row, -1);
        }

        // Start at position (0, 0)
        board[0][0] = 0;

        if (knightsTourUtil(board, 0, 0, 1, N)) {
            for (int[] row : board) {
                System.out.println(Arrays.toString(row));
            }
        } else {
            System.out.println("No solution exists");
        }
    }

    public static void main(String[] args) {
        int N = 6;
        knightsTour(N);
    }
}

