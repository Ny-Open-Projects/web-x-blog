# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385578
class MyCircularDeque:  # 定义类
    def __init__(self, k: int):  # 构造函数：初始化成员
        self.capacity = k + 1  # Use k+1 to distinguish full and empty
        self.rear = 0  # 把 0 写入 self.rear
        self.front = 0  # 把 0 写入 self.front
        self.elements = [0] * self.capacity  # 把 [0] 乘 self.capacity 写入 self.elements

    def insertFront(self, value: int) -> bool:  # 定义函数 insertFront（参数：self, value: int）
        if self.isFull():  # 若 self.isFull(
            return False  # 返回 False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.elements[self.front] = value  # 把 value 写入 self.elements[self.front]
        return True  # 返回 True

    def insertLast(self, value: int) -> bool:  # 定义函数 insertLast（参数：self, value: int）
        if self.isFull():  # 若 self.isFull(
            return False  # 返回 False
        self.elements[self.rear] = value  # 把 value 写入 self.elements[self.rear]
        self.rear = (
            self.rear + 1
        ) % self.capacity  # 把 (self.rear 加 1) 对…取模 self.capacity 写入 self.rear
        return True  # 返回 True

    def deleteFront(self) -> bool:  # 定义函数 deleteFront（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return False  # 返回 False
        self.front = (
            self.front + 1
        ) % self.capacity  # 把 (self.front 加 1) 对…取模 self.capacity 写入 self.front
        return True  # 返回 True

    def deleteLast(self) -> bool:  # 定义函数 deleteLast（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return False  # 返回 False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True  # 返回 True

    def getFront(self) -> int:  # 定义函数 getFront（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return -1  # 返回 减 1
        return self.elements[self.front]  # 返回 self.elements[self.front]

    def getRear(self) -> int:  # 定义函数 getRear（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return -1  # 返回 减 1
        return self.elements[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:  # 定义函数 isEmpty（参数：self）
        return self.rear == self.front  # 返回 self.rear 等于 self.front

    def isFull(self) -> bool:  # 定义函数 isFull（参数：self）
        return (
            self.rear + 1
        ) % self.capacity == self.front  # 返回 (self.rear 加 1) 对…取模 self.capacity 等于 self.front


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
