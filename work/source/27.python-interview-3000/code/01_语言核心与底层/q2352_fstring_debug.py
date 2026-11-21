"""f-string 的 = 调试语法:一行同时输出表达式与值。"""
import math


def area(r):
    return math.pi * r ** 2


if __name__ == "__main__":
    radius = 2.5
    name = "圆"
    print(f"{radius=}")
    print(f"{name=}")
    print(f"{area(radius)=:.3f}")
    print(f"{radius * 2=}")
    print(f"{radius = }")
    print(f"{radius=:>10.2f}")

    point = complex(3, 4)
    print(f"{point.real=}")
    print(f"{point ** 2=}")
