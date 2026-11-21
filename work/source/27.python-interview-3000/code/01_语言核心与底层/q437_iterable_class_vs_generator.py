from collections.abc import Iterable, Iterator

class Countdown(Iterable):
    """类实现:可重复迭代,每次 for 都从头开始"""
    def __init__(self, n):
        self.n = n

    def __iter__(self) -> Iterator:
        return CountdownIterator(self.n)

class CountdownIterator:
    def __init__(self, n):
        self.cur = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur <= 0:
            raise StopIteration
        self.cur -= 1
        return self.cur + 1

def countdown_gen(n):
    """生成器实现:代码最短,但实例一次性"""
    while n > 0:
        yield n
        n -= 1

if __name__ == "__main__":
    cd = Countdown(3)
    print(list(cd), list(cd))             # [3, 2, 1] [3, 2, 1] 可重复迭代
    cg = countdown_gen(3)
    print(list(cg), list(cg))             # 第二次为空:生成器已耗尽
