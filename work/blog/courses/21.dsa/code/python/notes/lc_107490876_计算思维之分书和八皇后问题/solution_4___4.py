# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def n_queens_stack():  # 定义函数 n_queens_stack（参数：无）
    """八皇后问题（栈/迭代回溯）：用显式栈代替递归，按列放置皇后并通过 valid 检查安全性。"""

    def valid(x, a):  # 定义函数 valid（参数：x, 数组）
        y = len(a) + 1  # 把 长度(数组) 加 1 存入 y
        for i in range(1, y):  # 让 下标 i 从 1 到 y 遍历
            if x == a[i - 1] or abs(y - i) == abs(x - a[i - 1]):
                return False  # 返回 False
        return True  # 返回 True

    solutions = []  # 把 [] 存入 solutions
    stack = [[]]  # 把 [[]] 存入 栈
    while stack:  # 循环，直到不满足「栈」
        a = stack.pop()  # 把 栈 弹出 ) 存入 数组
        if len(a) == 8:  # 若 长度(数组) 等于 8
            solutions.append(a)  # 把 数组 追加到列表尾部
        else:  # 否则
            for i in range(1, 9):  # 让 下标 i 从 1 到 9 遍历
                if valid(i, a):  # 若 valid(下标 i, 数组
                    stack.append(a + [i])  # 注意：是追加新元素，不是拼接 a[i]
    return solutions  # 返回 solutions


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    sols = n_queens_stack()  # 把 n_queens_stack() 存入 sols
    print("八皇后方案数:", len(sols))  # 打印输出
    print("第一个方案(列->行):", sols[0])  # 打印输出
