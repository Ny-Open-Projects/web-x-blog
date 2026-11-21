class Countdown:
    """可迭代对象:每次 iter 返回新迭代器,可重复遍历"""
    def __init__(self, n):
        self.n = n

    def __iter__(self):
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

if __name__ == "__main__":
    c = Countdown(3)
    print(list(c), list(c))       # [3,2,1] [3,2,1] 可重复
    it = iter(c)
    print(next(it), next(it))
    print(isinstance(c, __import__("collections.abc").Iterator))  # False
