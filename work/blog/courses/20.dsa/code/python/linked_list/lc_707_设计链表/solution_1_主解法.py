# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347892
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Node:  # 定义类
    def __init__(self, val=0):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.prev = None  # 把 None 写入 前一个
        self.next = None  # 把 None 写入 下一个


class MyLinkedList:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.head = None  # 把 None 写入 头节点
        self.tail = None  # 把 None 写入 尾节点
        self.size = 0  # 把 0 写入 大小

    def get(self, index: int) -> int:  # 定义函数 get（参数：self, index: int）
        if index < 0 or index >= self.size:  # 若 index 小于 0 or index 不低于 self.大小
            return -1  # 返回 减 1
        curr = self.head  # 把 self.头节点 存入 当前值
        for _ in range(index):  # 让 _ 从 index 遍历
            curr = curr.next  # 把 当前值.下一个 存入 当前值
        return curr.val  # 返回 当前值.值

    def addAtHead(self, val: int) -> None:  # 定义函数 addAtHead（参数：self, 值: int）
        new_node = Node(val)  # 把 Node(值) 存入 new_node
        new_node.next = self.head  # 把 self.头节点 写入 下一个
        if self.head:  # 若 self.头节点
            self.head.prev = new_node  # 把 new_node 写入 前一个
        else:  # 否则
            self.tail = new_node  # 把 new_node 写入 尾节点
        self.head = new_node  # 把 new_node 写入 头节点
        self.size += 1  # self.size累加 1

    def addAtTail(self, val: int) -> None:  # 定义函数 addAtTail（参数：self, 值: int）
        new_node = Node(val)  # 把 Node(值) 存入 new_node
        if self.tail:  # 若 self.尾节点
            self.tail.next = new_node  # 把 new_node 写入 下一个
            new_node.prev = self.tail  # 把 self.尾节点 写入 前一个
        else:  # 否则
            self.head = new_node  # 把 new_node 写入 头节点
        self.tail = new_node  # 把 new_node 写入 尾节点
        self.size += 1  # self.size累加 1

    def addAtIndex(
        self, index: int, val: int
    ) -> None:  # 定义函数 addAtIndex（参数：self, index: int, 值: int）
        if index < 0 or index > self.size:  # 若 index 小于 0 or index 超过 self.大小
            return  # return
        if index == 0:  # 若 index 等于 0
            self.addAtHead(val)  # self.addAtHead(值)
        elif index == self.size:  # 否则，若 index 等于 self.大小
            self.addAtTail(val)  # self.addAtTail(值)
        else:  # 否则
            curr = self.head  # 把 self.头节点 存入 当前值
            for _ in range(index):  # 让 _ 从 index 遍历
                curr = curr.next  # 把 当前值.下一个 存入 当前值
            new_node = Node(val)  # 把 Node(值) 存入 new_node
            new_node.prev = curr.prev  # 把 当前值.前一个 写入 前一个
            new_node.next = curr  # 把 当前值 写入 下一个
            curr.prev.next = new_node  # 把 new_node 写入 下一个
            curr.prev = new_node  # 把 new_node 写入 前一个
            self.size += 1  # self.size累加 1

    def deleteAtIndex(self, index: int) -> None:  # 定义函数 deleteAtIndex（参数：self, index: int）
        if index < 0 or index >= self.size:  # 若 index 小于 0 or index 不低于 self.大小
            return  # return
        if index == 0:  # 若 index 等于 0
            self.head = self.head.next  # 把 self.头节点.下一个 写入 头节点
            if self.head:  # 若 self.头节点
                self.head.prev = None  # 把 None 写入 前一个
            else:  # 否则
                self.tail = None  # 把 None 写入 尾节点
        elif index == self.size - 1:  # 否则，若 index 等于 self.大小 减 1
            self.tail = self.tail.prev  # 把 self.尾节点.前一个 写入 尾节点
            if self.tail:  # 若 self.尾节点
                self.tail.next = None  # 把 None 写入 下一个
            else:  # 否则
                self.head = None  # 把 None 写入 头节点
        else:  # 否则
            curr = self.head  # 把 self.头节点 存入 当前值
            for _ in range(index):  # 让 _ 从 index 遍历
                curr = curr.next  # 把 当前值.下一个 存入 当前值
            curr.prev.next = curr.next  # 把 当前值.下一个 写入 下一个
            curr.next.prev = curr.prev  # 把 当前值.前一个 写入 前一个
        self.size -= 1  # self.size累减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    obj = MyLinkedList()  # 把 MyLinkedList() 存入 obj
    obj.addAtHead(1)  # obj.addAtHead(1)
    obj.addAtTail(3)  # obj.addAtTail(3)
    obj.addAtIndex(1, 2)  # obj.addAtIndex(1, 2)
    print(obj.get(1))  # 2
    print(obj.get(0))  # 1
    print(obj.get(2))  # 3
    obj.deleteAtIndex(1)  # obj.deleteAtIndex(1)
    print(obj.get(1))  # 3
