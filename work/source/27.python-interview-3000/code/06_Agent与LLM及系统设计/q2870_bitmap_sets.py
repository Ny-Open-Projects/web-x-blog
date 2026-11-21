"""Q2870 位图签名集合:一个整数当一亿个布尔用 位运算做集合代数。

海量「是否出现」标记(签到 UV 去重 特征签名)用 set 存太贵,位图
用整数二进制位表达集合:add 是按位置或,and/or/except 是三条位运算,
基数就是 popcount——内存省两个量级,交并差一步到位。
"""


class Bitmap:
    def __init__(self, bits=0):
        self.bits = bits

    def add(self, x):
        self.bits |= 1 << x
        return self

    def __contains__(self, x):
        return bool((self.bits >> x) & 1)

    def card(self):
        return bin(self.bits).count("1")

    def to_list(self, limit=64):
        return [i for i in range(limit) if (self.bits >> i) & 1]

    def union(self, other):
        return Bitmap(self.bits | other.bits)

    def intersect(self, other):
        return Bitmap(self.bits & other.bits)

    def except_(self, other):
        return Bitmap(self.bits & ~other.bits)


def main():
    day1 = Bitmap().add(1).add(3).add(5)     # 周一签到用户 1 3 5
    day2 = Bitmap().add(3).add(5).add(7)     # 周二签到用户 3 5 7
    both = day1.intersect(day2)
    either = day1.union(day2)
    only_d1 = day1.except_(day2)
    assert both.to_list() == [3, 5] and both.card() == 2, both.to_list()
    assert either.to_list() == [1, 3, 5, 7], either.to_list()
    assert only_d1.to_list() == [1], only_d1.to_list()
    assert 3 in day1 and 7 not in day1
    assert day1.card() == 3
    # 只补一个位,不用复制整个集合
    day1.add(2)
    assert day1.card() == 4 and day1.to_list() == [1, 2, 3, 5]
    print("两天都来:", both.to_list())
    print("任一天来:", either.to_list())
    print("只周一:", only_d1.to_list())
    print("位运算集合代数:交 并 差基数分别为", both.card(),
          either.card(), only_d1.card())


if __name__ == "__main__":
    main()
