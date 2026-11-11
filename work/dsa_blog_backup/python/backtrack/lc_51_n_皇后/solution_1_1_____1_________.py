# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239695
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solveNQueens(n):  # 定义函数 solveNQueens（参数：元素个数）
    solutions = []  # 把 [] 存入 solutions
    queens = [-1] * n  # 把 [ 减 1] 乘 元素个数 存入 queens
    columns = set()  # 把 set() 存入 columns
    diagonal1 = set()  # 把 set() 存入 diagonal1
    diagonal2 = set()  # 把 set() 存入 diagonal2

    def generateBoard():  # 定义函数 generateBoard（参数：无）
        board = []  # 把 [] 存入 棋盘
        for i in range(n):  # 让 下标 i 从 元素个数 遍历
            row = ["."] * n  # 把 ['.'] 乘 元素个数 存入 row
            row[queens[i]] = "Q"  # 把 'Q' 写入 row[queens[i]]
            board.append("".join(row))  # 把 ''.join(row 追加到列表尾部
        return board  # 返回 棋盘

    def backtrack(row):  # 定义函数 backtrack（参数：row）
        if row == n:  # 若 row 等于 元素个数
            solutions.append(generateBoard())  # 把 generateBoard( 追加到列表尾部
            return  # return
        for col in range(n):  # 让 col 从 元素个数 遍历
            if col in columns or (row - col) in diagonal1 or (row + col) in diagonal2:
                continue  # 跳过本轮，进入下一次
            queens[row] = col  # 把 col 写入 queens[row]
            columns.add(col)  # columns 追加 col)
            diagonal1.add(row - col)  # diagonal1 追加 row 减 col)
            diagonal2.add(row + col)  # diagonal2 追加 row 加 col)
            backtrack(row + 1)  # backtrack(row 加 1)
            columns.discard(col)  # columns.discard(col)
            diagonal1.discard(row - col)  # diagonal1.discard(row 减 col)
            diagonal2.discard(row + col)  # diagonal2.discard(row 加 col)

    backtrack(0)  # backtrack(0)
    return solutions  # 返回 solutions


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    res = solveNQueens(4)  # 把 solveNQueens(4) 存入 结果
    for board in res:  # 逐个取出 结果 的元素（棋盘）
        print(board)  # 打印输出
    print("解的数量:", len(res))  # 打印输出
