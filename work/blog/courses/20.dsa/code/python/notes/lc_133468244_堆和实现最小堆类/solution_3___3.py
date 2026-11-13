# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468244
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class MinHeap:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆

    def get_parent_index(self, i):  # 定义函数 get_parent_index（参数：self, 下标 i）
        return (i - 1) >> 1  # 返回 (下标 i 减 1) 超过 超过 1

    def get_left_index(self, i):  # 定义函数 get_left_index（参数：self, 下标 i）
        return (i << 1) + 1  # 返回 (下标 i 小于 小于 1) 加 1

    def get_right_index(self, i):  # 定义函数 get_right_index（参数：self, 下标 i）
        return (i << 1) + 2  # 返回 (下标 i 小于 小于 1) 加 2

    def swap(self, i, j):  # 定义函数 swap（参数：self, 下标 i, 下标 j）
        self.heap[i], self.heap[j] = (
            self.heap[j],
            self.heap[i],
        )  # 把 self.堆[下标 j], self.堆[下标 i] 写入 self.heap[i], self.heap[j]

    def shift_up(self, i):  # 定义函数 shift_up（参数：self, 下标 i）
        if i == 0:  # 若 下标 i 等于 0
            return  # return
        pi = self.get_parent_index(i)  # 把 self.get_parent_index(下标 i) 存入 pi
        if self.heap[pi] > self.heap[i]:  # 若 self.堆[pi] 超过 self.堆[下标 i]
            self.swap(pi, i)  # self.交换 pi, 下标 i)
            self.shift_up(pi)  # self.shift_up(pi)

    def shift_down(self, i):  # 定义函数 shift_down（参数：self, 下标 i）
        size = self.size()  # 把 self.大小() 存入 大小
        li = self.get_left_index(i)  # 把 self.get_left_index(下标 i) 存入 li
        ri = self.get_right_index(i)  # 把 self.get_right_index(下标 i) 存入 ri
        cur = self.heap[i]  # 把 self.堆[下标 i] 存入 当前值
        smallest = i  # 把 下标 i 存入 smallest
        if li < size and self.heap[li] < cur:  # 若 li 小于 大小 and self.堆[li] 小于 当前值
            smallest = li  # 把 li 存入 smallest
        if (
            ri < size and self.heap[ri] < self.heap[smallest]
        ):  # 若 ri 小于 大小 and self.堆[ri] 小于 self.堆[smallest]
            smallest = ri  # 把 ri 存入 smallest
        if smallest != i:  # 若 smallest 不等于 下标 i
            self.swap(smallest, i)  # self.交换 smallest, 下标 i)
            self.shift_down(smallest)  # self.shift_down(smallest)

    def insert(self, value):  # 定义函数 insert（参数：self, value）
        self.heap.append(value)  # 把 value 追加到列表尾部
        self.shift_up(len(self.heap) - 1)  # self.shift_up(长度(self.堆) 减 1)

    def pop(self):  # 定义函数 pop（参数：self）
        if self.size() == 0:  # 若 self.大小() 等于 0
            return  # return
        self.heap[0] = self.heap.pop()  # 弹出栈顶元素
        self.shift_down(0)  # self.shift_down(0)

    def peak(self):  # 定义函数 peak（参数：self）
        if self.size() == 0:  # 若 self.大小() 等于 0
            return None  # 返回 None
        return self.heap[0]  # 返回 self.堆[0]

    def size(self):  # 定义函数 size（参数：self）
        return len(self.heap)  # 返回 长度(self.堆)

    def print_heap(self):  # 定义函数 print_heap（参数：self）
        print(self.heap)  # 打印输出


def main():  # 定义函数 main（参数：无）
    heap = MinHeap()  # 把 MinHeap() 存入 堆
    heap.insert(3)  # 堆 插入 3)
    heap.insert(1)  # 堆 插入 1)
    heap.insert(6)  # 堆 插入 6)
    heap.insert(5)  # 堆 插入 5)
    heap.insert(2)  # 堆 插入 2)
    heap.insert(4)  # 堆 插入 4)
    print("After insertions:")  # 打印输出
    heap.print_heap()  # 堆.print_heap()
    print("Peek:", heap.peak())  # 打印输出
    heap.pop()  # 弹出栈顶元素
    print("After pop:")  # 打印输出
    heap.print_heap()  # 堆.print_heap()
    heap.pop()  # 弹出栈顶元素
    print("After another pop:")  # 打印输出
    heap.print_heap()  # 堆.print_heap()
    print("Size:", heap.size())  # 打印输出
    empty_heap = MinHeap()  # 把 MinHeap() 存入 empty_heap
    print("Empty heap peek:", empty_heap.peak())  # 打印输出
    empty_heap.pop()  # 弹出栈顶元素
    print("Empty heap size after pop:", empty_heap.size())  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    main()  # main()
