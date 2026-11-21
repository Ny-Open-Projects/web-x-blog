---
title: [Q2613] and/or 的短路字节码:返回的是操作数不是 bool
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2613 · and/or 的短路字节码:返回的是操作数不是 bool

> 难度:★★☆☆☆ | 标签:短路求值, 字节码, 布尔语义

**问**:`x and y` 的求值规则是什么?为什么 `0 and 1/0` 不会抛 ZeroDivisionError?

**答**:`and`/`or` 走短路求值,字节码上是条件跳转指令:`and` 编译为 `JUMP_IF_FALSE_OR_POP`(左值为假直接把它作为整个表达式的值跳走),`or` 对应 `JUMP_IF_TRUE_OR_POP`。关键语义是:表达式返回的是**决定结果的那个操作数本身**,不是转成 bool 之后的值——所以 `0 and 1/0` 返回 0,右边的除法根本不求值;`[] or "default"` 返回 "default" 而不是 True。这就是「默认值惯用法」的来源,但也要小心它的陷阱:`0 or ""` 返回空串,用 or 提供默认值会把合法的假值一起吞掉,明确「缺失」语义时应该用 `is None` 判断。

```python
# file: code/01_语言核心与底层/q2613_andor_bytecode.py
"""and/or 的短路字节码与操作数返回语义。"""
import dis


def pick(a, b):
    return a or b


if __name__ == "__main__":
    dis.dis(pick)                      # 看 JUMP_IF_TRUE_OR_POP

    print("0 and 1/0 =", 0 and 1 / 0)          # 0,右侧不求值
    print("[] or 'default' =", [] or "default")  # 返回操作数本身
    print("0 or '' =", repr(0 or ""))          # 空串,假值陷阱
    print("None or 0 =", repr(None or 0))      # 0

    x = None
    print("x is None 判缺失:", "default" if x is None else x)
```

**追问**:1) 链式 `a or b or c` 的短路点在哪里?——从左到右逐个判定,第一个真值立即成为整个表达式的值,右侧全部不求值,字节码上是多个跳转目标指向同一条 RETURN。2) 「返回操作数」的语义?——JUMP_IF_TRUE 按真值跳转,返回值是操作数对象本身(不是 bool),所以 `0 or "x"` 得 "x"、`"" or []` 得 [];这就是 or 默认值行为与陷阱的来源(Q2082)。3) 与 and 的对称?——and 在第一个假值处短路返回它;两者配合的「默认值链」与「守卫链」;is None 判断不可被 or 替代(0/空串合法时)。4) 生产陷阱?——or 默认覆盖 falsy 合法值;把 or 链当 bool 输出(得到操作数);依赖短路做副作用编排。
