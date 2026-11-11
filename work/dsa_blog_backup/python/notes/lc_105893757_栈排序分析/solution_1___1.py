# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class SortedStack:  # 定义类
    """有序栈：push 时通过辅助栈把元素插入到正确位置，使栈底->栈顶保持升序（栈顶最小）。"""

    def __init__(self):  # 构造函数：初始化成员
        self._data = []  # 把 [] 写入 self._data

    def push(self, val):  # 定义函数 push（参数：self, 值）
        temp = []  # 把 [] 存入 临时变量
        while (
            self._data and self._data[-1] < val
        ):  # 循环，直到不满足「self._data and self._data[ 减 1] 小于 值」
            temp.append(self._data.pop())  # 把 self._data 弹出 追加到列表尾部
        self._data.append(val)  # 把 值 追加到列表尾部
        while temp:  # 循环，直到不满足「临时变量」
            self._data.append(temp.pop())  # 把 临时变量 弹出 追加到列表尾部

    def pop(self):  # 定义函数 pop（参数：self）
        return self._data.pop() if self._data else None  # 返回 self._data 弹出 ) if self._data else None

    def peek(self):  # 定义函数 peek（参数：self）
        return self._data[-1] if self._data else None  # 返回 self._data[ 减 1] if self._data else None

    def is_empty(self):  # 定义函数 is_empty（参数：self）
        return len(self._data) == 0  # 返回 长度(self._data) 等于 0

    def sort(self):  # 定义函数 sort（参数：self）
        return sorted(self._data)  # 返回 sorted(self._data)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    st = SortedStack()  # 把 SortedStack() 存入 st
    for v in [1, 3, 2, 4]:  # for 值 in [1, 3, 2, 4]:
        st.push(v)  # 把 值 压入栈/数组尾部
    print("栈内有序序列:", st.sort())  # 打印输出
    out = []  # 把 [] 存入 out
    while not st.is_empty():  # 循环，直到不满足「not st.is_empty(」
        out.append(st.pop())  # 把 st 弹出 追加到列表尾部
    print("依次 pop:", out)  # 打印输出
