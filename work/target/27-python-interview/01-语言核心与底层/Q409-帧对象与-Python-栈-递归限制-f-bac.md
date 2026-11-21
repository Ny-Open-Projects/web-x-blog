---
title: [Q409] 帧对象与 Python 栈:递归限制、f_back 与回溯
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q409 · 帧对象与 Python 栈:递归限制、f_back 与回溯

> 难度:★★★★☆ | 标签:帧对象, 调用栈, inspect

**问**:Python 的调用栈和 C 栈是什么关系?`sys.setrecursionlimit` 调大为什么可能直接段错误?`RecursionError` 的默认 1000 是怎么来的,3.12 有什么变化?

**答**:每层 Python 调用创建一个 `PyFrameObject`(3.11 后拆成惰性分配的 `_PyInterpreterFrame`,开销大减),串成 `f_back` 链,这是 Python 层看到的栈;同时解释器自身跑在 C 栈上,`Py_EnterRecursiveCall` 在每次调用时同时检查两层。`sys.setrecursionlimit` 只调 Python 层的计数,而 C 栈大小固定(通常 8MB),纯 Python 调用在 3.11 后几乎不消耗 C 栈,但对象析构、`__eq__` 嵌套等仍会回退到 C 递归——把 limit 调到百万级可能在真正耗尽 C 栈时直接崩溃而不是抛异常。3.12 起 CPython 引入"接近 C 栈上限时强制抛 RecursionError"的软保护(`Py_C_RECURSION_LIMIT`),默认 Python 限 1000 只是防失控的策略值,不是硬资源边界。

```python
# file: code/01_语言核心与底层/q409_frames_stack.py
import inspect
import sys

def depth():
    f = sys._getframe()
    n = 0
    while f:
        n += 1
        f = f.f_back          # 沿 f_back 链上溯,这就是 Python 栈
    return n

def recurse(n):
    return recurse(n + 1)     # 无限递归,直到撞上递归限制

def traceback_format(e):
    import traceback
    return traceback.format_exception(type(e), e, e.__traceback__)

print("current python stack depth:", depth())
print("recursionlimit:", sys.getrecursionlimit())

try:
    recurse(0)
except RecursionError as e:
    print("RecursionError:", e)

# 回溯本身就是帧链的可读投影
tb_lines = []
try:
    1 / 0
except ZeroDivisionError as e:
    tb_lines = traceback_format(e)

print("".join(tb_lines).splitlines()[-1])

# inspect 能拿到运行期帧
print("callers:", [s.function for s in inspect.stack()][:4])
```

**追问**:1) 生成器/协程的帧和普通帧有什么不同?——yield 时帧对象从解释器运行栈摘下但保留在堆上,状态全存帧里,`gen.gi_frame` 可观察,这是协程能"暂停"的物理基础。2) 为什么 3.11 版本 Python 函数调用快了很多?——帧改为栈上分配、惰性物化,且不再为每个调用无条件创建 `PyFrameObject` 堆对象。
