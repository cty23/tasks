def print_solution(board):
    """Print the chessboard configuration."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on the left
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, col, n):
    """Utilize backtracking to solve the N-Queens problem."""
    if col >= n:
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = True
            res = solve_n_queens_util(board, col + 1, n) or res
            board[i][col] = False

    return res

def solve_n_queens(n):
    """Solve the N-Queens problem and print all solutions."""
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("No solution exists")

if __name__ == "__main__":
    N = 8
    solve_n_queens(N)
