# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fib_recursive(n):  # 定义函数 fib_recursive（参数：元素个数）
    # 递归斐波那契：时间复杂度 O(2^n)，指数级
    if n < 2:  # 若 元素个数 小于 2
        return n  # 返回 元素个数
    return fib_recursive(n - 1) + fib_recursive(
        n - 2
    )  # 返回 fib_recursive(元素个数 减 1) 加 fib_recursive(元素个数 减 2)


def fib_iterative(n):  # 定义函数 fib_iterative（参数：元素个数）
    # 迭代/动态规划斐波那契：时间复杂度 O(n)
    if n < 2:  # 若 元素个数 小于 2
        return n  # 返回 元素个数
    a, b = 0, 1  # 把 0, 1 写入 a, b
    for _ in range(2, n + 1):  # 让 _ 从 2 到 元素个数 加 1 遍历
        a, b = b, a + b  # 把 b, 数组 加 b 写入 a, b
    return b  # 返回 b


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fib_recursive(10))  # 55
    print(fib_iterative(10))  # 55
