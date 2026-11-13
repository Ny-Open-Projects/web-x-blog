# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fib(n):  # 定义函数 fib（参数：元素个数）
    if n == 0:
        return 0  # 若 元素个数 等于 0: return 0
    if n == 1:
        return 1  # 若 元素个数 等于 1: return 1
    return fib(n - 1) + fib(n - 2)  # 返回 fib(元素个数 减 1) 加 fib(元素个数 减 2)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fib(1))  # 打印输出
