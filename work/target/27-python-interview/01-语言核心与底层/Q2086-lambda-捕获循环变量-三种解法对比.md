---
title: [Q2086] lambda 捕获循环变量:三种解法对比
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2086 · lambda 捕获循环变量:三种解法对比

> 难度:★★★☆☆ | 标签:闭包, late binding, lambda

**问**:循环里创建的 lambda 全都返回最后一个 i,三种修复方案各自的取舍是什么?

**答**:根因是 late binding(见 Q017):闭包捕获的是变量 i 本身而非当时的值,循环结束 i 停在最后一个元素。三种解法本质都是「把值固定进独立存储」:解法一默认参数 lambda i=i: i,利用默认值在 def 时求值一次的规则,最快最短,缺点是语法魔术 newcomers 看不懂;解法二 functools.partial(func, i),把实参固化为部分应用,语义显式、可复用同一函数对象,代价是多一层调用;解法三工厂闭包 make(i) 返回新函数,每个闭包有独立作用域,适合多参数多行逻辑,代码量最大。批量创建回调、信号槽、延迟任务里三选一:单参数选默认参数,复用现成函数选 partial,复杂逻辑选工厂。

```python
# file: code/01_语言核心与底层/q2086_lambda_capture.py
"""lambda 捕获循环变量:late binding 的三种解法。"""
import functools


def naive():
    return [lambda: i for i in range(3)]           # 全部看到最终的 i


def fix_default():
    return [lambda i=i: i for i in range(3)]       # 解法一:默认参数定义时绑定


def fix_partial():
    return [functools.partial(lambda v: v, i) for i in range(3)]   # 解法二:固化实参


def fix_factory():
    def make(v):
        return lambda: v
    return [make(i) for i in range(3)]             # 解法三:工厂制造独立作用域


if __name__ == "__main__":
    for name, builder in [("天真写法", naive), ("默认参数", fix_default),
                          ("partial", fix_partial), ("工厂闭包", fix_factory)]:
        print(f"{name}: {[cb() for cb in builder()]}")
```

**追问**:1) 三解法怎么选?——单参数要快选默认参数,复用现成函数选 partial,多参多行选工厂闭包;late binding 的根因?——闭包存的是单元格引用而非值快照,循环结束时单元格停在最后值。2) 晚绑定的机制细节?——同一循环的 lambda 共享同一个 cell(Q527);默认参数在 def 时求值是快照;partial 固化求值后的值——三者「绑定时刻」不同。3) 异步场景的放大效应?——asyncio.create_task(coro(i)) 循环变量错位是高频 bug;create_task 用 kwargs 或工厂;日志回调同理。4) 生产陷阱?——批量注册回调全是最后一个值;修复用默认参数但参数名与调用方冲突;工厂闭包又引用外层可变量。
