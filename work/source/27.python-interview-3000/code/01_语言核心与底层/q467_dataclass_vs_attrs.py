from dataclasses import dataclass, asdict

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Port:
    """手写 attrs 风格校验:借 __post_init__"""
    number: int

    def __post_init__(self):
        if not (0 < self.number < 65536):
            raise ValueError(f"invalid port {self.number}")

if __name__ == "__main__":
    p = Point(1, 2)
    print(asdict(p))
    print(Point("a", None))               # dataclass 运行时不校验类型
    try:
        Port(70000)
    except ValueError as e:
        print("hand validation:", e)
