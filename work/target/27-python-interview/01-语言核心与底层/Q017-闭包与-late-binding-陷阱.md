---
title: [Q017] 闭包与 late binding 陷阱
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q017 · 闭包与 late binding 陷阱

> 难度:★★★ | 标签:闭包, 函数

**问**:循环里用 lambda 生成一批函数,为什么它们返回的都是最后一个值?

**答**:闭包捕获的是自由变量的引用(通过 cell 对象),不是创建时的值。循环变量只有一个,循环结束后所有闭包共享它,调用时才解引用,于是全是末值,这就是 late binding。解法有二:用默认参数在定义时固化值 `lambda i=i: ...`,或用 `functools.partial`。

```python
# file: code/01_语言核心与底层/q017_late_binding.py
import functools

funcs_bad = [lambda: i for i in range(3)]
funcs_ok  = [lambda i=i: i for i in range(3)]
funcs_par = [functools.partial(lambda k: k, i) for i in range(3)]

if __name__ == "__main__":
    print([f() for f in funcs_bad])  # [2, 2, 2]  late binding
    print([f() for f in funcs_ok])   # [0, 1, 2]  默认参数固化
    print([f() for f in funcs_par])  # [0, 1, 2]

    def outer():
        x = 1
        def inner():
            return x
        x = 2           # inner 读到的是最终值
        return inner()
    print(outer())      # 2
```

**追问**:1) 如何查看闭包捕获了什么?——`func.__closure__` 是 cell 元组,`cell.cell_contents` 可读取当前值,只读不可写。2) 为什么默认参数 `lambda i=i:` 能修复 late binding?——默认值在 def 语句执行时求值一次,每个闭包的 `__defaults__` 各自持有当轮迭代的 i,等于定义时快照。3) 闭包捕获的是值还是变量?——通过 cell 对象捕获变量本身(引用),外层函数返回后变量存活在 cell 里;这也是闭包延长对象生命周期、排查内存滞留时要看的点(`func.__closure__`)。
