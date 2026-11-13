# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fib(n):  # 定义函数 fib（参数：元素个数）
    # 两个变量滚动迭代
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    if n == 1:  # 若 元素个数 等于 1
        return 1  # 返回 1
    start, end = 0, 1  # 把 0, 1 写入 start, end
    for _ in range(2, n + 1):  # 让 _ 从 2 到 元素个数 加 1 遍历
        start, end = end, start + end  # 把 终点, 起点 加 终点 写入 start, end
    return end  # 返回 终点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fib(5))  # 打印输出
