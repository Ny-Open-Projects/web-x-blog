# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239695
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solveNQueens(n):  # 定义函数 solveNQueens（参数：元素个数）
    res = []  # 把 [] 存入 结果
    cols = set()  # 把 set() 存入 列数
    diag1 = set()  # 把 set() 存入 diag1
    diag2 = set()  # 把 set() 存入 diag2

    def backtrack(r, board):  # 定义函数 backtrack（参数：右指针, 棋盘）
        if r == n:  # 若 右指针 等于 元素个数
            res.append(["".join(row) for row in board])  # 把 [''.join(row 追加到列表尾部
            return  # return
        for c in range(n):  # 让 字符 从 元素个数 遍历
            if (
                c in cols or (r - c) in diag1 or (r + c) in diag2
            ):  # 若 字符 in 列数 or (右指针 减 字符) in diag1 or (右指针 加 字符) in diag2
                continue  # 跳过本轮，进入下一次
            cols.add(c)  # 列数 追加 字符)
            diag1.add(r - c)  # diag1 追加 右指针 减 字符)
            diag2.add(r + c)  # diag2 追加 右指针 加 字符)
            board.append(
                ["."] * c + ["Q"] + ["."] * (n - 1 - c)
            )  # 把 ['.'] 乘 字符 加 ['Q'] 加 ['.'] 乘 (元素个数 减 1 减 字符 追加到列表尾部
            backtrack(r + 1, board)  # backtrack(右指针 加 1, 棋盘)
            board.pop()  # 弹出栈顶元素
            cols.remove(c)  # 列数 弹出 字符)
            diag1.remove(r - c)  # diag1 弹出 右指针 减 字符)
            diag2.remove(r + c)  # diag2 弹出 右指针 加 字符)

    backtrack(0, [])  # backtrack(0, [])
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(solveNQueens(4))  # 打印输出
