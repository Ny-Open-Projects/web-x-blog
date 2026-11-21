"""漏斗转化率的置信区间:单步 Wilson 区间与两版本差异区间"""

import math
from statistics import NormalDist

Z = NormalDist().inv_cdf(0.975)  # 95% 置信


def wilson(success, n, z=Z):
    """Wilson 区间:小样本或低转化率下比正态近似更稳"""
    if n == 0:
        return 0.0, 0.0, 0.0
    p = success / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z / denom * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return p, center - half, center + half


def two_proportion(s1, n1, s2, n2, z=Z):
    """两组转化率之差的置信区间,0 不在区间内即认为差异显著"""
    p1, p2 = s1 / n1, s2 / n2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    diff = p2 - p1
    return diff, diff - z * se, diff + z * se


if __name__ == "__main__":
    funnel = [("访问", 10000, 3200), ("加购", 3200, 900), ("支付", 900, 540)]
    print("步骤  转化率     95% CI")
    prev_n = None
    for name, n, succ in funnel:
        base = prev_n if prev_n is not None else n
        p, lo, hi = wilson(succ, base)
        print(f"{name}  {p:.1%}  [{lo:.1%}, {hi:.1%}]")
        prev_n = succ
    d, lo, hi = two_proportion(900, 3200, 540, 1000)
    print(f"\n新版支付转化 - 旧版 = {d:+.1%},95% CI [{lo:+.1%}, {hi:+.1%}]")
    print("结论:", "显著提升" if lo > 0 else "尚不能认为有显著差异")
