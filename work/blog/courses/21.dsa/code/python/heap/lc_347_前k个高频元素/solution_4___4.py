# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖
from collections import Counter  # from collections import Counter


def topKFrequent(nums, k):  # 定义函数 topKFrequent（参数：数组, 下标 k）
    freq = Counter(nums)  # 把 Counter(数组) 存入 频次表
    # 直接取频次最高的 k 个元素
    return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sorted(topKFrequent([1, 1, 1, 2, 2, 3], 2)))  # 打印输出
