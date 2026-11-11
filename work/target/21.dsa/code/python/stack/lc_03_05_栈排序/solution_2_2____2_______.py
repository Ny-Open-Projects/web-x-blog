# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311
class SortedStack:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.stk = []  # 把 [] 写入 栈

    def push(self, val: int) -> None:  # 定义函数 push（参数：self, 值: int）
        temp_stack = []  # 把 [] 存入 temp_stack
        # Move all elements larger than val from stk to temp_stack
        while self.stk and self.stk[-1] > val:  # 循环，直到不满足「self.栈 and self.栈[ 减 1] 超过 值」
            temp_stack.append(self.stk.pop())  # 把 self.栈 弹出 追加到列表尾部
        # Push val onto stk
        self.stk.append(val)  # 把 值 追加到列表尾部
        # Move elements back from temp_stack to stk
        while temp_stack:  # 循环，直到不满足「temp_stack」
            self.stk.append(temp_stack.pop())  # 把 temp_stack 弹出 追加到列表尾部

    def pop(self) -> None:  # 定义函数 pop（参数：self）
        if not self.isEmpty():  # 若 not self.isEmpty(
            self.stk.pop()  # 弹出栈顶元素

    def peek(self) -> int:  # 定义函数 peek（参数：self）
        if self.isEmpty():  # 若 self.isEmpty(
            return -1  # 返回 减 1
        return self.stk[-1]  # 返回 self.栈[ 减 1]

    def isEmpty(self) -> bool:  # 定义函数 isEmpty（参数：self）
        return len(self.stk) == 0  # 返回 长度(self.栈) 等于 0

    def sort(self):  # 定义函数 sort（参数：self）
        result = []  # 把 [] 存入 结果
        while self.stk:  # 循环，直到不满足「self.栈」
            result.append(self.stk.pop())  # 把 self.栈 弹出 追加到列表尾部
        return result[::-1]  # 返回 结果[:: 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    s = SortedStack()  # 把 SortedStack() 存入 字符串
    for v in [4, 2, 5, 1, 3]:  # for 值 in [4, 2, 5, 1, 3]:
        s.push(v)  # 把 值 压入栈/数组尾部
    out = []  # 把 [] 存入 out
    while not s.isEmpty():  # 循环，直到不满足「not 字符串.isEmpty(」
        out.append(s.peek())  # 把 字符串.peek( 追加到列表尾部
        s.pop()  # 弹出栈顶元素
    print(out)  # 打印输出
