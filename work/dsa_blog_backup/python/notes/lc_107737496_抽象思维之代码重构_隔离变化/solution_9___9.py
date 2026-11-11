# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Location:  # 定义类
    def __init__(self, row=0, col=0):  # 构造函数：初始化成员
        self.row = row  # 把 row 写入 self.row
        self.col = col  # 把 col 写入 self.col


class Filler:  # 定义类
    """填充器：依据规则串（如 ESVM 逆时针 / semv 顺时针）逐位置前进（方案 9）。"""

    def __init__(self, rn, cn):  # 构造函数：初始化成员
        self.row_num = rn  # 把 rn 写入 self.row_num
        self.col_num = cn  # 把 cn 写入 self.col_num
        self.reset()  # self.reset()

    def reset(self):  # 定义函数 reset（参数：self）
        self.pos = Location(0, 0)  # 把 Location(0, 0) 写入 self.pos
        self.idx = 0  # 把 0 写入 self.idx
        self.r_min = self.c_min = 0  # 把 self.c_min 赋值为 0 写入 self.r_min
        self.r_max = self.row_num - 1  # 把 self.row_num 减 1 写入 self.r_max
        self.c_max = self.col_num - 1  # 把 self.col_num 减 1 写入 self.c_max
        self.rule = "ESVM"  # 把 「ESVM」 写入 self.rule

    def set_rule(self, rule):  # 定义函数 set_rule（参数：self, rule）
        self.rule = rule  # 把 rule 写入 self.rule

    def current(self):  # 定义函数 current（参数：self）
        return self.pos  # 返回 self.pos

    def __iter__(self):  # 定义函数 __iter__（参数：self）
        return self  # 返回 self

    def __next__(self):  # 定义函数 __next__（参数：self）
        res = Location(self.pos.row, self.pos.col)  # 把 Location(self.pos.row, self.pos.col) 存入 结果
        ch = self.rule[self.idx % len(self.rule)]  # 把 self.rule[self.idx 对…取模 长度(self.rule)] 存入 字符
        if ch == "E":  # 向下
            self.pos.row += 1  # self.pos.row累加 1
            if self.pos.row == self.r_max:  # 若 self.pos.row 等于 self.r_max
                self.idx += 1  # self.idx累加 1
                self.c_min += 1  # self.c_min累加 1
        elif ch == "S":  # 向右
            self.pos.col += 1  # self.pos.col累加 1
            if self.pos.col == self.c_max:  # 若 self.pos.col 等于 self.c_max
                self.idx += 1  # self.idx累加 1
                self.r_max -= 1  # self.r_max累减 1
        elif ch == "V":  # 向上
            self.pos.row -= 1  # self.pos.row累减 1
            if self.pos.row == self.r_min:  # 若 self.pos.row 等于 self.r_min
                self.idx += 1  # self.idx累加 1
                self.c_max -= 1  # self.c_max累减 1
        elif ch == "M":  # 向左
            self.pos.col -= 1  # self.pos.col累减 1
            if self.pos.col == self.c_min:  # 若 self.pos.col 等于 self.c_min
                self.idx += 1  # self.idx累加 1
                self.r_min += 1  # self.r_min累加 1
        elif ch == "e":  # 顺时针：向下
            self.pos.row += 1  # self.pos.row累加 1
            if self.pos.row == self.r_max:  # 若 self.pos.row 等于 self.r_max
                self.idx += 1  # self.idx累加 1
                self.c_max -= 1  # self.c_max累减 1
        elif ch == "s":  # 顺时针：向右
            self.pos.col += 1  # self.pos.col累加 1
            if self.pos.col == self.c_max:  # 若 self.pos.col 等于 self.c_max
                self.idx += 1  # self.idx累加 1
                self.r_min += 1  # self.r_min累加 1
        elif ch == "v":  # 顺时针：向上
            self.pos.row -= 1  # self.pos.row累减 1
            if self.pos.row == self.r_min:  # 若 self.pos.row 等于 self.r_min
                self.idx += 1  # self.idx累加 1
                self.c_min += 1  # self.c_min累加 1
        elif ch == "m":  # 顺时针：向左
            self.pos.col -= 1  # self.pos.col累减 1
            if self.pos.col == self.c_min:  # 若 self.pos.col 等于 self.c_min
                self.idx += 1  # self.idx累加 1
                self.r_max -= 1  # self.r_max累减 1
        return res  # 返回 结果


def test(rule, rn, cn):  # 定义函数 test（参数：rule, rn, cn）
    obj = Filler(rn, cn)  # 把 Filler(rn, cn) 存入 obj
    obj.set_rule(rule)  # obj.set_rule(rule)
    seq = [next(obj) for _ in range(rn * cn)]  # 把 [下一个(obj) for _ in range(rn 乘 cn)] 存入 seq
    print(rule, "->", [(p.row, p.col) for p in seq])  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    test("ESVM", 4, 4)  # test(「ESVM」, 4, 4)
    test("semv", 4, 4)  # test(「semv」, 4, 4)
