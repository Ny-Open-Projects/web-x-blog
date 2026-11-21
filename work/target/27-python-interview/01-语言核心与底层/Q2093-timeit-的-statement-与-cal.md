---
title: [Q2093] timeit 的 statement 与 callable
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2093 · timeit 的 statement 与 callable

> 难度:★★☆☆☆ | 标签:timeit, 微基准, 实测

**问**:timeit.timeit 传字符串和传 callable 有什么区别?哪种测得更准?

**答**:两种喂法的语义差异:字符串语句被 timeit 编译一次后反复执行,循环体就是语句本身;callable 形式会被包进 lambda,每次循环多一层 Python 函数调用——本机实测差额稳定存在,测「目标函数本身」时这层包装是系统性偏差。所以精确基准用字符串形式配合 globals=globals() 把被测函数送进去;粗略相对比较用 callable 更顺手,偏差不影响排名。另外两条纪律:timeit 默认禁用 GC,测分配密集代码时结论会偏乐观,要对比就显式开启;单次 timeit 受环境抖动影响,用 timeit.repeat 取最小值——最小值最接近无干扰真值,平均值反而吸收了毛刺。还有个反例要认得:"1 + 2" 这类常量表达式会被编译期折叠,测出来快得没意义,变量化才是真实成本。

```python
# file: code/01_语言核心与底层/q2093_timeit_forms.py
"""timeit 的两种喂法:statement 字符串与 callable 的开销差异。"""
import timeit


def target(n=1000):
    return sum(range(n))


ENV = {"target": target}


if __name__ == "__main__":
    n = 2000
    t_stmt = timeit.timeit("target()", globals=ENV, number=n)
    t_call = timeit.timeit(lambda: target(), number=n)
    print("字符串语句形式:", round(t_stmt, 4), "秒")
    print("callable 形式(多一层 lambda):", round(t_call, 4), "秒")
    print("差额是系统性包装开销:", round(t_call - t_stmt, 4), "秒")

    t_const = timeit.timeit("1 + 2", number=500000)
    t_names = timeit.timeit("a + b", setup="a, b = 1, 2", number=500000)
    print("常量折叠的假快:", round(t_const, 5), "| 变量加法真实成本:", round(t_names, 5))

    best = min(timeit.repeat("target()", globals=ENV, number=500, repeat=5))
    print("repeat 取最小值更抗干扰:", round(best, 4), "秒")
```

**追问**:1) timeit 为什么默认关 GC?——避免回收抖动污染微基准,测分配密集代码要手动开启对比;repeat 取几次?——3 到 5 次取最小,最小值最接近无干扰真值,平均会吸收毛刺。2) statement 与 callable 两形态?——callable 形态避免「字符串拼接源码」的失真;字符串形态配 setup 参数;number 先粗测校准,保证单次计时 > 0.2s。3) 微基准的方法论?——timeit min(Q401 官方口径)、同一进程内对比、注意 3.11+ 特化对结论的扰动(Q1259);微基准只回答常数级问题。4) 生产陷阱?——跑一次就下结论;GC 干扰分配密集场景(手动 gc.enable 对比);基准代码与生产代码形态不一致(如混合类型输入触发 deopt)。
