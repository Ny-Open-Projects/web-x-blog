# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import Counter  # from collections import Counter


def leastInterval(tasks, n):  # 定义函数 leastInterval（参数：tasks, 元素个数）
    # 公式法（另一写法）
    cnt = list(Counter(tasks).values())  # 把 列表(Counter(tasks).values()) 存入 计数
    freq = max(cnt)  # 把 取较大值 计数) 存入 频次表
    same = cnt.count(freq)  # 把 计数.计数(频次表) 存入 same
    return max(
        (freq - 1) * (n + 1) + same, len(tasks)
    )  # 返回 取较大值 (频次表 减 1) 乘 (元素个数 加 1) 加 same, 长度(tasks))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # 打印输出
