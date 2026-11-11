# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085409
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def heapify(arr, n, root):  # 定义函数 heapify（参数：数组, 元素个数, 根节点）
    """下沉操作：以 root 为根的子堆中，把最大值换到根。"""
    largest = root  # 把 根节点 存入 largest
    l = 2 * root + 1  # 把 2 乘 根节点 加 1 存入 左指针
    r = 2 * root + 2  # 把 2 乘 根节点 加 2 存入 右指针
    if l < n and arr[l] > arr[largest]:  # 若 左指针 小于 元素个数 and 数组[左指针] 超过 数组[largest]
        largest = l  # 把 左指针 存入 largest
    if r < n and arr[r] > arr[largest]:  # 若 右指针 小于 元素个数 and 数组[右指针] 超过 数组[largest]
        largest = r  # 把 右指针 存入 largest
    if largest != root:  # 若 largest 不等于 根节点
        arr[root], arr[largest] = (
            arr[largest],
            arr[root],
        )  # 把 数组[largest], 数组[根节点] 写入 arr[root], arr[largest]
        heapify(arr, n, largest)  # heapify(数组, 元素个数, largest)


def heap_sort(arr):  # 定义函数 heap_sort（参数：数组）
    """堆排序（升序）：先建最大堆，再反复把堆顶交换到末尾并下沉。"""
    a = arr[:]  # 把 复制 数组 存入 数组
    n = len(a)  # 把 长度(数组) 存入 元素个数
    for i in range(n // 2 - 1, -1, -1):  # 让 下标 i 从 元素个数 除以 除以 2 减 1 倒数回去（每步减 1）
        heapify(a, n, i)  # heapify(数组, 元素个数, 下标 i)
    for i in range(n - 1, 0, -1):  # 让 下标 i 从 元素个数 减 1 倒数回去（每步减 1）
        a[0], a[i] = a[i], a[0]  # 把 数组[下标 i], 数组[0] 写入 a[0], a[i]
        heapify(a, i, 0)  # heapify(数组, 下标 i, 0)
    return a  # 返回 数组


class MaxHeap:  # 定义类
    """最大堆：用于动态获取/删除最大值。"""

    def __init__(self):  # 构造函数：初始化成员
        self.data = []  # 把 [] 写入 self.data

    def push(self, val):  # 定义函数 push（参数：self, 值）
        self.data.append(val)  # 把 值 追加到列表尾部
        self._up(len(self.data) - 1)  # self._up(长度(self.data) 减 1)

    def pop(self):  # 定义函数 pop（参数：self）
        if not self.data:  # 若 not self.data
            return None  # 返回 None
        top = self.data[0]  # 把 self.data[0] 存入 top
        self.data[0] = self.data[-1]  # 把 self.data[ 减 1] 写入 self.data[0]
        self.data.pop()  # 弹出栈顶元素
        self._down(0)  # self._down(0)
        return top  # 返回 top

    def _up(self, i):  # 定义函数 _up（参数：self, 下标 i）
        while i > 0 and self.data[i] > self.data[(i - 1) // 2]:
            self.data[i], self.data[(i - 1) // 2] = self.data[(i - 1) // 2], self.data[i]
            i = (i - 1) // 2  # 把 (下标 i 减 1) 除以 除以 2 存入 下标 i

    def _down(self, i):  # 定义函数 _down（参数：self, 下标 i）
        n = len(self.data)  # 把 长度(self.data) 存入 元素个数
        while True:  # 循环，直到不满足「True」
            l, r, m = 2 * i + 1, 2 * i + 2, i  # 把 2 乘 下标 i 加 1, 2 乘 下标 i 加 2, 下标 i 写入 l, r, m
            if (
                l < n and self.data[l] > self.data[m]
            ):  # 若 左指针 小于 元素个数 and self.data[左指针] 超过 self.data[映射表]
                m = l  # 把 左指针 存入 映射表
            if (
                r < n and self.data[r] > self.data[m]
            ):  # 若 右指针 小于 元素个数 and self.data[右指针] 超过 self.data[映射表]
                m = r  # 把 右指针 存入 映射表
            if m == i:  # 若 映射表 等于 下标 i
                break  # 跳出循环
            self.data[i], self.data[m] = self.data[m], self.data[i]
            i = m  # 把 映射表 存入 下标 i


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print("heap sort:", heap_sort([12, 11, 13, 5, 6, 7]))  # 打印输出
    h = MaxHeap()  # 把 MaxHeap() 存入 h
    for v in [4, 1, 9, 3]:  # for 值 in [4, 1, 9, 3]:
        h.push(v)  # 把 值 压入栈/数组尾部
    print("max heap pops:", [h.pop() for _ in range(4)])  # 打印输出
