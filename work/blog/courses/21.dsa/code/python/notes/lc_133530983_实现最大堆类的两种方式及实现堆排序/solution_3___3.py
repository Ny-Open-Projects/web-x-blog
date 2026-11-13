# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class MaxHeap:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆

    def swap(self, i, j):  # 定义函数 swap（参数：self, 下标 i, 下标 j）
        self.heap[i], self.heap[j] = (
            self.heap[j],
            self.heap[i],
        )  # 把 self.堆[下标 j], self.堆[下标 i] 写入 self.heap[i], self.heap[j]

    def get_parent_index(self, i):  # 定义函数 get_parent_index（参数：self, 下标 i）
        return (i - 1) >> 1  # 返回 (下标 i 减 1) 超过 超过 1

    def get_left_index(self, i):  # 定义函数 get_left_index（参数：self, 下标 i）
        return (i << 1) + 1  # 返回 (下标 i 小于 小于 1) 加 1

    def get_right_index(self, i):  # 定义函数 get_right_index（参数：self, 下标 i）
        return (i << 1) + 2  # 返回 (下标 i 小于 小于 1) 加 2

    def shift_up(self, index):  # 定义函数 shift_up（参数：self, index）
        if index == 0:  # 若 index 等于 0
            return  # return
        parent_index = self.get_parent_index(index)  # 把 self.get_parent_index(index) 存入 parent_index
        if self.heap[parent_index] < self.heap[index]:  # 若 self.堆[parent_index] 小于 self.堆[index]
            self.swap(parent_index, index)  # self.交换 parent_index, index)
            self.shift_up(parent_index)  # self.shift_up(parent_index)

    def shift_down(self, index):  # 定义函数 shift_down（参数：self, index）
        if index >= len(self.heap) - 1:  # 若 index 不低于 长度(self.堆) 减 1
            return  # return
        size = self.size()  # 把 self.大小() 存入 大小
        left_index = self.get_left_index(index)  # 把 self.get_left_index(index) 存入 left_index
        right_index = self.get_right_index(index)  # 把 self.get_right_index(index) 存入 right_index
        if (
            left_index < size and self.heap[left_index] > self.heap[index]
        ):  # 若 left_index 小于 大小 and self.堆[left_index] 超过 self.堆[index]
            self.swap(left_index, index)  # self.交换 left_index, index)
            self.shift_down(left_index)  # self.shift_down(left_index)
        if (
            right_index < size and self.heap[right_index] > self.heap[index]
        ):  # 若 right_index 小于 大小 and self.堆[right_index] 超过 self.堆[index]
            self.swap(right_index, index)  # self.交换 right_index, index)
            self.shift_down(right_index)  # self.shift_down(right_index)

    def insert(self, value):  # 定义函数 insert（参数：self, value）
        self.heap.append(value)  # 把 value 追加到列表尾部
        self.shift_up(len(self.heap) - 1)  # self.shift_up(长度(self.堆) 减 1)

    def pop(self):  # 定义函数 pop（参数：self）
        if len(self.heap) <= 1:  # 若 长度(self.堆) 不超过 1
            return  # return
        self.heap[0] = self.heap.pop()  # 弹出栈顶元素
        self.shift_down(0)  # self.shift_down(0)

    def peak(self):  # 定义函数 peak（参数：self）
        return self.heap[0] if self.heap else None  # 返回 self.堆[0] if self.堆 else None

    def size(self):  # 定义函数 size（参数：self）
        return len(self.heap)  # 返回 长度(self.堆)

    def sort(self, arr):  # 定义函数 sort（参数：self, 数组）
        for n in arr:  # 逐个取出 数组 的元素（元素个数）
            self.insert(n)  # self 插入 元素个数)
        result = []  # 把 [] 存入 结果
        while self.size() > 1:  # 循环，直到不满足「self.大小() 超过 1」
            result.append(self.peak())  # 把 self.peak( 追加到列表尾部
            self.pop()  # 弹出栈顶元素
        result.append(self.peak())  # 把 self.peak( 追加到列表尾部
        self.heap = result  # 把 结果 写入 堆
        return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    mh = MaxHeap()  # 把 MaxHeap() 存入 mh
    sorted_array = mh.sort([1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98])
    print(sorted_array)  # 打印输出
