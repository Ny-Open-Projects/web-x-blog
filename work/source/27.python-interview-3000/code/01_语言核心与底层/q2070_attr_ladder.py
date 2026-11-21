"""属性访问性能阶梯:实例字典、__slots__、property、描述符与 __getattr__。"""
import timeit


class DictPoint:
    """普通类:属性在实例 __dict__ 里。"""
    def __init__(self, x):
        self.x = x


class SlotPoint:
    """__slots__:固定槽位偏移访问。"""
    __slots__ = ("x",)

    def __init__(self, x):
        self.x = x


class PropPoint:
    """property:每次读取都是一次函数调用。"""
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x


class DescPoint:
    """非数据描述符:比 property 多一层协议分派。"""
    class TenX:
        def __get__(self, obj, cls):
            return obj._x * 10 if obj else self
    x = TenX()

    def __init__(self, x):
        self._x = x


class GetattrPoint:
    """__getattr__ 兜底:常态查找失败后才触发,最慢。"""
    def __init__(self, x):
        self._store = {"x": x}

    def __getattr__(self, name):
        if name == "x":
            return self._store["x"]
        raise AttributeError(name)


def bench(cls, number=200000):
    p = cls(21)
    best = min(timeit.repeat("p.x", globals={"p": p}, number=number, repeat=3))
    return best / number * 1e9


if __name__ == "__main__":
    for cls in (DictPoint, SlotPoint, PropPoint, DescPoint, GetattrPoint):
        print(f"{cls.__name__:13} {bench(cls):7.1f} ns/op")
    print("阶梯:实例字典 约等于 slots < property < 描述符 < __getattr__ 未命中")
