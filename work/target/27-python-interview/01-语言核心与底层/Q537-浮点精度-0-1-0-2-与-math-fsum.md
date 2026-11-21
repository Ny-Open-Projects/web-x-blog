---
title: [Q537] 浮点精度:0.1+0.2 与 math.fsum
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q537 · 浮点精度:0.1+0.2 与 math.fsum

> 难度:★★★☆ | 标签:浮点数, IEEE 754

**问**:0.1 + 0.2 为什么不等于 0.3?求和时怎么把累积误差压到最小?

**答**:二进制浮点无法精确表示 0.1(它是二进制下的无限循环小数),0.1 实际存储是略大/略小的近似值,两个近似值相加再四舍五入,结果与 0.3 的近似值差一位尾数。解决按场景:比较用 math.isclose(带相对误差);求和用 math.fsum(维护精确部分和,Shewchuk 算法,一次舍入);货币用 Decimal 或以「分」为单位的整数。更深的坑:大数吃小数(1e16 + 1.0 == 1e16),因为尾数只有 53 位,加法结果超出精度直接被舍去——累加大数时顺序都会影响结果。

```python
# file: code/01_语言核心与底层/q537_float_precision.py
import math

if __name__ == "__main__":
    print("0.1 + 0.2 =", 0.1 + 0.2)
    print("equals 0.3:", (0.1 + 0.2) == 0.3)
    print(f"0.1 in binary-ish: {0.1:.20f}")
    print("isclose:", math.isclose(0.1 + 0.2, 0.3))

    nums = [0.1] * 10
    print("naive sum == 1.0:", sum(nums) == 1.0)
    print("fsum == 1.0   :", math.fsum(nums) == 1.0)

    print("big eats small:", 1e16 + 1.0 - 1e16)
    print("fsum resists  :", math.fsum([1e16, 1.0, -1e16]))
```

**追问**:1) 为什么 fsum 能精确?——它把中间结果按精度分层暂存(部分和数组),最终只舍入一次;代价是慢与额外内存,只用于求和这一种运算。2) 0.1+0.2 != 0.3 的根源?——0.1/0.2 在二进制浮点里不可精确表示,相加结果是「两个近似值的和再近似」;比较必须 math.isclose 或误差阈值,不能 ==。3) 普通 sum 的误差模型?——每步都做一次 IEEE 舍入,误差累积与顺序相关:同一组数不同顺序结果不同,fsum 消除顺序依赖。4) 生产陷阱?——金额累加用 float 对不上账,应 Decimal;测试断言 float 相等导致跨平台 flaky;统计大数吃小数(累加大数组时小项被吸收),关键场景 fsum。
