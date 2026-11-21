"""Q2582 embedding 归一化的必要性实测:余弦等价于归一后的点积。

数学事实:cos(a,b) = dot(norm(a), norm(b));工程后果:检索库若
没归一化,点积被模长主导,方向完全相同的两向量点积可以任意大。
本实验用小向量实测定量关系。
"""
import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def normalize(v):
    n = norm(v) or 1.0
    return [x / n for x in v]


def cosine_raw(a, b):
    return dot(a, b) / (norm(a) * norm(b))


def main():
    a = [3.0, 4.0]
    b = [6.0, 8.0]      # 与 a 同方向,模长翻倍
    c = [-0.8, 0.6]     # 与 a 近似正交
    assert abs(cosine_raw(a, b) - 1.0) < 1e-12          # 方向完全相同
    assert abs(dot(normalize(a), normalize(b)) - cosine_raw(a, b)) < 1e-12
    assert abs(norm(normalize(a)) - 1.0) < 1e-12        # 归一后模长恒为 1
    raw_same = dot(a, b)          # 未归一点积:被模长放大
    raw_ortho = dot(a, c)         # 未归一点积:近正交仍可能为正
    assert abs(raw_same - 50.0) < 1e-12
    assert raw_ortho < 0.5 and cosine_raw(a, c) < 0.1
    print("dot a b =", raw_same, "但真实余弦 = 1.0,点积虚高 50 倍")
    print("dot a c =", round(raw_ortho, 4), "而余弦 =", round(cosine_raw(a, c), 4))
    print("结论:入库前统一归一化,点积才严格等价余弦。")


if __name__ == "__main__":
    main()
