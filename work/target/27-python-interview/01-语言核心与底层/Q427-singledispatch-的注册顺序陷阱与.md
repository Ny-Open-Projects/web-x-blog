---
title: [Q427] singledispatch 的注册顺序陷阱与 MRO
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q427 · singledispatch 的注册顺序陷阱与 MRO

> 难度:★★★☆☆ | 标签:functools, singledispatch, 陷阱

**问**:`functools.singledispatch` 注册 `list` 之后又注册 `object` 会覆盖吗?为什么给 `Sequence` 注册后传 `list` 能命中?运行期修改注册表(条件注册)有什么坑?

**答**:`singledispatch` 不是简单 dict 覆盖,而是按参数类型的 **MRO 距离**选最具体匹配:每次 `register` 把实现登记进 dispatch 表,派发时沿 `type(arg).__mro__` 找最近注册;后注册更泛的类型不会遮蔽已注册的更具体类型,给抽象基类(`Sequence`)注册也能命中 `list`(经 `__subclasshook__` 虚拟子类判定)。陷阱在:(1) 注册发生在**模块导入时**,若注册代码在 `if` 里且依赖 import 顺序,不同入口导入结果不同;(2) 对同一类型重复注册,后者**静默覆盖**前者(mro 表里同键覆盖),没有警告;(3) `register` 装饰的函数签名检查只在调用时做,类型注解写错要到运行期才炸;(4) 派发只看**第一个位置参数**——把派发参数用关键字传入不参与派发(直接 TypeError),任何版本都不支持 keyword-only 派发(3.12 只是把这个口径写进了文档,提案 bpo-36744 已被拒绝)。生产建议:集中注册、模块级一次性完成,避免运行期条件分支里 register。

```python
# file: code/01_语言核心与底层/q427_singledispatch_order.py
from collections.abc import Sequence
from functools import singledispatch

@singledispatch
def render(arg):
    return f"fallback: {arg!r}"

@render.register
def _(arg: list):                 # 具体类型
    return f"list of {len(arg)}"

@render.register
def _(arg: Sequence):             # 更泛的 ABC,list 是其虚拟子类
    return "sequence-like"

print(render([1, 2]))             # list of 2 —— 最具体的赢,顺序无关
print(render((1, 2)))             # sequence-like
print(render("abc"))              # fallback? str 也是 Sequence!注意 str 命中 ABC 分支

# 同类型重复注册:后者静默覆盖
@render.register
def _(arg: list):
    return "second list impl"
print(render([1]))                # second list impl,无任何警告

print("registry keys:", sorted(k.__name__ for k in render.registry))
```

**追问**:1) `render("abc")` 为什么命中 Sequence 而不是 object?——`str.__mro__` 距离上 Sequence 注册被虚拟子类判定命中,str 没有更具体注册;这正是"注册 ABC 影响面比想象大"的例子。2) 怎么调试派发到哪个实现?——`render.dispatch(type(arg))` 直接查表,`render.registry` 看全部注册。
