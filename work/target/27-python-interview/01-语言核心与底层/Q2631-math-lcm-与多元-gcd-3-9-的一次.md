---
title: [Q2631] math.lcm 与多元 gcd:3.9 的一次成型
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2631 · math.lcm 与多元 gcd:3.9 的一次成型

> 难度:★☆☆☆☆ | 标签:math, lcm, 3.9 新特性

**问**:求最小公倍数以前为什么要手写?3.9 变了什么?

**答**:3.9 起 `math.lcm` 直接内置,而且和 `math.gcd` 一样支持任意多个参数:`math.lcm(4, 6, 10)` 一步得到 60。此前只能手写 `a * b // math.gcd(a, b)` 再自己叠 reduce,还要小心 a*b 溢出——Python 整数无所谓溢出,但手写终究是重复代码。典型用途:多个周期的对齐时间点、分母通分、调度任务的最小公共间隔。与 `math.gcd` 一样,参数为 0 时 lcm 定义为 0,负数按绝对值处理,与数学约定一致。

```python
# file: code/01_语言核心与底层/q2631_math_lcm.py
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
```

**追问**:1) lcm 参数很多时会怎样?——多元 lcm 是逐对归约实现的,结果可能非常大,Python 大整数直接扛住,不存在溢出问题。2) lcm/gcd 的语义?——math.gcd/lcm(3.9 起 lcm)接受任意多参;gcd(0,n)=n;lcm 结果位数 = 各参数质因数并集;与 fractions.gcd(旧)的区别。3) 与 pow 的组合?——模运算场景 pow(a, b, m) 模幂(Q1292);lcm/gcd 常用于周期归并与对齐;functools.reduce(math.gcd, xs) 与多参等价。4) 生产陷阱?——自己写 gcd 循环(标准库有);lcm 爆炸后的 str 转换触发 3.11+ 位数限制(Q557);0 参与 lcm 语义误解。
