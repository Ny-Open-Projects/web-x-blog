# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Location:  # 定义类
    def __init__(self, row=0, col=0):  # 构造函数：初始化成员
        self.row = row  # 把 row 写入 self.row
        self.col = col  # 把 col 写入 self.col


class Rule:  # 定义类
    """规则对象：供 Filler 通过指针 (*cmd) 读取/推进当前命令。"""

    def __init__(self, r):  # 构造函数：初始化成员
        self.data = list(r)  # 把 列表(右指针) 写入 self.data
        self.idx = 0  # 把 0 写入 self.idx
        self.length = len(self.data)  # 把 长度(self.data) 写入 长度

    def current(self):  # 定义函数 current（参数：self）
        return self.data[self.idx]  # 返回 self.data[self.idx]

    def advance(self):  # 定义函数 advance（参数：self）
        self.idx = (self.idx + 1) % self.length  # 把 (self.idx 加 1) 对…取模 self.长度 写入 self.idx


class Filler:  # 定义类
    """填充器：持有 Rule 对象，依据规则逐位置前进（方案 12）。"""

    def __init__(self, rn, cn):  # 构造函数：初始化成员
        self.row_num = rn  # 把 rn 写入 self.row_num
        self.col_num = cn  # 把 cn 写入 self.col_num
        self.reset()  # self.reset()

    def reset(self):  # 定义函数 reset（参数：self）
        self.pos = Location(0, 0)  # 把 Location(0, 0) 写入 self.pos
        self.r_min = self.c_min = 0  # 把 self.c_min 赋值为 0 写入 self.r_min
        self.r_max = self.row_num - 1  # 把 self.row_num 减 1 写入 self.r_max
        self.c_max = self.col_num - 1  # 把 self.col_num 减 1 写入 self.c_max
        self.cmd = None  # 把 None 写入 self.cmd

    def set_rule(self, rule):  # 定义函数 set_rule（参数：self, rule）
        self.cmd = rule  # 把 rule 写入 self.cmd

    def __iter__(self):  # 定义函数 __iter__（参数：self）
        return self  # 返回 self

    def __next__(self):  # 定义函数 __next__（参数：self）
        res = Location(self.pos.row, self.pos.col)  # 把 Location(self.pos.row, self.pos.col) 存入 结果
        ch = self.cmd.current()  # 把 self.cmd.current() 存入 字符
        if ch == "E":  # 若 字符 等于 'E'
            self.pos.row += 1  # self.pos.row累加 1
            if self.pos.row == self.r_max:  # 若 self.pos.row 等于 self.r_max
                self.cmd.advance()  # self.cmd.advance()
                self.c_min += 1  # self.c_min累加 1
        elif ch == "S":  # 否则，若 字符 等于 'S'
            self.pos.col += 1  # self.pos.col累加 1
            if self.pos.col == self.c_max:  # 若 self.pos.col 等于 self.c_max
                self.cmd.advance()  # self.cmd.advance()
                self.r_max -= 1  # self.r_max累减 1
        elif ch == "V":  # 否则，若 字符 等于 'V'
            self.pos.row -= 1  # self.pos.row累减 1
            if self.pos.row == self.r_min:  # 若 self.pos.row 等于 self.r_min
                self.cmd.advance()  # self.cmd.advance()
                self.c_max -= 1  # self.c_max累减 1
        elif ch == "M":  # 否则，若 字符 等于 'M'
            self.pos.col -= 1  # self.pos.col累减 1
            if self.pos.col == self.c_min:  # 若 self.pos.col 等于 self.c_min
                self.cmd.advance()  # self.cmd.advance()
                self.r_min += 1  # self.r_min累加 1
        return res  # 返回 结果


def test(rule, rn, cn):  # 定义函数 test（参数：rule, rn, cn）
    obj = Filler(rn, cn)  # 把 Filler(rn, cn) 存入 obj
    obj.set_rule(Rule(rule))  # obj.set_rule(Rule(rule))
    seq = [next(obj) for _ in range(rn * cn)]  # 把 [下一个(obj) for _ in range(rn 乘 cn)] 存入 seq
    print(rule, "->", [(p.row, p.col) for p in seq])  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    test("ESVM", 4, 4)  # test(「ESVM」, 4, 4)
