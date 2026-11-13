# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344649
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


class MinHeap:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆

    def size(self):  # 定义函数 size（参数：self）
        return len(self.heap)  # 返回 长度(self.堆)

    def peek(self):  # 定义函数 peek（参数：self）
        return self.heap[0] if self.heap else None  # 返回 self.堆[0] if self.堆 else None

    def insert(self, val):  # 定义函数 insert（参数：self, 值）
        heapq.heappush(self.heap, val)  # heapq.heappush(self.堆, 值)

    def pop(self):  # 定义函数 pop（参数：self）
        return heapq.heappop(self.heap)  # 返回 heapq.heappop(self.堆)


class MaxHeap:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆

    def size(self):  # 定义函数 size（参数：self）
        return len(self.heap)  # 返回 长度(self.堆)

    def peek(self):  # 定义函数 peek（参数：self）
        return -self.heap[0] if self.heap else None  # 返回 减 self.堆[0] if self.堆 else None

    def insert(self, val):  # 定义函数 insert（参数：self, 值）
        heapq.heappush(self.heap, -val)  # heapq.heappush(self.堆, 减 值)

    def pop(self):  # 定义函数 pop（参数：self）
        return -heapq.heappop(self.heap)  # 返回 减 heapq.heappop(self.堆)


class MedianFinder:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.maxHeap = MaxHeap()  # 把 MaxHeap() 写入 self.maxHeap
        self.minHeap = MinHeap()  # 把 MinHeap() 写入 self.minHeap

    def addNum(self, num):  # 定义函数 addNum（参数：self, num）
        if (
            self.maxHeap.size() == 0 or num <= self.maxHeap.peek()
        ):  # 若 self.maxHeap.大小() 等于 0 or num 不超过 self.maxHeap.peek(
            self.maxHeap.insert(num)  # self.maxHeap 插入 num)
        else:  # 否则
            self.minHeap.insert(num)  # self.minHeap 插入 num)
        if (
            self.maxHeap.size() > self.minHeap.size() + 1
        ):  # 若 self.maxHeap.大小() 超过 self.minHeap.大小() 加 1
            self.minHeap.insert(self.maxHeap.pop())  # 弹出栈顶元素
        elif (
            self.minHeap.size() > self.maxHeap.size()
        ):  # 否则，若 self.minHeap.大小() 超过 self.maxHeap.大小(
            self.maxHeap.insert(self.minHeap.pop())  # 弹出栈顶元素

    def findMedian(self):  # 定义函数 findMedian（参数：self）
        if self.maxHeap.size() == self.minHeap.size():  # 若 self.maxHeap.大小() 等于 self.minHeap.大小(
            return (
                self.maxHeap.peek() + self.minHeap.peek()
            ) / 2  # 返回 (self.maxHeap.peek() 加 self.minHeap.peek()) 除以 2
        return self.maxHeap.peek()  # 返回 self.maxHeap.peek()


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    mf = MedianFinder()  # 把 MedianFinder() 存入 mf
    for x in [1, 2, 3, 4, 5]:  # for x in [1, 2, 3, 4, 5]:
        mf.addNum(x)  # mf.addNum(x)
    print(mf.findMedian())  # 打印输出
