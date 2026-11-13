# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def n_queens_simple():  # 定义函数 n_queens_simple（参数：无）
    """八皇后问题（简洁递归版）：以 (row, col) 记录已放置皇后，逐列尝试并检查攻击。"""
    positions = []  # 已放置的 (row, col)
    solutions = []  # 把 [] 存入 solutions

    def safe(r, c):  # 定义函数 safe（参数：右指针, 字符）
        for rr, cc in positions:  # for (rr, cc) in positions:
            if rr == r or abs(rr - r) == abs(
                cc - c
            ):  # 若 rr 等于 右指针 or 取绝对值 rr 减 右指针) 等于 取绝对值 cc 减 字符
                return False  # 返回 False
        return True  # 返回 True

    def solve(col):  # 定义函数 solve（参数：col）
        if col == 8:  # 若 col 等于 8
            solutions.append([p[0] for p in positions])  # 把 [节点[0] for 节点 in positions] 追加到列表尾部
            return  # return
        for r in range(8):  # 让 右指针 从 8 遍历
            if safe(r, col):  # 若 safe(右指针, col
                positions.append((r, col))  # 把 (右指针, col 追加到列表尾部
                solve(col + 1)  # solve(col 加 1)
                positions.pop()  # 弹出栈顶元素

    solve(0)  # solve(0)
    return solutions  # 返回 solutions


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    sols = n_queens_simple()  # 把 n_queens_simple() 存入 sols
    print("八皇后方案数:", len(sols))  # 打印输出
    print("第一个方案(列->行,0-indexed):", sols[0])  # 打印输出
