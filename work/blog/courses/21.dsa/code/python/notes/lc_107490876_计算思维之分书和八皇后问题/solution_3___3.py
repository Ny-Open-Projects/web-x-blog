# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def n_queens_safe():  # 定义函数 n_queens_safe（参数：无）
    """八皇后问题（逐列放置 + 显式安全检查 isSafe）：
    在 8x8 棋盘上放置 8 个皇后使其互不攻击。board[col]=row 记录每列皇后所在行。
    返回所有方案的列表。"""
    results = []  # 把 [] 存入 results
    board = [0] * 8  # board[col] = row

    def is_safe(col, row):  # 定义函数 is_safe（参数：col, row）
        for c in range(col):  # 让 字符 从 col 遍历
            if board[c] == row or abs(board[c] - row) == abs(
                c - col
            ):  # 若 棋盘[字符] 等于 row or 取绝对值 棋盘[字符] 减 row) 等于 取绝对值 字符 减 col
                return False  # 返回 False
        return True  # 返回 True

    def place(col):  # 定义函数 place（参数：col）
        if col == 8:  # 若 col 等于 8
            results.append(board[:])  # 把 复制 棋盘 追加到列表尾部
            return  # return
        for row in range(1, 9):  # 让 row 从 1 到 9 遍历
            if is_safe(col, row):  # 若 is_safe(col, row
                board[col] = row  # 把 row 写入 board[col]
                place(col + 1)  # place(col 加 1)

    place(0)  # place(0)
    return results  # 返回 results


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    sols = n_queens_safe()  # 把 n_queens_safe() 存入 sols
    print("八皇后方案数:", len(sols))  # 打印输出
    print("第一个方案(列->行):", sols[0])  # 打印输出
