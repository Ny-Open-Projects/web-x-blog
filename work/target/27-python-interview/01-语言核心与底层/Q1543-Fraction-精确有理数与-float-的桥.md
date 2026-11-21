---
title: [Q1543] Fraction:精确有理数与 float 的桥
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1543 · Fraction:精确有理数与 float 的桥

> 难度:★★★☆☆ | 标签:fraction, 精度, 有理数

**问**:需要精确的比例运算(概率、配比、利息分摊),Fraction 比 Decimal 强在哪?float 和 Fraction 之间怎么转换不丢真?

**答**:Fraction 是任意精度有理数:自动约分(gcd 归一)、四则运算永远精确,适合「比例本身必须精确」的概率、配比、分摊;Decimal 精确的是十进制小数,除不尽仍要按 prec 舍入。构造与转换:Fraction(3, 4)、Fraction("3/4")、Fraction(Decimal("0.75")) 都精确;Fraction(0.1) 得到的是该浮点值的精确分数(分母是 2 的幂),想要「人类以为的 1/10」用 limit_denominator() 还原。要点:① 与 float 比较时双方按精确实数处理,Fraction(1,3) > 0.333 成立靠精确值而非容差;② Fraction 与 Decimal 直接混算抛 TypeError,先构造再算;③ numerator/denominator 取分子分母,hash 与 int/float 统一体系,分摊时「最后一份兜底」可保证总和精确。

```python
# file: code/01_语言核心与底层/q1543_fraction_exact.py
from decimal import Decimal
from fractions import Fraction


def split_profit(total, ratios):
    """按精确比例分摊,最后一份兜底,保证总和精确等于 total。"""
    denom = sum(ratios)
    shares = [total * r / denom for r in ratios[:-1]]
    shares.append(total - sum(shares))
    return shares


if __name__ == "__main__":
    third = Fraction(1, 3)
    print("1/3 * 3 =", third * 3, "| float:", 1 / 3 * 3)

    f = Fraction(0.1)                   # float 的精确分数形态
    print("Fraction(0.1) =", f)
    print("limit_denominator:", f.limit_denominator(),
          "=", float(f.limit_denominator()))

    print("from str  :", Fraction("3/4"), Fraction("0.125"))
    print("from Dec  :", Fraction(Decimal("0.75")))
    print("auto gcd  :", Fraction(6, 8), "->",
          Fraction(6, 8).numerator, "/", Fraction(6, 8).denominator)
    print("compare   :", Fraction(1, 2) == 0.5, Fraction(1, 3) > 0.333)

    ratios = (Fraction(1, 3), Fraction(1, 4), Fraction(5, 12))
    shares = split_profit(Fraction(1000), ratios)
    print("shares:", shares, "sum:", sum(shares))

    try:
        Fraction(1, 2) + Decimal("0.5")
    except TypeError:
        print("Fraction + Decimal -> TypeError, 先构造再算:",
              Fraction(1, 2) + Fraction(Decimal("0.5")))
```

**追问**:1) Fraction 和 float 比较公平吗?——公平且精确:双方按精确实数比较,Fraction(1,3) > 0.333 靠精确值,不是容差。2) Fraction 的工程位?——精确比例(1/3 存分子分母)、与 Decimal 互转、limit_denominator 求近似分数;构造要从字符串/整数对,Fraction(0.1) 是二进制近似的分数化。3) 运算语义?——自动约分;与 float 比较按精确值(float 转 Fraction 比较,无舍入);哈希与相等值一致(Fraction(1,2) == 0.5 且哈希相同);代价是慢与大分母膨胀。4) 生产陷阱?——Fraction(0.1) 继承 float 误差,应 Fraction("0.1");连乘导致分母指数膨胀;序列化成字符串要保留 (num, den) 才无歧义。
