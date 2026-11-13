# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011
class MyQueue:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.inStack = []  # 把 [] 写入 self.inStack
        self.outStack = []  # 把 [] 写入 self.outStack

    def push(self, x: int) -> None:  # 定义函数 push（参数：self, x: int）
        self.inStack.append(x)  # 把 x 追加到列表尾部

    def pop(self) -> int:  # 定义函数 pop（参数：self）
        if not self.outStack:  # 若 not self.outStack
            self._in2out()  # self._in2out()
        return self.outStack.pop()  # 返回 self.outStack 弹出 )

    def peek(self) -> int:  # 定义函数 peek（参数：self）
        if not self.outStack:  # 若 not self.outStack
            self._in2out()  # self._in2out()
        return self.outStack[-1]  # 返回 self.outStack[ 减 1]

    def empty(self) -> bool:  # 定义函数 empty（参数：self）
        return not self.outStack and not self.inStack  # 返回 not self.outStack and not self.inStack

    def _in2out(self) -> None:  # 定义函数 _in2out（参数：self）
        while self.inStack:  # 循环，直到不满足「self.inStack」
            self.outStack.append(self.inStack.pop())  # 把 self.inStack 弹出 追加到列表尾部


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    q = MyQueue()  # 把 MyQueue() 存入 节点
    q.push(1)  # 把 1 压入栈/数组尾部
    q.push(2)  # 把 2 压入栈/数组尾部
    print(q.peek())  # 打印输出
    print(q.pop())  # 打印输出
    print(q.empty())  # 打印输出
    q.push(3)  # 把 3 压入栈/数组尾部
    print(q.pop())  # 打印输出
    print(q.pop())  # 打印输出
