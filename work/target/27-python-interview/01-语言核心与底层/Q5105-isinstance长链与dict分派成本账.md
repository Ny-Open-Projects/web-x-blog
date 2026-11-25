---
title: [Q5105] isinstance 长链与 dict 分派成本账
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5105 · isinstance 长链与 dict 分派成本账

> 难度:★★★☆☆ | 标签:成本工程, 分派, 热路径

**问**:热路径上一段 10 分支的 `isinstance` 类型判断链，怎么优化？收益量级多少？

**答**:结论：isinstance 是 C 级调用，单次本身不贵（几十 ns），但长链逐个短路求值，最坏要 N 次；命中靠后的类型每次都付全链成本。可量化的替代：① dict 分派——以类型对象为 key，`O(1)` 哈希查找；② 注册表 + `type(obj)` 精确匹配；③ 需要继承语义时用 `functools.singledispatch`（按 MRO 注册，语义与 isinstance 链等价且维护性更好）。取舍：dict 分派要求"精确类型"语义，子类会 miss；singledispatch 有首次注册与 MRO 解析开销但摊销后稳定。实测收益通常 2~5 倍（取决于链长与命中位置），更重要的是把"加一个类型要改 if 链"的开敞成本关掉。注意 open/closed 原则的收益往往大于那点纳秒。

```python
import timeit

class A: pass
class B: pass
class C: pass

def chain(o):                       # 10 分支链的模拟：命中在末尾
    for cls in (A,) * 8 + (B, C):
        if isinstance(o, cls):
            return cls.__name__
    return "?"

DISPATCH = {B: "B", C: "C"}

def dispatch(o):
    return DISPATCH.get(type(o), "?")

o = C()
assert chain(o) == dispatch(o) == "C"

t_chain = timeit.timeit(lambda: chain(o), number=200_000)
t_disp = timeit.timeit(lambda: dispatch(o), number=200_000)
print(f"isinstance 链 {t_chain:.3f}s | dict 分派 {t_disp:.3f}s | {t_chain/t_disp:.1f}x")

# 继承语义等价的正解：singledispatch（按 MRO 分派）
from functools import singledispatch

@singledispatch
def name(o): return "?"

@name.register
def _(o: B): return "B"

@name.register
def _(o: C): return "C"

class Sub(C): pass
print(name(Sub()))                  # 'C' —— 子类命中父类注册，isinstance 语义
```

**追问一层**:`type(o)` 作 dict key 为什么可行且无坑（hash 稳定性、PYTHONHASHSEED 影响）？
**追二层**:`functools.singledispatch` 对抽象基类（如 `collections.abc.Sequence`）的注册如何解析？有什么坑？

**背诵要点**
- isinstance 链最坏 O(N)，命尾部类型反复付全链成本。
- 精确类型用 dict 分派，继承语义用 singledispatch。
- 优化前先量：链长与命中位置决定收益（典型 2~5x）。

**复盘追问**
- 热路径里高频出现的是"类型未知的外部输入"时，分派表的 key 怎么兜底？提示：default 分支 + 观测日志。
- singledispatch 在多进程 spawn 下注册是否会丢失？提示：模块导入时机。
