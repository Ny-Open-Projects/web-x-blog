# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class MaxHeap:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆

    @staticmethod  # @staticmethod
    def swap(arr, i, j):  # 定义函数 swap（参数：数组, 下标 i, 下标 j）
        if i == j:  # 若 下标 i 等于 下标 j
            return  # return
        arr[i], arr[j] = arr[j], arr[i]  # 把 数组[下标 j], 数组[下标 i] 写入 arr[i], arr[j]

    @staticmethod  # @staticmethod
    def max_heapify(arr, i, size):  # 定义函数 max_heapify（参数：数组, 下标 i, 大小）
        l = (i << 1) + 1  # 把 (下标 i 小于 小于 1) 加 1 存入 左指针
        r = (i << 1) + 2  # 把 (下标 i 小于 小于 1) 加 2 存入 右指针
        largest = i  # 把 下标 i 存入 largest
        if l < size and arr[l] > arr[largest]:  # 若 左指针 小于 大小 and 数组[左指针] 超过 数组[largest]
            largest = l  # 把 左指针 存入 largest
        if r < size and arr[r] > arr[largest]:  # 若 右指针 小于 大小 and 数组[右指针] 超过 数组[largest]
            largest = r  # 把 右指针 存入 largest
        if largest != i:  # 若 largest 不等于 下标 i
            MaxHeap.swap(arr, i, largest)  # MaxHeap.交换 数组, 下标 i, largest)
            MaxHeap.max_heapify(arr, largest, size)  # MaxHeap.max_heapify(数组, largest, 大小)

    def sort(self):  # 定义函数 sort（参数：self）
        i_arr = self.heap  # 把 self.堆 存入 i_arr
        n = len(i_arr)  # 把 长度(i_arr) 存入 元素个数
        if n <= 1:  # 若 元素个数 不超过 1
            return i_arr  # 返回 i_arr
        for i in range(n // 2 - 1, -1, -1):  # 让 下标 i 从 元素个数 除以 除以 2 减 1 倒数回去（每步减 1）
            MaxHeap.max_heapify(i_arr, i, n)  # MaxHeap.max_heapify(i_arr, 下标 i, 元素个数)
        for j in range(n - 1):  # 让 下标 j 从 元素个数 减 1 遍历
            MaxHeap.swap(i_arr, 0, n - 1 - j)  # MaxHeap.交换 i_arr, 0, 元素个数 减 1 减 下标 j)
            MaxHeap.max_heapify(
                i_arr, 0, n - 1 - j - 1
            )  # MaxHeap.max_heapify(i_arr, 0, 元素个数 减 1 减 下标 j 减 1)
        return i_arr  # 返回 i_arr


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    mh = MaxHeap()  # 把 MaxHeap() 存入 mh
    mh.heap = [
        1,
        10,
        9,
        5,
        3,
        11,
        3,
        9,
        11,
        13,
        1,
        -1,
        98,
    ]  # 把 [1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, 减 1, 98] 写入 堆
    print(mh.sort())  # 打印输出
