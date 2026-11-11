# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import Counter  # from collections import Counter


def leastInterval(tasks, n):  # 定义函数 leastInterval（参数：tasks, 元素个数）
    # 公式法（显式统计）：以任务频率桶实现
    freq = [0] * 26  # 把 [0] 乘 26 存入 频次表
    for t in tasks:  # 逐个取出 tasks 的元素（另一字符串）
        freq[ord(t) - ord("A")] += 1  # 把 1 写入 freq[ord(t) - ord('A')] +
    max_freq = max(freq)  # 把 取较大值 频次表) 存入 max_freq
    same = sum(1 for f in freq if f == max_freq)  # 把 累计和(1 for f in 频次表 if f 等于 max_freq) 存入 same
    return max(
        (max_freq - 1) * (n + 1) + same, len(tasks)
    )  # 返回 取较大值 (max_freq 减 1) 乘 (元素个数 加 1) 加 same, 长度(tasks))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # 打印输出
