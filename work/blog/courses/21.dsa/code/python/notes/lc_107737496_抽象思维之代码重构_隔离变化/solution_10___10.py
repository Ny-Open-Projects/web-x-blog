# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Location:  # 定义类
    def __init__(self, row=0, col=0):  # 构造函数：初始化成员
        self.row = row  # 把 row 写入 self.row
        self.col = col  # 把 col 写入 self.col


class Filler:  # 定义类
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

    def __iter__(self):  # 定义函数 __iter__（参数：self）
        return self  # 返回 self

    def __next__(self):  # 定义函数 __next__（参数：self）
        res = Location(self.pos.row, self.pos.col)  # 把 Location(self.pos.row, self.pos.col) 存入 结果
        ch = self.rule[self.idx % len(self.rule)]  # 把 self.rule[self.idx 对…取模 长度(self.rule)] 存入 字符
        if ch == "E":  # 若 字符 等于 'E'
            self.pos.row += 1  # self.pos.row累加 1
            if self.pos.row == self.r_max:  # 若 self.pos.row 等于 self.r_max
                self.idx += 1  # self.idx累加 1
                self.c_min += 1  # self.c_min累加 1
        elif ch == "S":  # 否则，若 字符 等于 'S'
            self.pos.col += 1  # self.pos.col累加 1
            if self.pos.col == self.c_max:  # 若 self.pos.col 等于 self.c_max
                self.idx += 1  # self.idx累加 1
                self.r_max -= 1  # self.r_max累减 1
        elif ch == "V":  # 否则，若 字符 等于 'V'
            self.pos.row -= 1  # self.pos.row累减 1
            if self.pos.row == self.r_min:  # 若 self.pos.row 等于 self.r_min
                self.idx += 1  # self.idx累加 1
                self.c_max -= 1  # self.c_max累减 1
        elif ch == "M":  # 否则，若 字符 等于 'M'
            self.pos.col -= 1  # self.pos.col累减 1
            if self.pos.col == self.c_min:  # 若 self.pos.col 等于 self.c_min
                self.idx += 1  # self.idx累加 1
                self.r_min += 1  # self.r_min累加 1
        return res  # 返回 结果


class Matrix:  # 定义类
    def __init__(self, r, c):  # 构造函数：初始化成员
        self.row = r  # 把 右指针 写入 self.row
        self.col = c  # 把 字符 写入 self.col
        self.buf = [[0] * c for _ in range(r)]  # 把 [[0] 乘 字符 for _ in range(右指针)] 写入 self.buf

    def __call__(self, r, c):  # 定义函数 __call__（参数：self, 右指针, 字符）
        return self.buf[r][c]  # 返回 self.buf[右指针][字符]

    def __setitem__(self, key, value):  # 定义函数 __setitem__（参数：self, key, value）
        r, c = key  # 把 key 写入 r, c
        self.buf[r][c] = value  # 把 value 写入 self.buf[r][c]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    rn = cn = 9  # 把 cn 赋值为 9 存入 rn
    obj = Filler(rn, cn)  # 把 Filler(rn, cn) 存入 obj
    obj.set_rule("ESVM")  # 逆时针
    m = Matrix(rn, cn)  # 把 Matrix(rn, cn) 存入 映射表
    for i in range(rn * cn):  # 让 下标 i 从 rn 乘 cn 遍历
        p = next(obj)  # 把 下一个(obj) 存入 节点
        m[p.row, p.col] = i + 1  # 把 下标 i 加 1 写入 m[p.row, p.col]
    for row in m.buf:  # 逐个取出 映射表 的元素（row）
        print(" ".join(f"{x:2d}" for x in row))  # 打印输出
