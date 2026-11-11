# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385578
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Node:  # 定义类
    def __init__(self, value):  # 构造函数：初始化成员
        self.val = value  # 把 value 写入 值
        self.prev = None  # 把 None 写入 前一个
        self.next = None  # 把 None 写入 下一个


class MyCircularDeque:  # 定义类
    def __init__(self, k: int):  # 构造函数：初始化成员
        self.head = None  # 把 None 写入 头节点
        self.tail = None  # 把 None 写入 尾节点
        self.capacity = k  # 把 下标 k 写入 self.capacity
        self.size = 0  # 把 0 写入 大小

    def insertFront(self, value: int) -> bool:  # 定义函数 insertFront（参数：self, value: int）
        if self.isFull():  # 若 self.isFull(
            return False  # 返回 False
        new_node = Node(value)  # 把 Node(value) 存入 new_node
        if self.isEmpty():  # 若 self.isEmpty(
            self.head = new_node  # 把 new_node 写入 头节点
            self.tail = new_node  # 把 new_node 写入 尾节点
        else:  # 否则
            new_node.next = self.head  # 把 self.头节点 写入 下一个
            if self.head:  # 若 self.头节点
                self.head.prev = new_node  # 把 new_node 写入 前一个
            self.head = new_node  # 把 new_node 写入 头节点
        self.size += 1  # self.size累加 1
        return True  # 返回 True

    def insertLast(self, value: int) -> bool:  # 定义函数 insertLast（参数：self, value: int）
        if self.isFull():  # 若 self.isFull(
            return False  # 返回 False
        new_node = Node(value)  # 把 Node(value) 存入 new_node
        if self.isEmpty():  # 若 self.isEmpty(
            self.head = new_node  # 把 new_node 写入 头节点
            self.tail = new_node  # 把 new_node 写入 尾节点
        else:  # 否则
            if self.tail:  # 若 self.尾节点
                self.tail.next = new_node  # 把 new_node 写入 下一个
                new_node.prev = self.tail  # 把 self.尾节点 写入 前一个
            self.tail = new_node  # 把 new_node 写入 尾节点
        self.size += 1  # self.size累加 1
        return True  # 返回 True

    def deleteFront(self) -> bool:  # 定义函数 deleteFront（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return False  # 返回 False
        if self.head:  # 若 self.头节点
            self.head = self.head.next  # 把 self.头节点.下一个 写入 头节点
            if self.head:  # 若 self.头节点
                self.head.prev = None  # 把 None 写入 前一个
            else:  # 否则
                self.tail = None  # 把 None 写入 尾节点
        self.size -= 1  # self.size累减 1
        return True  # 返回 True

    def deleteLast(self) -> bool:  # 定义函数 deleteLast（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return False  # 返回 False
        if self.tail:  # 若 self.尾节点
            self.tail = self.tail.prev  # 把 self.尾节点.前一个 写入 尾节点
            if self.tail:  # 若 self.尾节点
                self.tail.next = None  # 把 None 写入 下一个
            else:  # 否则
                self.head = None  # 把 None 写入 头节点
        self.size -= 1  # self.size累减 1
        return True  # 返回 True

    def getFront(self) -> int:  # 定义函数 getFront（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return -1  # 返回 减 1
        return self.head.val if self.head else -1  # 返回 self.头节点.值 if self.头节点 else 减 1

    def getRear(self) -> int:  # 定义函数 getRear（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return -1  # 返回 减 1
        return self.tail.val if self.tail else -1  # 返回 self.尾节点.值 if self.尾节点 else 减 1

    def isEmpty(self) -> bool:  # 定义函数 isEmpty（参数：self）
        return self.size == 0  # 返回 self.大小 等于 0

    def isFull(self) -> bool:  # 定义函数 isFull（参数：self）
        return self.size == self.capacity  # 返回 self.大小 等于 self.capacity


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    obj = MyCircularDeque(3)  # 把 MyCircularDeque(3) 存入 obj
    print(obj.insertLast(1))  # True
    print(obj.insertLast(2))  # True
    print(obj.insertFront(3))  # True
    print(obj.insertFront(4))  # False (full)
    print(obj.getRear())  # 2
    print(obj.isFull())  # True
    print(obj.deleteLast())  # True
    print(obj.insertFront(4))  # True
    print(obj.getFront())  # 4
