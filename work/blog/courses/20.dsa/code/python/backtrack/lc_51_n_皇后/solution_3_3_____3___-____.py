# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239695
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solveNQueens(n):  # 定义函数 solveNQueens（参数：元素个数）
    res = []  # 把 [] 存入 结果
    cols = [False] * n  # 把 [False] 乘 元素个数 存入 列数
    diag1 = [False] * (2 * n)  # 把 [False] 乘 (2 乘 元素个数) 存入 diag1
    diag2 = [False] * (2 * n)  # 把 [False] 乘 (2 乘 元素个数) 存入 diag2
    board = []  # 把 [] 存入 棋盘

    def backtrack(r):  # 定义函数 backtrack（参数：右指针）
        if r == n:  # 若 右指针 等于 元素个数
            res.append(["".join(row) for row in board])  # 把 [''.join(row 追加到列表尾部
            return  # return
        for c in range(n):  # 让 字符 从 元素个数 遍历
            if (
                cols[c] or diag1[r - c + n] or diag2[r + c]
            ):  # 若 列数[字符] or diag1[右指针 减 字符 加 元素个数] or diag2[右指针 加 字符]
                continue  # 跳过本轮，进入下一次
            cols[c] = diag1[r - c + n] = diag2[r + c] = True
            board.append(
                ["."] * c + ["Q"] + ["."] * (n - 1 - c)
            )  # 把 ['.'] 乘 字符 加 ['Q'] 加 ['.'] 乘 (元素个数 减 1 减 字符 追加到列表尾部
            backtrack(r + 1)  # backtrack(右指针 加 1)
            board.pop()  # 弹出栈顶元素
            cols[c] = diag1[r - c + n] = diag2[r + c] = False

    backtrack(0)  # backtrack(0)
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(solveNQueens(4))  # 打印输出
