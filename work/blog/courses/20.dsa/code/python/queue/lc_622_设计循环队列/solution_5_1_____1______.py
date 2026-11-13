# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class MyCircularQueue:  # 定义类
    # 用数组 + front/rear 指针 + size 记录元素个数，避免空/满歧义
    def __init__(self, k):  # 构造函数：初始化成员
        self.queue = [-1] * k  # 把 [ 减 1] 乘 下标 k 写入 队列
        self.front = 0  # 把 0 写入 self.front
        self.rear = -1  # 把 减 1 写入 self.rear
        self.size = 0  # 把 0 写入 大小
        self.capacity = k  # 把 下标 k 写入 self.capacity

    def enQueue(self, value):  # 定义函数 enQueue（参数：self, value）
        if self.isFull():  # 若 self.isFull(
            return False  # 返回 False
        self.rear = (
            self.rear + 1
        ) % self.capacity  # 把 (self.rear 加 1) 对…取模 self.capacity 写入 self.rear
        self.queue[self.rear] = value  # 把 value 写入 self.queue[self.rear]
        self.size += 1  # self.size累加 1
        return True  # 返回 True

    def deQueue(self):  # 定义函数 deQueue（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return False  # 返回 False
        self.front = (
            self.front + 1
        ) % self.capacity  # 把 (self.front 加 1) 对…取模 self.capacity 写入 self.front
        self.size -= 1  # self.size累减 1
        return True  # 返回 True

    def Front(self):  # 定义函数 Front（参数：self）
        return (
            -1 if self.isEmpty() else self.queue[self.front]
        )  # 返回 减 1 if self.isEmpty() else self.队列[self.front]

    def Rear(self):  # 定义函数 Rear（参数：self）
        return (
            -1 if self.isEmpty() else self.queue[self.rear]
        )  # 返回 减 1 if self.isEmpty() else self.队列[self.rear]

    def isEmpty(self):  # 定义函数 isEmpty（参数：self）
        return self.size == 0  # 返回 self.大小 等于 0

    def isFull(self):  # 定义函数 isFull（参数：self）
        return self.size == self.capacity  # 返回 self.大小 等于 self.capacity


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    q = MyCircularQueue(3)  # 把 MyCircularQueue(3) 存入 节点
    print(q.enQueue(1))  # 打印输出
    print(q.enQueue(2))  # 打印输出
    print(q.Rear())  # 打印输出
    print(q.deQueue())  # 打印输出
    print(q.Front())  # 打印输出
