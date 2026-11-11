# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import Counter  # from collections import Counter


def leastInterval(tasks, n):  # 定义函数 leastInterval（参数：tasks, 元素个数）
    # 公式法：出现最多的任务 freq 个，有 same 个并列最多，
    # 最少时间 = (freq-1)*(n+1) + same，且不能少于任务总数
    cnt = Counter(tasks)  # 把 Counter(tasks) 存入 计数
    freq = max(cnt.values())  # 把 取较大值 计数.values()) 存入 频次表
    same = sum(
        1 for v in cnt.values() if v == freq
    )  # 把 累计和(1 for 值 in 计数.values() if 值 等于 频次表) 存入 same
    return max(
        (freq - 1) * (n + 1) + same, len(tasks)
    )  # 返回 取较大值 (频次表 减 1) 乘 (元素个数 加 1) 加 same, 长度(tasks))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # 打印输出
