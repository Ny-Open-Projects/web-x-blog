---
title: [Q538] decimal:货币与精度工程
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q538 · decimal:货币与精度工程

> 难度:★★★☆ | 标签:decimal, 精度

**问**:为什么货币计算不能用 float?Decimal 的精度规则和 float 有什么本质不同?

**答**:float 是二进制浮点,0.1 这类十进制小数本身表示不准,累加与舍入误差在金额上不可接受(财务对账差一分钱都是事故);Decimal 是十进制浮点,0.1 精确存储,运算按声明的精度(prec,默认 28 位有效数字)十进制舍入。规则:构造一律用字符串 Decimal("19.99"),从 float 构造会带入二进制误差;除法可能除不尽时按 prec 舍入,展示层用 quantize(Decimal("0.01"), ROUND_HALF_UP) 显式定舍入位;context 是线程本地还是全局要注意(python 3.14 前是线程局部副本)。高性能大批量场景退回「整数分」方案。

```python
# file: code/01_语言核心与底层/q538_decimal.py
from decimal import Decimal, ROUND_HALF_UP, getcontext

if __name__ == "__main__":
    print("exact addition:", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

    total = Decimal("19.99") * 3
    print("total:", total)
    print("per 7:", (total / 7).quantize(Decimal("0.01"), ROUND_HALF_UP))

    getcontext().prec = 4
    print("precision 4:", Decimal(2) / Decimal(3))
    getcontext().prec = 28

    print("float ctor keeps error:", Decimal(0.1))
    print("str ctor is exact   :", Decimal("0.1"))
```

**追问**:1) Decimal 和 Fraction 怎么选?——Fraction 是精确有理数(1/3 存为分子分母),适合数学推导与符号计算;Decimal 是十进制定点风格,贴合货币与人类十进制习惯;两者都慢于 float。2) Decimal 为什么贴货币?——十进制表示无 0.1 类表示误差,精度位数与舍入模式(ROUND_HALF_UP 等)显式可控;float 的二进制舍入与会计规则天然冲突。3) 上下文机制?——精度与舍入由当前 Context 决定(getcontext 按线程独立);构造必须用字符串 Decimal("0.1"),从 float 构造会继承误差。4) 生产陷阱?——Decimal 与 float 混算 TypeError;ORM 把 Numeric 列映射成 float 丢精度,要显式 Decimal;全局改 context 精度影响其他模块。
