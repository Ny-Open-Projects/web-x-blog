# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
# 前 K 个高频元素 - 方案: 大小为 k 的小顶堆
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖
from collections import Counter  # from collections import Counter


def top_k_frequent(nums, k):  # 定义函数 top_k_frequent（参数：数组, 下标 k）
    cnt = Counter(nums)  # 把 Counter(数组) 存入 计数
    heap = []  # 把 [] 存入 堆
    for num, freq in cnt.items():  # for num, 频次表 in 计数.items():
        heapq.heappush(heap, (freq, num))  # heapq.heappush(堆, (频次表, num))
        if len(heap) > k:  # 若 长度(堆) 超过 下标 k
            heapq.heappop(heap)  # heapq.heappop(堆)
    return [num for _, num in heap]  # 返回 [num for _, num in 堆]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
