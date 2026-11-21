"""property setter 的副作用设计:归一化与派生字段联动。"""


class Rectangle:
    def __init__(self, width, height):
        self._w = self._h = 0.0
        self.area = 0.0            # 派生字段,由 setter 联动维护
        self.width = width         # 走 setter 完成校验与归一化
        self.height = height

    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width 必须为正数")
        self._w = float(value)
        self._sync_area()

    @property
    def height(self):
        return self._h

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height 必须为正数")
        self._h = float(value)
        self._sync_area()

    def _sync_area(self):
        self.area = self._w * self._h


if __name__ == "__main__":
    r = Rectangle(3, 4)
    print("初值:", r.width, r.height, "面积:", r.area)
    r.width = 10                   # setter 联动刷新派生字段
    print("改宽后:", r.width, "面积:", r.area)
    try:
        r.height = -1
    except ValueError as e:
        print("非法值被 setter 拦下:", e)
    print("面积未被污染:", r.area)
