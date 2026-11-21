---
title: [Q2091] 函数组合:compose 与 pipeline 的极简实现
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2091 · 函数组合:compose 与 pipeline 的极简实现

> 难度:★★★☆☆ | 标签:函数组合, 管道, 高阶函数

**问**:怎么用几行标准库代码实现函数组合?compose 和 pipeline 方向为什么相反?

**答**:两个组合器都是「闭包持函数序列,逐个应用」:compose 从右向左——compose(f, g)(x) 数学记法 f(g(x)),适合表达「先内后外」的嵌套语义;pipeline 从左向右——数据加工流水线按书写顺序执行,更贴阅读习惯,数据管道场景几乎总选它。实现只用一个 for 循环,不需要 reduce 技巧,可读性即正确性。组合的工程价值:把清洗、归一化、校验拆成单职责小函数,用组合拼装成流程,每节都能独立单测与复用;调试时插入一个 tap 函数(打印并原样返回)即可观测链路,不用拆掉组合。

```python
# file: code/01_语言核心与底层/q2091_compose.py
"""函数组合:compose 与 pipeline 的极简实现。"""


def compose(*funcs):
    """从右向左:compose(f, g)(x) == f(g(x))。"""
    def composed(value):
        for func in reversed(funcs):
            value = func(value)
        return value
    return composed


def pipeline(*funcs):
    """从左向右:pipeline(f, g)(x) == g(f(x))。"""
    def piped(value):
        for func in funcs:
            value = func(value)
        return value
    return piped


def squash(s):
    return "-".join(s.split())


if __name__ == "__main__":
    clean = pipeline(str.strip, str.lower, squash)
    print("pipeline:", clean("  Hello  World  "))
    print("compose 同链:", compose(squash, str.lower, str.strip)("  Hello  World  "))

    import functools
    via_reduce = functools.reduce(lambda acc, f: f(acc), [str.strip, str.lower, squash],
                                  "  Hi  There  ")
    print("reduce 等价实现:", via_reduce)
```

**追问**:1) 哪个更常用?——数据管道按书写顺序执行,pipeline 贴阅读习惯,是默认选择;组合链怎么调试?——插入带日志的 tap 函数观测中间值,而不是拆散组合。2) compose 与 pipeline 的方向差?——compose(f, g)(x) = f(g(x)) 数学序右到左;pipeline(f, g)(x) = g(f(x)) 书写序左到右;实现都是 functools.reduce 包函数。3) 与生成器管道的关系?——函数组合是「变换链」(每步全量);生成器管道是「流式链」(逐条穿全链,Q435);大数据场景后者内存 O(1)。4) 生产陷阱?——方向搞反(compose 顺序写反);组合链异常定位难(堆栈一层层剥);过度抽象把三行代码写成框架。
