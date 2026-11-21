---
title: [Q1258] fast locals:局部变量槽与 locals() 的物化成本
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1258 · fast locals:局部变量槽与 locals() 的物化成本

> 难度:★★★☆☆ | 标签:字节码, 性能, 作用域

**问**:为什么函数里 `x = 1; x + 1` 比 `y['x'] = 1` 快得多?`locals()` 返回的是什么,改它有用吗?

**答**:函数内的局部变量编译期就定位到 `co_varnames` 槽位数组,字节码用 `LOAD_FAST` 按索引直取,是所有名字查找里最快的(对比 `LOAD_GLOBAL` 要查两套字典,见 Q548)。代价是 f_locals 默认不是字典:调用 `locals()` 或访问 `frame.f_locals` 时才把槽位数组物化成新字典,热循环里反复调 `locals()` 是可测出的开销;3.13 的 PEP 667 把 f_locals 改为真·代理视图,但「别在函数里改 locals()」的结论不变——那是未定义行为,优化器不保证回写。模块级与类体没有 fast locals(走 LOAD_NAME),这也是为什么「把热代码包进函数」总是更快。

```python
# file: code/01_语言核心与底层/q1258_fast_locals.py
import dis
import sys


def sample(a, b):
    c = a + b
    d = c * 2
    return d


if __name__ == "__main__":
    print("co_varnames:", sample.__code__.co_varnames)
    print("co_nlocals :", sample.__code__.co_nlocals)
    ops = [i.opname for i in dis.get_instructions(sample)]
    print("opnames    :", ops)

    captured = []
    def probe():
        x = 1
        captured.append(sys._getframe())
        return x
    probe()
    f = captured[0]
    print("f.f_locals is materialized snapshot:", f.f_locals)
    print("修改它不会影响原槽位 — 未定义行为,勿用")
```

**追问**:1) 为什么类体里 `x = 1; [x for _ in range(1)]` 会 NameError?——类体走 LOAD_NAME,而推导式有独立函数作用域,其 fast locals 里没有 x,只能查 globals(见 Q528)。2) 局部变量为什么快?——编译期定槽位,LOAD_FAST 按索引取帧内数组,零哈希;globals 要哈希查找加 builtins 回退,这是「局部变量化」优化的根据(Q548)。3) locals() 的物化机制?——调用时把 fast locals 拷成新字典(3.13 前是快照),改它不回写帧;exec/eval 里拿到的 locals 同样是拷贝。4) 生产陷阱?——热循环里调 locals() 做调试输出(物化成本);exec 中「修改 locals」不生效;依赖 locals() 键序的逻辑脆弱。
