# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238257
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solveSudoku(board):  # 定义函数 solveSudoku（参数：棋盘）
    def is_valid(board, row, col, num):  # 定义函数 is_valid（参数：棋盘, row, col, num）
        for i in range(9):  # 让 下标 i 从 9 遍历
            if board[i][col] == num:  # 若 棋盘[下标 i][col] 等于 num
                return False  # 返回 False
            if board[row][i] == num:  # 若 棋盘[row][下标 i] 等于 num
                return False  # 返回 False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):  # 让 下标 i 从 3 遍历
            for j in range(3):  # 让 下标 j 从 3 遍历
                if (
                    board[start_row + i][start_col + j] == num
                ):  # 若 棋盘[start_row 加 下标 i][start_col 加 下标 j] 等于 num
                    return False  # 返回 False
        return True  # 返回 True

    def backtrack(board):  # 定义函数 backtrack（参数：棋盘）
        for row in range(9):  # 让 row 从 9 遍历
            for col in range(9):  # 让 col 从 9 遍历
                if board[row][col] == ".":  # 若 棋盘[row][col] 等于 '.'
                    for num in "123456789":  # for num in '123456789':
                        if is_valid(board, row, col, num):  # 若 is_valid(棋盘, row, col, num
                            board[row][col] = num  # 把 num 写入 board[row][col]
                            if backtrack(board):  # 若 backtrack(棋盘
                                return True  # 返回 True
                            board[row][col] = "."  # 把 '.' 写入 board[row][col]
                    return False  # 返回 False
        return True  # 返回 True

    backtrack(board)  # backtrack(棋盘)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solveSudoku(board)  # solveSudoku(棋盘)
    for row in board:  # 逐个取出 棋盘 的元素（row）
        print(row)  # 打印输出
