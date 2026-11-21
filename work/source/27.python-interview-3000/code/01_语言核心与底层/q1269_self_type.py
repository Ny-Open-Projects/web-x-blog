from __future__ import annotations

from typing import TypeVar

T = TypeVar("T", bound="Shape")       # 3.11+ 可直接 from typing import Self


class Shape:
    def move(self: T, dx: float) -> T:
        self.x = getattr(self, "x", 0.0) + dx
        return self

    def scale(self: T, k: float) -> T:
        self.k = getattr(self, "k", 1.0) * k
        return self


class Circle(Shape):
    pass


if __name__ == "__main__":
    c = Circle().move(3).scale(2)     # 静态检查器知道整条链都是 Circle
    print(type(c).__name__, c.x, c.k)
    s = Shape().move(1)
    print(type(s).__name__, s.x)
