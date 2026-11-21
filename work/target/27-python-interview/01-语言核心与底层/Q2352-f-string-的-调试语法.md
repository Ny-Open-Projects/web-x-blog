---
title: [Q2352] f-string 的 = 调试语法
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2352 · f-string 的 = 调试语法

> 难度:★★★☆☆ | 标签:f-string, 调试, 3.8 新特性

**问**:f"{x=}" 输出的是什么?调试时它比 print(f"val: {x}") 好在哪?

**答**:3.8 起 f-string 支持 `=` 修饰:表达式文本、等号、值的 repr 一次输出,`f"{radius=}"` 得到 `radius=2.5`。价值在于「所见即所测」:变量名不再手打两遍,复制粘贴时也不会名实不符——手写 print 很容易打印的标签和实际取的变量对不上,= 语法在语言层杜绝了这种漂移。它还能带格式说明(`f"{x=:.2f}"`,先输出表达式再按 spec 格式化值)、控制等号两侧空格(`f"{x = }"`)、用于属性访问与任意表达式(`f"{point.real=}"`、`f"{area(r)=:.3f}"`)。边界要清楚:= 捕获的是源代码文本,经过的变量重绑定它不知道;输出用 repr,想看 str 形式要显式格式化。它是轻量级 print 调试的最佳形态,但多变量、多轮次的排查仍应升级为表格化输出或日志。

```python
# file: code/01_语言核心与底层/q2352_fstring_debug.py
"""f-string 的 = 调试语法:一行同时输出表达式与值。"""
import math


def area(r):
    return math.pi * r ** 2


if __name__ == "__main__":
    radius = 2.5
    name = "圆"
    print(f"{radius=}")
    print(f"{name=}")
    print(f"{area(radius)=:.3f}")
    print(f"{radius * 2=}")
    print(f"{radius = }")
    print(f"{radius=:>10.2f}")

    point = complex(3, 4)
    print(f"{point.real=}")
    print(f"{point ** 2=}")
```

**追问**:1) = 输出的值一定是 repr 吗?——默认走 repr(字符串会带引号),想换 str 形式加 !s 或 !r 显式指定:`f"{name=!s}"`。2) = 语法的机制?——输出「表达式文本 + 求值结果」,表达式在等号前原样保留(含空格格式);3.8+ 语法;调试输出自带上下文,不再手写 "name=" 前缀。3) 与日志的分工?——= 是「人看的现场快照」;正式日志走 logging + %s 惰性格式化(Q503);不要把 f-string 调试行留在生产。4) 生产陷阱?——= 调试行混进提交;复杂表达式在等号前过长;默认 repr 让字符串输出带引号被误读为字面量。
