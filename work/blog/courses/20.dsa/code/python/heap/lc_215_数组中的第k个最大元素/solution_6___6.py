# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
# 数组中的第 K 个最大元素 - 方案: 大小为 k 的小顶堆
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


def find_kth_largest(nums, k):  # 定义函数 find_kth_largest（参数：数组, 下标 k）
    heap = []  # 把 [] 存入 堆
    for x in nums:  # 逐个取出 数组 的元素（x）
        heapq.heappush(heap, x)  # heapq.heappush(堆, x)
        if len(heap) > k:  # 若 长度(堆) 超过 下标 k
            heapq.heappop(heap)  # heapq.heappop(堆)
    return heap[0]  # 返回 堆[0]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
