"""定义 __eq__ 之后,__hash__ 被隐式置为 None 的机制与修复。"""


class Point:
    """只定义 __eq__:Point.__hash__ 被隐式置为 None。"""

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)


class A:
    """父类同时给出 __eq__ 与 __hash__,契约一致。"""

    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return isinstance(other, A) and self.key == other.key

    def __hash__(self):
        return hash(self.key)


class B(A):
    """子类只重写 __eq__:继承来的 __hash__ 也会被置空。"""

    def __eq__(self, other):
        return isinstance(other, A) and self.key == other.key


class C(A):
    """修复:显式恢复哈希,且相等性语义未变,契约成立。"""
    __hash__ = A.__hash__


if __name__ == "__main__":
    print("Point.__hash__:", Point.__hash__)
    try:
        hash(Point(1, 2))
    except TypeError as e:
        print("hash 实例报错:", e)

    print("B.__hash__:", B.__hash__, "(父类有哈希也被置空)")
    print("C 恢复哈希且与父类一致:", hash(C("k")) == hash(A("k")))
    print("等值的 C 与 A 在集合里去重:", len({C("k"), A("k")}))
