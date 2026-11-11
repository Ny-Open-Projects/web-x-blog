# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


class MinHeap:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆

    def size(self):  # 定义函数 size（参数：self）
        return len(self.heap)  # 返回 长度(self.堆)

    def peak(self):  # 定义函数 peak（参数：self）
        return self.heap[0]  # 返回 self.堆[0]

    def insert(self, val):  # 定义函数 insert（参数：self, 值）
        heapq.heappush(self.heap, val)  # heapq.heappush(self.堆, 值)

    def pop(self):  # 定义函数 pop（参数：self）
        return heapq.heappop(self.heap)  # 返回 heapq.heappop(self.堆)


def findKthLargest(nums, k):  # 定义函数 findKthLargest（参数：数组, 下标 k）
    h = MinHeap()  # 把 MinHeap() 存入 h
    for n in nums:  # 逐个取出 数组 的元素（元素个数）
        h.insert(n)  # h 插入 元素个数)
        if h.size() > k:  # 若 h.大小() 超过 下标 k
            h.pop()  # 弹出栈顶元素
    return h.peak()  # 返回 h.peak()


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 打印输出
    print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 打印输出
