# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311
class SortedStack:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.stk1 = []  # 把 [] 写入 self.stk1
        self.stk2 = []  # 把 [] 写入 self.stk2

    def push(self, val: int) -> None:  # 定义函数 push（参数：self, 值: int）
        # Move all elements larger than val from stk1 to stk2
        while self.stk1 and self.stk1[-1] > val:  # 循环，直到不满足「self.stk1 and self.stk1[ 减 1] 超过 值」
            self.stk2.append(self.stk1.pop())  # 把 self.stk1 弹出 追加到列表尾部
        # Push val onto stk1
        self.stk1.append(val)  # 把 值 追加到列表尾部
        # Move elements back from stk2 to stk1
        while self.stk2:  # 循环，直到不满足「self.stk2」
            self.stk1.append(self.stk2.pop())  # 把 self.stk2 弹出 追加到列表尾部

    def pop(self) -> None:  # 定义函数 pop（参数：self）
        if not self.isEmpty():  # 若 not self.isEmpty(
            self.stk1.pop()  # 弹出栈顶元素

    def peek(self) -> int:  # 定义函数 peek（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return -1  # 返回 减 1
        return self.stk1[-1]  # 返回 self.stk1[ 减 1]

    def isEmpty(self) -> bool:  # 定义函数 isEmpty（参数：self）
        return len(self.stk1) == 0  # 返回 长度(self.stk1) 等于 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    s = SortedStack()  # 把 SortedStack() 存入 字符串
    for v in [4, 2, 5, 1, 3]:  # for 值 in [4, 2, 5, 1, 3]:
        s.push(v)  # 把 值 压入栈/数组尾部
    out = []  # 把 [] 存入 out
    while not s.isEmpty():  # 循环，直到不满足「not 字符串.isEmpty(」
        out.append(s.peek())  # 把 字符串.peek( 追加到列表尾部
        s.pop()  # 弹出栈顶元素
    print(out)  # 打印输出
