# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖
from collections import Counter  # from collections import Counter


def topKFrequent(nums, k):  # 定义函数 topKFrequent（参数：数组, 下标 k）
    freq = Counter(nums)  # 把 Counter(数组) 存入 频次表
    # 维护一个大小为 k 的最小堆，堆顶是堆中频次最小的元素
    heap = []  # 把 [] 存入 堆
    for num, cnt in freq.items():  # for num, 计数 in 频次表.items():
        heapq.heappush(heap, (cnt, num))  # heapq.heappush(堆, (计数, num))
        if len(heap) > k:  # 若 长度(堆) 超过 下标 k
            heapq.heappop(heap)  # heapq.heappop(堆)
    # 取出堆中剩下的元素（频次最高的 k 个），顺序任意
    return [num for _, num in heap]  # 返回 [num for _, num in 堆]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sorted(topKFrequent([1, 1, 1, 2, 2, 3], 2)))  # 打印输出
