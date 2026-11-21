"""in 的回退链:__contains__ 优先,其次 __iter__,最后旧式 __getitem__。"""


class OnlyContains:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        print(f"    OnlyContains.__contains__({item!r})")
        return item in self.data


class OnlyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        print("    OnlyIterable 走迭代逐元素比较")
        return iter(self.data)


class OnlyGetItem:
    """只实现 __getitem__:旧式协议,in 按下标从 0 起试探。"""

    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        print(f"    OnlyGetItem.__getitem__({index})")
        return self.data[index]


class Nothing:
    pass


if __name__ == "__main__":
    print("2 in OnlyContains:")
    print("    结果:", 2 in OnlyContains([1, 2, 3]))

    print("3 in OnlyIterable:")
    print("    结果:", 3 in OnlyIterable([1, 2, 3]))

    print("'b' in OnlyGetItem:")
    print("    结果:", "b" in OnlyGetItem("abc"))

    try:
        1 in Nothing()
    except TypeError as exc:
        print("in Nothing:", exc)
