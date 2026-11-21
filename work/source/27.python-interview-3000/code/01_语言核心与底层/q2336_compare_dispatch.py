"""比较运算的分派顺序:正向方法优先,拒绝后反射到对方。"""


class Temperature:
    """摄氏温度:__lt__ 只处理同类,__gt__ 只处理数字,演示双向分派。"""

    def __init__(self, celsius):
        self.celsius = celsius

    def __lt__(self, other):
        print(f"    调 __lt__ self={self.celsius} other={other!r}")
        if isinstance(other, Temperature):
            return self.celsius < other.celsius
        return NotImplemented            # 礼貌拒绝,交给对方反射

    def __gt__(self, other):
        print(f"    调 __gt__ self={self.celsius} other={other!r}")
        if isinstance(other, (int, float)):
            return self.celsius > other
        return NotImplemented


if __name__ == "__main__":
    cold, hot = Temperature(10), Temperature(30)

    print("cold < hot:")
    print("    结果:", cold < hot)        # 正向 __lt__ 一次成功

    print("25 < hot: int.__lt__ 不认识 Temperature,反射到 hot.__gt__")
    print("    结果:", 25 < hot)

    print("hot < 25: __lt__ 拒绝,int 的 __gt__ 也不认识 Temperature")
    try:
        hot < 25
    except TypeError as exc:
        print("    TypeError:", exc)

    print("sorted 只依赖 <:", [t.celsius for t in sorted([hot, cold])])
