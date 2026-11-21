---
title: [Q882] 浮点与 DECIMAL: 金额计算的底线
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q882 · 浮点与 DECIMAL: 金额计算的底线

> 难度:★★☆☆ | 标签:数据类型, 精度

**问**:为什么金额字段不能用 float/double?0.1 + 0.2 != 0.3 怎么回事?

**答**:IEEE-754 浮点用二进制尾数表示,0.1 这类十进制小数无法精确表示,累加误差会累积,对账时出现 0.0099999 之类的分毫差异。数据库层金额用 DECIMAL(M,D)(MySQL)精确十进制;应用层用 decimal.Decimal,或更常见的"分为单位存 bigint"——整数没有精度问题且运算快。SQLite 没有独立 DECIMAL 类型,REAL 即浮点,所以演示里用"分"整数或 Decimal 在应用层处理,落库存整数分。比较浮点相等要用误差容忍,但金额场景直接换类型才是根治。

```python
# file: code/04_数据库与缓存/q882_float_decimal.py
"""浮点误差演示与两种金额方案: Decimal 与整数分"""
from decimal import Decimal

if __name__ == "__main__":
    print("浮点:", 0.1 + 0.2, "== 0.3 ?", (0.1 + 0.2) == 0.3)
    print("Decimal:", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

    price = Decimal("19.99")
    qty = 3
    print("Decimal 金额:", price * qty)

    cents = 1999                       # 库里存分
    print("整数分金额:", cents * qty, "分 =", cents * qty / 100, "元")
    print("浮点做账的坑: 19.99 * 3 =", 19.99 * 3)
```

**追问**:
- DECIMAL(10,2) 的含义?——总共 10 位数字、其中 2 位小数,最大 99999999.99,超范围报错而不是静默截断。
- SUM 浮点列结果每次不同吗?——顺序相关,浮点加法不满足结合律,聚合顺序不同结果可能在末位抖动,对账场景必须用精确类型。

---
