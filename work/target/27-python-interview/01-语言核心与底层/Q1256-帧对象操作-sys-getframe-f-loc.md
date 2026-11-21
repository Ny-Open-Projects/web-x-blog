---
title: [Q1256] 帧对象操作:sys._getframe、f_locals 与 frame.clear
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1256 · 帧对象操作:sys._getframe、f_locals 与 frame.clear

> 难度:★★★★☆ | 标签:帧对象, 内省, CPython

**问**:如何在运行时拿到调用者的帧?帧对象上有哪些可用信息?frame.clear() 是干什么的?

**答**:`sys._getframe(depth)` 直接取当前调用栈上的帧对象:depth 0 是自己,1 是调用者,沿 `f_back` 可以一路走到栈底。帧上最有用的属性:`f_code`(代码对象)、`f_lineno`(当前执行行号,只读)、`f_locals`(局部变量字典)与 `f_globals`。注意 `f_locals` 是「按需物化」的快照——CPython 的局部变量存在连续槽位数组里,访问 f_locals 才把它们拷成字典,所以函数内修改 `locals()` 是未定义行为。`frame.clear()` 用于强制释放一个被 traceback 之类引用挂住的帧的局部变量,防止异常对象长期滞留把整条调用链钉在内存里(Q424 的对症手术);正在执行的帧不能 clear,会抛 RuntimeError。

```python
# file: code/01_语言核心与底层/q1256_frame_introspect.py
import sys


def inner():
    return sys._getframe(1)          # 拿到调用者的帧


def outer():
    caller = inner()
    n, f = 0, sys._getframe()
    while f is not None:             # 沿 f_back 数这条 Python 栈
        n += 1
        f = f.f_back
    return caller.f_code.co_name, caller.f_lineno, sorted(caller.f_locals), n


def raise_deep():
    raise ValueError("boom")


def catch_and_clear():
    try:
        raise_deep()
    except ValueError:
        tb = sys.exc_info()[2]
        current = sys._getframe()
        cleared = 0
        while tb is not None:
            if tb.tb_frame is not current:   # 正在执行的帧不能 clear
                tb.tb_frame.clear()          # 释放 traceback 钉住的局部变量
                cleared += 1
            tb = tb.tb_next
        return cleared


if __name__ == "__main__":
    name, line, locals_, depth = outer()
    print("caller:", name, "at line", line)
    print("caller locals:", locals_)
    print("python stack depth:", depth)
    print("cleared non-current frames:", catch_and_clear())
```

**追问**:1) 为什么 profiler 和调试器都靠帧而不是靠 print?——帧是解释器的一等观测点:f_lineno、f_trace、f_locals 让工具能按行插桩,这也是 sys.settrace(Q552)的物料基础。2) f_locals 的真相是什么?——3.13 前它是「每次访问把 fast locals 拷出的快照字典」,写它不回写帧;PEP 667(3.13)改成读写代理——所以「修改 locals()」在旧版本是未定义行为,不要依赖。3) frame.clear 释放什么?——把帧对局部变量的引用清空,被 traceback 挂住的帧因此不再把整条调用链钉在内存;正在执行的帧不能 clear(RuntimeError)。4) 生产陷阱?——长期持有异常对象/traceback 让整段调用链存活(内存上涨),捕获后处理完要丢弃引用;调试工具生产禁用;依赖「写 f_locals 生效」的代码在 3.13 前是错的。
