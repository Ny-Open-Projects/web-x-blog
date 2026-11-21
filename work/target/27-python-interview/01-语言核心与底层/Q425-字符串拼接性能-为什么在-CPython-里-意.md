---
title: [Q425] 字符串拼接性能:+= 为什么在 CPython 里"意外地快"?
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q425 · 字符串拼接性能:+= 为什么在 CPython 里"意外地快"?

> 难度:★★★★☆ | 标签:str, 性能, CPython

**问**:教材说字符串不可变要避免 `+=` 循环拼接,为什么 CPython 实测有时 `+=` 比 `''.join` 还快?这个优化依赖什么条件?跨实现还成立吗?

**答**:CPython 对 `s += t` 有一个针对性优化(`unicode_concatenate`/CEval 里的特殊路径):当 `+=` 的左值是唯一持有该字符串的局部变量(引用计数为 1)时,原地扩容重用底层缓冲,均摊近似 O(n) 而不是朴素 O(n²)。条件苛刻:有其他引用(哪怕 `sys.getrefcount` 场景、别名、异常帧里挂着)就不触发;3.x 的 `-OO`、free-threading 构建、PyPy/Jython 行为完全不同——PyPy 上 join 快、CPython 上可能反转。因此工程结论:**依赖这一优化是错误的可移植性假设**,跨实现/跨版本稳定的选择是 `''.join(parts)` 或 `io.StringIO`;热路径先用 `timeit` 在目标版本实测(见 Q430),再把"路径选择"写死在代码注释里注明测过的 Python 版本。

```python
# file: code/01_语言核心与底层/q425_str_concat.py
import timeit

setup = "parts = ['chunk-%d' % i for i in range(2000)]"

plus = timeit.timeit(
    "s = ''\nfor p in parts:\n    s += p", setup, number=100)
join = timeit.timeit(
    "s = ''.join(parts)", setup, number=100)
print(f"+= loop : {plus*10:.1f} ms per 1000 iters")
print(f"join    : {join*10:.1f} ms per 1000 iters")

# 破坏唯一引用条件,+= 优化失效:先留一个别名
bad = timeit.timeit(
    "s = ''\nalias = s\nfor p in parts:\n    s += p", setup, number=100)
print(f"+= with alias: {bad*10:.1f} ms per 1000 iters  <- 优化失效,退化为 O(n^2)")
```

**追问**:1) 怎么从字节码确认优化生效?——优化在 eval loop 的 `BINARY_OP`/`INPLACE_ADD` 分支做运行期判断,字节码本身相同,差异在运行时引用计数,可用 `sys.getrefcount` 演示条件破坏。2) f-string 为什么快?——3.12 前 f-string 编译成 BUILD_STRING/BUILD_LIST 拼段,3.12+ 的 PEP 701 让 f-string 成为正式语法树可嵌套任意表达式,常用路径仍比 `%`/format 快,因为免去了运行时格式解析。
