# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344649
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


class Heap:  # 定义类
    def __init__(self, compare_fn):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆
        self.compare_fn = compare_fn  # 把 compare_fn 写入 self.compare_fn

    def size(self):  # 定义函数 size（参数：self）
        return len(self.heap)  # 返回 长度(self.堆)

    def peek(self):  # 定义函数 peek（参数：self）
        return self.heap[0] if self.heap else None  # 返回 self.堆[0] if self.堆 else None

    def insert(self, value):  # 定义函数 insert（参数：self, value）
        self.heap.append(value)  # 把 value 追加到列表尾部
        self._shift_up(len(self.heap) - 1)  # self._shift_up(长度(self.堆) 减 1)

    def pop(self):  # 定义函数 pop（参数：self）
        if len(self.heap) == 1:  # 若 长度(self.堆) 等于 1
            return self.heap.pop()  # 返回 self.堆 弹出 )
        first = self.heap[0]  # 把 self.堆[0] 存入 first
        self.heap[0] = self.heap.pop()  # 弹出栈顶元素
        self._shift_down(0)  # self._shift_down(0)
        return first  # 返回 first

    def _shift_up(self, i):  # 定义函数 _shift_up（参数：self, 下标 i）
        while i > 0 and self.compare_fn(self.heap[(i - 1) >> 1], self.heap[i]):
            self.heap[(i - 1) >> 1], self.heap[i] = self.heap[i], self.heap[(i - 1) >> 1]
            i = (i - 1) >> 1  # 把 (下标 i 减 1) 超过 超过 1 存入 下标 i

    def _shift_down(self, pi):  # 定义函数 _shift_down（参数：self, pi）
        size = len(self.heap)  # 把 长度(self.堆) 存入 大小
        left = 2 * pi + 1  # 把 2 乘 pi 加 1 存入 左边界
        right = 2 * pi + 2  # 把 2 乘 pi 加 2 存入 右边界
        largest = pi  # 把 pi 存入 largest
        if left < size and self.compare_fn(
            self.heap[largest], self.heap[left]
        ):  # 若 左边界 小于 大小 and self.compare_fn(self.堆[largest], self.堆[左边界]
            largest = left  # 把 左边界 存入 largest
        if right < size and self.compare_fn(
            self.heap[largest], self.heap[right]
        ):  # 若 右边界 小于 大小 and self.compare_fn(self.堆[largest], self.堆[右边界]
            largest = right  # 把 右边界 存入 largest
        if largest != pi:  # 若 largest 不等于 pi
            self.heap[pi], self.heap[largest] = self.heap[largest], self.heap[pi]
            self._shift_down(largest)  # self._shift_down(largest)


class MinHeap(Heap):  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        super().__init__(lambda a, b: a > b)  # super().__init__(lambda 数组, b: 数组 超过 b)


class MaxHeap(Heap):  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        super().__init__(lambda a, b: a < b)  # super().__init__(lambda 数组, b: 数组 小于 b)


class MedianFinder:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.minHeap = MinHeap()  # 把 MinHeap() 写入 self.minHeap
        self.maxHeap = MaxHeap()  # 把 MaxHeap() 写入 self.maxHeap

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
