"""isqrt 与 sqrt 的精度分界:一个实测的 off-by-one 反例。"""
import math


def is_perfect_square(n):
    r = math.isqrt(n)
    return r * r == n


if __name__ == "__main__":
    x = (10**8 + 1) ** 2 - 1
    print("真值 isqrt:      ", math.isqrt(x))
    print("float 开方 int:  ", int(math.sqrt(x)), "(错了 1)")
    print("完全平方判定:", is_perfect_square(x), is_perfect_square(x + 1))

    big = 10**18 + 1
    print("大整数 isqrt:", math.isqrt(big), "精确无误差")

    try:
        math.isqrt(10**18 + 0.5)
    except TypeError as exc:
        print("isqrt 只收整数:", exc)
