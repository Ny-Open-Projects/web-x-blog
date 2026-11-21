---
title: [Q2345] 数值混合比较:float、Decimal 与 Fraction 同场
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2345 · 数值混合比较:float、Decimal 与 Fraction 同场

> 难度:★★★★☆ | 标签:Decimal, Fraction, 数值比较

**问**:Decimal("0.3")、0.3 和 Fraction(3, 10) 互相比较结果是什么?混合排序安全吗?

**答**:数值类型之间可以互相比较,而且规则比想象中严格:Fraction 与 float 比较走精确有理数运算,0.1+0.2(实际是 0.30000000000000004)会正确地大于 3/10;Decimal 与 float 的比较也是精确的,把 float 看成它真实的二进制值再比,所以 Decimal("0.3") == 0.3 是 False;Decimal 与 Fraction 比较时两边都精确展开,Decimal("0.3") == Fraction(3,10) 是 True。混合排序因此天然安全,sorted 能直接处理四种类型混排,不必先统一类型。真正会破坏一切的是 NaN:任何与 NaN 的有序比较都是 False,排序结果不可预期。这组语义的价值在于:数值口径不一致时,「比较」比「相等」可靠,而最可靠的做法是排序与聚合前统一转 Fraction 或 Decimal。

```python
# file: code/01_语言核心与底层/q2345_mixed_numeric_compare.py
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
```

**追问**:1) Decimal 和 float 之间能直接做加减吗?——比较可以、算术不行,`Decimal("0.3") + 0.1` 抛 TypeError,必须先统一类型;这正是「比较精确、运算设防」的设计。2) 混合比较的机制?——数值类型按精确实数互比(Fraction 最精确、float 转精确分数再比,Q1543);比较规则统一由 IEEE/数值塔定义,但算术只在同类或可提升类型间。3) bool/int/float 的混算?——bool 是 int(Q539)、int 自动升 float;Decimal 与 Fraction 不互算;金额场景统一 Decimal。4) 生产陷阱?——比较通过后直接混算崩;float 精度进入 Decimal(Decimal(0.1) 带误差,Q1542);NaN 让所有比较 False(Q534)。
