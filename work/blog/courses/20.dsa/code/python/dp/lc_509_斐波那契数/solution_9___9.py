# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fib(n):  # 定义函数 fib（参数：元素个数）
    # 两变量滚动（从 0 开始迭代 n 次）
    a, b = 0, 1  # 把 0, 1 写入 a, b
    for _ in range(n):  # 让 _ 从 元素个数 遍历
        a, b = b, a + b  # 把 b, 数组 加 b 写入 a, b
    return a  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fib(5))  # 打印输出
