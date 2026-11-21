import operator

class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return iter(range(self.n, 0, -1))

    def __length_hint__(self):
        return self.n                     # 提示:大约 n 个,允许不准

if __name__ == "__main__":
    c = Countdown(5)
    print("length_hint:", operator.length_hint(c))
    print("materialized:", list(c))
    print("hint of plain generator:", operator.length_hint(x for x in range(3)))
