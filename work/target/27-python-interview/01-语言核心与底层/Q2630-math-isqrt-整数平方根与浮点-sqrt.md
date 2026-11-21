---
title: [Q2630] math.isqrt:整数平方根与浮点 sqrt 的精度陷阱
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2630 · math.isqrt:整数平方根与浮点 sqrt 的精度陷阱

> 难度:★★★☆☆ | 标签:math, isqrt, 精度

**问**:`int(math.sqrt(n))` 有什么坑?isqrt 是怎么解决的?

**答**:`math.sqrt` 返回 float,超出 2**53 的整数无法精确表示,开方结果的舍入方向不可控,`int(math.sqrt(n))` 会差 1——实测 `(10**8 + 1)**2 - 1` 的真平方根是 `10**8`,而 float 开方舍入后 `int` 得到 `10**8 + 1`。`math.isqrt`(3.8+)是整数域精确解:返回不超过 n 的最大整数平方根,对任意大整数都正确,大数场景(密码学、数论、坐标整除)必须用它。判断完全平方数的正确姿势也由此而来:`isqrt(n) ** 2 == n`,不要用 `sqrt` 后比较。记忆口诀:整数进整数出,别让 float 当搬运工。

```python
# file: code/01_语言核心与底层/q2630_isqrt.py
"""isqrt 与 sqrt 的精度分界:一个实测的 off-by-one 反例。"""
import math


def is_perfect_square(n):
    r = math.isqrt(n)
    return r * r == n


if __name__ == "__main__":
    x = (10**8 + 1) ** 2 - 1
    print("真值 isqrt:      ", math.isqrt(x))
    print("float 开方 int:  ", int(math.sqrt(x)), "(错了 1)")
    print("完全平方判定:", is_perfect_square(x), is_perfect_square(x + 1))

    big = 10**18 + 1
    print("大整数 isqrt:", math.isqrt(big), "精确无误差")

    try:
        math.isqrt(10**18 + 0.5)
    except TypeError as exc:
        print("isqrt 只收整数:", exc)
```

**追问**:1) isqrt 对负数会怎样?——抛 ValueError,平方根在整数域对负数无定义;float 的 sqrt 会返回复数域报错同样,两者都要求非负。2) isqrt 的意义?——大整数平方根的精确整数结果;float sqrt 超过 2^53 后精度丢失,isqrt 永远精确;配合 pow 的模平方根(crypto)场景。3) 与 math.trunc(sqrt()) 的差异?——trunc(sqrt(10**30)) 有浮点误差,isqrt 精确;floor 语义与 isqrt 一致(非负整数);边界 0/1。4) 生产陷阱?——用 float sqrt 处理大数(精度);负数入参;以为 sqrt 返回整数类型;大数乘法溢出认知(int 无溢出但 str 转换有限制,Q557)。
