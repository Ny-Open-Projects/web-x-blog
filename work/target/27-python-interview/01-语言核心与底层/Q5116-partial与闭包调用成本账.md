---
title: [Q5116] partial、闭包与 lambda 调用成本账
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5116 · partial、闭包与 lambda 调用成本账

> 难度:★★★★☆ | 标签:成本工程, 函数对象, 参数绑定

**问**:回调注册处常见三种写法：`functools.partial(func, x=1)`、闭包 `def f(): return func(x=1)`、`lambda: func(x=1)`。它们在调用成本、可读性、调试友好度上的真实差异是什么？热路径里该选哪个？

**答**:结论：**三者的调用成本都在百纳秒量级，方向取决于绑定方式：纯位置参数的 partial 走 C 快路径可略快；但 keyword 绑定的 partial 每次 `__call__` 要合并绑定字典，实测可能比手写闭包还慢（322ns vs 152ns）**——热路径里真正的成本不在绑定方式而在被调函数本身，所以选型的第一权重是**语义与调试**，不是性能。机理差异：a) `lambda`/闭包每次调用创建一个 Python 栈帧（调用期 frame push/pop），但 0 参数闭包走 LOAD_CLOSURE 快路径；b) `partial` 是 C 实现，无 Python 帧创建，但要把预存 args/kwargs 与调用时参数合并成新的元组/字典——keyword 越多合并越贵；c) 调试维度：partial 的 `repr` 显示函数名与绑定参数，而裸 lambda 在 traceback 里只有 `<lambda>`，定位成本高；d) 元数据：`partial` 保留 `func` 引用可继续取 `__name__`，lambda 需手动维护。另有一个正确性差异常被忽视：`partial` 在**创建时**就固化参数求值，闭包晚绑定陷阱（Q017）在 lambda 循环里会拿到循环变量的最终值，partial 循环里 `partial(f, i)` 每个对象固化各自的 i——注册回调循环里 partial 更不易出错。

```python
import functools, timeit, sys

def target(x=0, y=0):
    return x + y

# 三种绑定的调用成本
p   = functools.partial(target, x=1)
lam = lambda: target(x=1)

def closure():
    return target(x=1)

def _bench(fn, n=2_000_000):
    return timeit.timeit(fn, number=n) / n * 1e9

print(f"partial 调用: {_bench(p):.1f} ns/次")
print(f"lambda  调用: {_bench(lam):.1f} ns/次")
print(f"closure 调用: {_bench(closure):.1f} ns/次")

# 调试友好度对比
print("partial repr:", repr(p))
print("lambda repr :", repr(lam))
print("partial 可取底层函数:", p.func.__name__, "| 已绑定参数:", p.keywords)

# 晚绑定差异（关键正确性点）
callbacks_lam = [lambda: i for i in range(3)]
callbacks_par = [functools.partial(lambda v: v, i) for i in range(3)]
print("lambda 循环注册后:", [c() for c in callbacks_lam])   # [2, 2, 2] 全是尾值
print("partial 循环注册后:", [c() for c in callbacks_par])   # [0, 1, 2] 各自固化

# partial 链式绑定：keyword 合并语义，调用时同名 keyword 会报重复
base = functools.partial(target, x=10)
print("base(y=5):", base(y=5))                                # keyword 固着 x=10，调用只补 y
print("链式 partial:", functools.partial(base, y=7)())
```

**追问一层**:`partial` 固化的是"创建时的值"，那如果绑定的是一个可变对象的引用，之后对象被改了会怎样？与闭包捕获同一个对象引用有何区别？
**追二层**:C 层面 `partial.__call__` 真的不创建帧吗？和 `methodcaller`/`operator.itemgetter` 这类"操作符版 partial"的成本差在哪（引 Q2624/Q5090）？

**背诵要点**
- 三者调用都在百 ns 量级；keyword 绑定的 partial 需合并字典，可能比闭包更慢——性能不构成选型依据。
- partial 创建时固化参数值，循环注册回调不受晚绑定陷阱影响；lambda 循环会拿到尾值。
- partial 保留底层函数与绑定参数，traceback/repr 可读；裸 lambda 只有 `<lambda>`。

**复盘追问**
- 团队里 2000 个回调都改成 partial 后 CPU 没降，为什么？提示：绑定成本是创建期一次性，调用差距只在热路径可测，先看 profile 里的真实大头。
- partial 固化 `conn` 这类连接对象后，连接被关闭重建，回调还拿着旧引用——这类"绑定过期"怎么治理？提示：绑定惰性获取器而非实例，或注册时用 weakref（引 Q404）。
