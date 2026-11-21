from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Point:
    x: float
    y: float = 0.0

@dataclass
class Basket:
    items: list[str] = field(default_factory=list)
    total: int = field(init=False, default=0)

    def __post_init__(self):
        self.total = len(self.items)

    def add(self, item: str):
        self.items.append(item)
        self.total = len(self.items)

if __name__ == "__main__":
    print(Point(1, 2) < Point(3))
    b = Basket(["apple"])
    b.add("pear")
    print(b)                     # 自动 __repr__
    print(b == Basket(["apple", "pear"]))

    try:
        Point(1, 2).x = 9
    except Exception as e:
        print(type(e).__name__, e)   # frozen 禁止赋值
