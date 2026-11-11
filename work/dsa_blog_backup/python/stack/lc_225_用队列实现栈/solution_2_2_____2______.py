# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113825
from collections import deque  # from collections import deque


class MyStack:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.queue = deque()  # 把 deque() 写入 队列

    def push(self, x: int) -> None:  # 定义函数 push（参数：self, x: int）
        n = len(self.queue)  # 把 长度(self.队列) 存入 元素个数
        self.queue.append(x)  # 把 x 追加到列表尾部
        for _ in range(n):  # 让 _ 从 元素个数 遍历
            self.queue.append(self.queue.popleft())  # 把 self.队列.popleft( 追加到列表尾部

    def pop(self) -> int:  # 定义函数 pop（参数：self）
        return self.queue.popleft()  # 返回 self.队列.popleft()

    def top(self) -> int:  # 定义函数 top（参数：self）
        return self.queue[0]  # 返回 self.队列[0]

    def empty(self) -> bool:  # 定义函数 empty（参数：self）
        return len(self.queue) == 0  # 返回 长度(self.队列) 等于 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    obj = MyStack()  # 把 MyStack() 存入 obj
    obj.push(1)  # 把 1 压入栈/数组尾部
    obj.push(2)  # 把 2 压入栈/数组尾部
    print(obj.top())  # 2
    print(obj.pop())  # 2
    print(obj.empty())  # False
