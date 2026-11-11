# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
class MinStack:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.x_stack = []  # 把 [] 写入 self.x_stack
        self.min_stack = [float("inf")]  # 把 [float('inf')] 写入 self.min_stack

    def push(self, val: int) -> None:  # 定义函数 push（参数：self, 值: int）
        self.x_stack.append(val)  # 把 值 追加到列表尾部
        self.min_stack.append(
            min(self.min_stack[-1], val)
        )  # 把 取较小值 self.min_stack[ 减 1], 值 追加到列表尾部

    def pop(self) -> None:  # 定义函数 pop（参数：self）
        self.x_stack.pop()  # 弹出栈顶元素
        self.min_stack.pop()  # 弹出栈顶元素

    def top(self) -> int:  # 定义函数 top（参数：self）
        return self.x_stack[-1]  # 返回 self.x_stack[ 减 1]

    def getMin(self) -> int:  # 定义函数 getMin（参数：self）
        return self.min_stack[-1]  # 返回 self.min_stack[ 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    minStack = MinStack()  # 把 MinStack() 存入 minStack
    minStack.push(-2)  # 把 减 2 压入栈/数组尾部
    minStack.push(0)  # 把 0 压入栈/数组尾部
    minStack.push(-3)  # 把 减 3 压入栈/数组尾部
    print(minStack.getMin())  # -3
    minStack.pop()  # 弹出栈顶元素
    print(minStack.top())  # 0
    print(minStack.getMin())  # -2
