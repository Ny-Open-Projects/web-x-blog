"""实现 cosine、内积、欧氏距离并对比;演示归一化后内积等于 cosine。"""
import math


def cosine(a: list[float], b: list[float]) -> float:
    num = sum(x * y for x, y in zip(a, b))
    return num / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


def inner(a, b):
    return sum(x * y for x, y in zip(a, b))


def euclid(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def normalize(v: list[float]) -> list[float]:
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v]


if __name__ == "__main__":
    q = [1.0, 2.0, 3.0]
    good = [1.2, 2.1, 2.9]   # 语义相近
    bad = [3.0, 1.0, 0.5]    # 语义无关
    for name, fn in [("cosine", cosine), ("inner", inner), ("euclid", euclid)]:
        print(f"{name}: 相关={fn(q, good):.3f} 无关={fn(q, bad):.3f}")
    print("归一化后 inner(q,good) =", round(inner(normalize(q), normalize(good)), 3),
          "== cosine:", round(cosine(q, good), 3))
