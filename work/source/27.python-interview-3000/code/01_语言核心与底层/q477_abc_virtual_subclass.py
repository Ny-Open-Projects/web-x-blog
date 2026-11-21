from collections.abc import Sequence, Iterable

class Range3(Sequence):
    """正规子类:实现抽象方法,获得 Mixin 能力"""
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if i < 0:
            i += self.n
        if not 0 <= i < self.n:
            raise IndexError(i)
        return i * 10

class Bag:
    """从未继承 Iterable,却声称自己是"""
    def __iter__(self):
        return iter([1, 2, 3])

Iterable.register(Bag)

if __name__ == "__main__":
    r = Range3(3)
    print(list(r), r[1], len(r))          # Mixin 提供的 __iter__ 生效
    print(isinstance(r, Sequence), issubclass(Range3, Sequence))

    b = Bag()
    print(isinstance(b, Iterable))        # True:虚拟子类只改 isinstance
    print(list(b))
    print(issubclass(Bag, Iterable))
