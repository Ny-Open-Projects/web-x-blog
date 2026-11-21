class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        if isinstance(other, int):
            return Vector(self.x + other, self.y + other)
        return NotImplemented             # 哨兵:交给对方或失败

    __radd__ = __add__                    # 10 + v 分派到 v.__radd__(10)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

if __name__ == "__main__":
    v = Vector(1, 2)
    print(v + Vector(3, 4))
    print(v + 10)                         # v.__add__(10)
    print(10 + v)                         # int 不支持 → v.__radd__(10)
    try:
        v + "x"                           # 双方都 NotImplemented
    except TypeError as e:
        print("TypeError:", e)
