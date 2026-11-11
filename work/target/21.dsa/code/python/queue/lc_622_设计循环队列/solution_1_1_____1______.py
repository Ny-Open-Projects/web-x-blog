# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class MyCircularQueue:  # 定义类
    def __init__(self, k: int):  # 构造函数：初始化成员
        self.capacity = k  # 把 下标 k 写入 self.capacity
        self.data = [0] * k  # 把 [0] 乘 下标 k 写入 self.data
        self.front = 0  # 把 0 写入 self.front
        self.rear = 0  # 把 0 写入 self.rear
        self.size = 0  # 把 0 写入 大小

    def enQueue(self, value: int) -> bool:  # 定义函数 enQueue（参数：self, value: int）
        if self.isFull():  # 若 self.isFull(
            return False  # 返回 False
        self.data[self.rear] = value  # 把 value 写入 self.data[self.rear]
        self.rear = (
            self.rear + 1
        ) % self.capacity  # 把 (self.rear 加 1) 对…取模 self.capacity 写入 self.rear
        self.size += 1  # self.size累加 1
        return True  # 返回 True

    def deQueue(self) -> bool:  # 定义函数 deQueue（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return False  # 返回 False
        self.front = (
            self.front + 1
        ) % self.capacity  # 把 (self.front 加 1) 对…取模 self.capacity 写入 self.front
        self.size -= 1  # self.size累减 1
        return True  # 返回 True

    def Front(self) -> int:  # 定义函数 Front（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return -1  # 返回 减 1
        return self.data[self.front]  # 返回 self.data[self.front]

    def Rear(self) -> int:  # 定义函数 Rear（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return -1  # 返回 减 1
        return self.data[
            (self.rear - 1) % self.capacity
        ]  # 返回 self.data[(self.rear 减 1) 对…取模 self.capacity]

    def isEmpty(self) -> bool:  # 定义函数 isEmpty（参数：self）
        return self.size == 0  # 返回 self.大小 等于 0

    def isFull(self) -> bool:  # 定义函数 isFull（参数：self）
        return self.size == self.capacity  # 返回 self.大小 等于 self.capacity


def solution():  # 定义函数 solution（参数：无）
    q = MyCircularQueue(3)  # 把 MyCircularQueue(3) 存入 节点
    results = []  # 把 [] 存入 results
    results.append(q.enQueue(1))  # 把 节点.enQueue(1 追加到列表尾部
    results.append(q.enQueue(2))  # 把 节点.enQueue(2 追加到列表尾部
    results.append(q.enQueue(3))  # 把 节点.enQueue(3 追加到列表尾部
    results.append(q.enQueue(4))  # 把 节点.enQueue(4 追加到列表尾部
    results.append(q.Rear())  # 把 节点.Rear( 追加到列表尾部
    results.append(q.isFull())  # 把 节点.isFull( 追加到列表尾部
    results.append(q.deQueue())  # 把 节点.deQueue( 追加到列表尾部
    results.append(q.enQueue(4))  # 把 节点.enQueue(4 追加到列表尾部
    results.append(q.Rear())  # 把 节点.Rear( 追加到列表尾部
    return results  # 返回 results


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(solution())  # 打印输出
