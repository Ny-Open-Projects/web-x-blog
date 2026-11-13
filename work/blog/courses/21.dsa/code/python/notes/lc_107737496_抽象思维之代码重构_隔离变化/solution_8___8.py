# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Filler:  # 定义类
    """填充器（迭代器风格）：按规则串（如 'ESVM' 逆时针 / 'semv' 顺时针）在 matrix 上逐格前进。
    规则字母：E/S/V/M 表示 下/右/上/左；遇到边界后收缩对应的最小/最大行列，实现旋转填充。"""

    def __init__(self, rn, cn):  # 构造函数：初始化成员
        self.row_num = rn  # 把 rn 写入 self.row_num
        self.col_num = cn  # 把 cn 写入 self.col_num
        self.rule = "ESVM"  # 把 'ESVM' 写入 self.rule
        self.reset()  # self.reset()

    def reset(self):  # 定义函数 reset（参数：self）
        self.pos = {"row": 0, "col": 0}  # 把 {'row': 0, 'col': 0} 写入 self.pos
        self.idx = 0  # 把 0 写入 self.idx
        self.r_min = self.c_min = 0  # 把 self.c_min 赋值为 0 写入 self.r_min
        self.r_max = self.row_num - 1  # 把 self.row_num 减 1 写入 self.r_max
        self.c_max = self.col_num - 1  # 把 self.col_num 减 1 写入 self.c_max

    def set_rule(self, r):  # 定义函数 set_rule（参数：self, 右指针）
        self.rule = r  # 把 右指针 写入 self.rule

    def __iter__(self):  # 定义函数 __iter__（参数：self）
        while (
            self.r_min
            <= self.pos["row"]
            <= self.r_max  # 循环，直到不满足「self.r_min 不超过 self.pos['row'] 不超过 self.r_max and」
            and self.c_min <= self.pos["col"] <= self.c_max
        ):  # 把 self.pos['col'] 不超过 self.c_max): 写入 self.c_min <
            yield (self.pos["row"], self.pos["col"])  # yield (self.pos['row'], self.pos['col'])
            self._advance()  # self._advance()

    def _advance(self):  # 定义函数 _advance（参数：self）
        cmd = self.rule[self.idx % 4]  # 把 self.rule[self.idx 对…取模 4] 存入 cmd
        if cmd == "E":  # 向下
            self.pos["row"] += 1  # 把 1 写入 self.pos['row'] +
            if self.pos["row"] == self.r_max:  # 若 self.pos['row'] 等于 self.r_max
                self.idx += 1  # self.idx累加 1
                self.c_min += 1  # self.c_min累加 1
        elif cmd == "S":  # 向右
            self.pos["col"] += 1  # 把 1 写入 self.pos['col'] +
            if self.pos["col"] == self.c_max:  # 若 self.pos['col'] 等于 self.c_max
                self.idx += 1  # self.idx累加 1
                self.r_max -= 1  # self.r_max累减 1
        elif cmd == "V":  # 向上
            self.pos["row"] -= 1  # 把 1 写入 self.pos['row'] -
            if self.pos["row"] == self.r_min:  # 若 self.pos['row'] 等于 self.r_min
                self.idx += 1  # self.idx累加 1
                self.c_max -= 1  # self.c_max累减 1
        elif cmd == "M":  # 向左
            self.pos["col"] -= 1  # 把 1 写入 self.pos['col'] -
            if self.pos["col"] == self.c_min:  # 若 self.pos['col'] 等于 self.c_min
                self.idx += 1  # self.idx累加 1
                self.r_min += 1  # self.r_min累加 1


def fill_matrix(rn, cn, rule="ESVM"):  # 定义函数 fill_matrix（参数：rn, cn, rule 赋值为 'ESVM'）
    mat = [[0] * cn for _ in range(rn)]  # 把 [[0] 乘 cn for _ in range(rn)] 存入 mat
    f = Filler(rn, cn)  # 把 Filler(rn, cn) 存入 f
    f.set_rule(rule)  # f.set_rule(rule)
    i = 1  # 把 1 存入 下标 i
    for r, c in f:  # for (右指针, 字符) in f:
        mat[r][c] = i  # 把 下标 i 写入 mat[r][c]
        i += 1  # 下标 i累加 1
    return mat  # 返回 mat


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    for row in fill_matrix(6, 6, "ESVM"):  # 逐个取出 fill_matrix 的元素（row）
        print(" ".join("%2d" % v for v in row))  # 打印输出
