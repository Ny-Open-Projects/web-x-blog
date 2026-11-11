# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
class Rule:  # 定义类
    """规则类：规则串中的不同字符表示不同的前进命令，循环使用（方案 11）。"""

    def __init__(self, r):  # 构造函数：初始化成员
        self.data = list(r)  # 把 列表(右指针) 写入 self.data
        self.idx = 0  # 把 0 写入 self.idx
        self.length = len(self.data)  # 把 长度(self.data) 写入 长度

    def __iter__(self):  # 定义函数 __iter__（参数：self）
        return self  # 返回 self

    def __next__(self):  # 定义函数 __next__（参数：self）
        ch = self.data[self.idx]  # 把 self.data[self.idx] 存入 字符
        self.idx = (self.idx + 1) % self.length  # 把 (self.idx 加 1) 对…取模 self.长度 写入 self.idx
        return ch  # 返回 字符

    def peek(self):  # 定义函数 peek（参数：self）
        return self.data[self.idx]  # 返回 self.data[self.idx]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    r = Rule("ESVM")  # 把 Rule(「ESVM」) 存入 右指针
    print("".join(next(r) for _ in range(10)))  # ESVMESVMES
    r2 = Rule("semv")  # 把 Rule(「semv」) 存入 r2
    print("".join(next(r2) for _ in range(6)))  # semvse
