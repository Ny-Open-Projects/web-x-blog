# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
# Fibonacci - 带记忆化 (Memoization)
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fibonacci(n, memo=None):  # 定义函数 fibonacci（参数：元素个数, 记忆化表 赋值为 None）
    if memo is None:  # 若 记忆化表 is None
        memo = {}  # 把 {} 存入 记忆化表
    if n <= 1:  # 若 元素个数 不超过 1
        return n  # 返回 元素个数
    if n in memo:  # 若 元素个数 in 记忆化表
        return memo[n]  # 返回 记忆化表[元素个数]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]  # 返回 记忆化表[元素个数]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fibonacci(10))  # 55
