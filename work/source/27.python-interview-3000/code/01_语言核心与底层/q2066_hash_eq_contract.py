"""可哈希与相等性的一致性契约:== 相等必须带来相同哈希。"""
import itertools


class Money:
    """金额:相等的实例必须落进同一个哈希桶。"""

    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, other):
        return isinstance(other, Money) and self.cents == other.cents

    def __hash__(self):
        return hash(self.cents)      # 与 __eq__ 用同一字段


_counter = itertools.count()


class BrokenMoney:
    """反面教材:__eq__ 按值,__hash__ 却每个实例不同,契约破裂。"""

    def __init__(self, cents):
        self.cents = cents
        self._h = next(_counter)     # 每个实例一个独立哈希

    def __eq__(self, other):
        return isinstance(other, BrokenMoney) and self.cents == other.cents

    def __hash__(self):
        return self._h


if __name__ == "__main__":
    a, b = Money(100), Money(100)
    print("a == b:", a == b, "| 哈希相同:", hash(a) == hash(b))
    ledger = {a: "工资"}
    print("dict 用等值的 b 取 a 存的值:", ledger[b])

    x, y = BrokenMoney(100), BrokenMoney(100)
    print("BrokenMoney: x == y:", x == y, "| 哈希相同:", hash(x) == hash(y))
    bad = {x: "工资"}
    try:
        print("dict 用 y 取值:", bad[y])
    except KeyError:
        print("契约破坏:等值对象找不到彼此的键,KeyError")
