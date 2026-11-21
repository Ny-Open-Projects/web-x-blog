"""math.lcm:3.9 的多元最小公倍数。"""
import math
from functools import reduce


def lcm_old(*nums):
    """3.9 之前的手写姿势,留作对照。"""
    return reduce(lambda a, b: a * b // math.gcd(a, b), nums)


if __name__ == "__main__":
    print("math.lcm(4, 6, 10):", math.lcm(4, 6, 10))
    print("lcm_old(4, 6, 10): ", lcm_old(4, 6, 10))
    print("math.gcd(12, 18):  ", math.gcd(12, 18))

    periods = [3, 5, 7]
    print("三个周期对齐:", math.lcm(*periods), "个单位后重合")

    print("含 0 的约定:", math.lcm(0, 5), "含负数:", math.lcm(-4, 6))
