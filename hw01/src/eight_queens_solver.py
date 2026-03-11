def print_solution(board):
    """打印棋盘配置。"""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    """检查在 board[row][col] 放置皇后是否安全。"""
    # 检查左侧行
    for i in range(col):
        if board[row][i]:
            return False

    # 检查左上对角线
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # 检查左下对角线
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, col, n, callback=None):
    """使用回溯法求解 N 皇后问题。"""
    if col >= n:
        # 1. 打印解（保持你原有功能）
        print_solution(board)
        # 2. 如果提供了回调函数，将当前解传给它（满足测试要求）
        if callback:
            # 将布尔矩阵转换为简单的行索引列表（通常测试脚本期待这种格式，或直接传 board）
            # 这里我们配合测试脚本的需求，如果它需要 board，就传 board
            callback(board) 
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = True
            # 递归传递 callback
            res = solve_n_queens_util(board, col + 1, n, callback) or res
            board[i][col] = False

    return res

def solve_n_queens(n, callback=None):
    """求解 N 皇后问题，打印所有解，并通过 callback 返回。"""
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0, n, callback):
        if not callback: # 只有非测试模式下才打印
            print("No solution exists")

if __name__ == "__main__":
    # 手动运行时依然有效
    N = 8
    solve_n_queens(N)
