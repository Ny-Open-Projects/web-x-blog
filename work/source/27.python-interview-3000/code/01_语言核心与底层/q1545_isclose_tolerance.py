import math


def naive_equal(a, b, eps=1e-9):
    return abs(a - b) < eps


if __name__ == "__main__":
    print("0.1+0.2 == 0.3 :", 0.1 + 0.2 == 0.3)
    print("isclose default:", math.isclose(0.1 + 0.2, 0.3))

    # 大数:绝对差 0.1,但相对误差极小——朴素 eps 误判
    big_a, big_b = 1e12, 1e12 + 0.1
    print("big naive:", naive_equal(big_a, big_b),
          "| isclose:", math.isclose(big_a, big_b))

    # 接近零:rel_tol 失效,必须给 abs_tol
    print("tiny vs 0 default:", math.isclose(1e-12, 0.0),
          "| with abs_tol:", math.isclose(1e-12, 0.0, abs_tol=1e-9))

    # 累加误差:sum 与 fsum 的对比(呼应 Q537)
    vals = [0.1] * 10
    print("sum:", repr(sum(vals)), "| fsum:", repr(math.fsum(vals)),
          "| isclose to 1.0:", math.isclose(sum(vals), 1.0))

    # isclose 对称
    print("symmetric:", math.isclose(100.0, 100.1, rel_tol=1e-3) ==
          math.isclose(100.1, 100.0, rel_tol=1e-3))
