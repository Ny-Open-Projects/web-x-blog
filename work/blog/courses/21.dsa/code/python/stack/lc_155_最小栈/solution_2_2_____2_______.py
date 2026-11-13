# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
class MinStack:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.stack = []  # 把 [] 写入 栈
        self.mins = []  # 把 [] 写入 self.mins

    def push(self, val: int) -> None:  # 定义函数 push（参数：self, 值: int）
        self.stack.append(val)  # 把 值 追加到列表尾部
        self.mins.append(
            min(last(self.mins), val) if self.mins else val
        )  # 把 取较小值 last(self.mins 追加到列表尾部

    def pop(self) -> None:  # 定义函数 pop（参数：self）
        self.stack.pop()  # 弹出栈顶元素
        self.mins.pop()  # 弹出栈顶元素

    def top(self) -> int:  # 定义函数 top（参数：self）
        return self.stack[-1]  # 返回 self.栈[ 减 1]

    def getMin(self) -> int:  # 定义函数 getMin（参数：self）
        return last(self.mins)  # 返回 last(self.mins)


def last(arr):  # 定义函数 last（参数：数组）
    return arr[-1]  # 返回 数组[ 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    minStack = MinStack()  # 把 MinStack() 存入 minStack
    minStack.push(-2)  # 把 减 2 压入栈/数组尾部
    minStack.push(0)  # 把 0 压入栈/数组尾部
    minStack.push(-3)  # 把 减 3 压入栈/数组尾部
    print(minStack.getMin())  # -3
    minStack.pop()  # 弹出栈顶元素
    print(minStack.top())  # 0
    print(minStack.getMin())  # -2
