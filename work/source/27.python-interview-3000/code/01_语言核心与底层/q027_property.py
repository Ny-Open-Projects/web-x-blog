class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius must be non-negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2   # 只读派生属性

if __name__ == "__main__":
    c = Circle(1)
    print(round(c.area, 4))
    c.radius = 2
    print(round(c.area, 4))
    try:
        c.radius = -1
    except ValueError as e:
        print("rejected:", e)
