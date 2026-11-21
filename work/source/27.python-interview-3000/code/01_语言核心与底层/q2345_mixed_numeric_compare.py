"""数值类型混合比较:int、float、Fraction、Decimal 的互操作性。"""
import math
from decimal import Decimal
from fractions import Fraction

if __name__ == "__main__":
    f = 0.1 + 0.2
    d = Decimal("0.3")
    fr = Fraction(3, 10)
    print("float  :", repr(f))
    print("Decimal:", d, "| Fraction:", fr)

    print("float > Fraction(精确比较):", f > fr)
    print("Decimal == Fraction:", d == fr)
    print("Decimal == float:", d == f)
    print("int == Decimal/Fraction:", 1 == Decimal("1.0"), 2 == Fraction(4, 2))

    nums = [Decimal("0.5"), Fraction(1, 3), 0.75, 2, -1]
    print("混合排序:", sorted(nums))

    print("nan 的有序比较恒 False:", math.nan > 1, math.nan == math.nan)
