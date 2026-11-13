# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


class MinHeap:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆

    def size(self):  # 定义函数 size（参数：self）
        return len(self.heap)  # 返回 长度(self.堆)

    def insert(self, value, key):  # 定义函数 insert（参数：self, value, key）
        heapq.heappush(self.heap, (value, key))  # heapq.heappush(self.堆, (value, key))

    def pop(self):  # 定义函数 pop（参数：self）
        return heapq.heappop(self.heap)  # 返回 heapq.heappop(self.堆)


def topKFrequent(nums, k):  # 定义函数 topKFrequent（参数：数组, 下标 k）
    map = {}  # 把 {} 存入 映射表
    for n in nums:  # 逐个取出 数组 的元素（元素个数）
        map[n] = map.get(n, 0) + 1  # 把 映射表 查找 元素个数, 0) 加 1 写入 map[n]
    h = MinHeap()  # 把 MinHeap() 存入 h
    for key, value in map.items():  # for key, value in 映射表.items():
        h.insert(value, key)  # h 插入 value, key)
        if h.size() > k:  # 若 h.大小() 超过 下标 k
            h.pop()  # 弹出栈顶元素
    return [item[1] for item in h.heap]  # 返回 [item[1] for item in h.堆]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2] in any order
