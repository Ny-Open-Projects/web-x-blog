# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145382034
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def myAtoi(str):  # 定义函数 myAtoi（参数：str）
    class Automaton:  # 定义类
        def __init__(self):  # 构造函数：初始化成员
            self.state = "start"  # 把 '起点' 写入 self.state
            self.sign = 1  # 把 1 写入 self.sign
            self.ans = 0  # 把 0 写入 答案
            self.table = {  # 把 { 写入 self.table
                "start": ["start", "signed", "in_number", "end"],
                "signed": ["end", "end", "in_number", "end"],
                "in_number": ["end", "end", "in_number", "end"],
                "end": ["end", "end", "end", "end"],
            }

        def get_col(self, c):  # 定义函数 get_col（参数：self, 字符）
            if c == " ":  # 若 字符 等于 ' '
                return 0  # 返回 0
            if c in "+-":  # 若 字符 in ' 加 减 '
                return 1  # 返回 1
            if c.isdigit():  # 若 字符.isdigit(
                return 2  # 返回 2
            return 3  # 返回 3

        def get(self, c):  # 定义函数 get（参数：self, 字符）
            self.state = self.table[self.state][
                self.get_col(c)
            ]  # 把 self.table[self.state][self.get_col(字符)] 写入 self.state
            if self.state == "in_number":  # 若 self.state 等于 'in_number'
                self.ans = self.ans * 10 + int(c)  # 把 self.答案 乘 10 加 int(字符) 写入 答案
                if self.sign == 1:  # 若 self.sign 等于 1
                    self.ans = min(self.ans, 2147483647)  # 把 取较小值 self.答案, 2147483647) 写入 答案
                else:  # 否则
                    self.ans = min(self.ans, 2147483648)  # 把 取较小值 self.答案, 2147483648) 写入 答案
            elif self.state == "signed":  # 否则，若 self.state 等于 'signed'
                self.sign = 1 if c == "+" else -1  # 把 1 if 字符 等于 ' 加 ' else 减 1 写入 self.sign

    automaton = Automaton()  # 把 Automaton() 存入 automaton
    for c in str:  # 逐个取出 str 的元素（字符）
        automaton.get(c)  # automaton 查找 字符)
    return automaton.sign * automaton.ans  # 返回 automaton.sign 乘 automaton.答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(myAtoi("   -42"))  # 打印输出
    print(myAtoi("4193 with words"))  # 打印输出
    print(myAtoi("words and 987"))  # 打印输出
    print(myAtoi("-91283472332"))  # 打印输出
