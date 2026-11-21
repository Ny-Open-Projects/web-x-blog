"""+= 的返回值契约:__iadd__ 的返回值会成为左侧名字的新绑定。"""


class Gauge:
    """正确示范:原地修改并 return self。"""

    def __init__(self, value):
        self.value = value

    def __iadd__(self, delta):
        self.value += delta
        return self


class BrokenGauge:
    """反面教材:只改内部忘了 return,隐式返回 None。"""

    def __init__(self, value):
        self.value = value

    def __iadd__(self, delta):
        self.value += delta
        # 缺了 return self


if __name__ == "__main__":
    a, b = [1, 2], None
    b = a
    a += [3]
    print("list += 原地改,b 同步变化:", b)

    t, alias = (1, 2), None
    alias = t
    t += (3,)
    print("tuple += 新建对象,alias 不动:", alias, "| t:", t)

    g = Gauge(10)
    g += 5
    print("Gauge += 后:", g.value)

    bg = BrokenGauge(10)
    bg += 5
    print("BrokenGauge += 后左侧名字变成:", bg)
