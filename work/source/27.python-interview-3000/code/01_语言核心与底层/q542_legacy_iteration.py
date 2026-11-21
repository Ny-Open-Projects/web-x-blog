from collections.abc import Iterable

class OldStyle:
    """只有 __getitem__:旧式序列协议,依然可迭代"""
    def __getitem__(self, i):
        if i > 2:
            raise IndexError
        return i * i

if __name__ == "__main__":
    o = OldStyle()
    print("for works:", list(o), [x for x in o])
    print("iter + next:", next(iter(o)))

    print("isinstance Iterable:", isinstance(o, Iterable))   # False:协议按 __iter__ 判定
    print("yet iteration works — legacy protocol in action")
