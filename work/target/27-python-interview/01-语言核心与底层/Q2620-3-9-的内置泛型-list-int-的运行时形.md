---
title: [Q2620] 3.9 的内置泛型:list[int] 的运行时形态与陷阱
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2620 · 3.9 的内置泛型:list[int] 的运行时形态与陷阱

> 难度:★★★☆☆ | 标签:PEP 585, 泛型, 3.9 新特性

**问**:3.9 里 `list[int]` 能直接写了吗?和 `typing.List[int]` 有什么区别,有什么坑?

**答**:能——PEP 585 让内置容器类型直接支持下标,`list[int]`、`dict[str, int]`、`tuple[int, ...]` 在 3.9 运行时都是合法表达式,产物是 `types.GenericAlias`,同样可以用 `get_origin`/`get_args` 拆解,与 `typing.List[int]` 在注解层面等价。三个坑要记住:第一,它仍然不能用于 `isinstance`;第二,不是所有内置类型都可参数化,`str[int]` 会直接 TypeError,因为 str 没有提供 `__class_getitem__` 的参数化支持;第三,老版本兼容代码或需要 `typing` 专属能力(如 `List` 在旧 3.7/3.8 里)时仍要回到 typing 双轨写法。工程建议:3.9 起新代码统一用内置泛型,少一层 import、序列化更直观。

```python
# file: code/01_语言核心与底层/q2620_builtin_generics.py
"""3.9 的内置泛型:PEP 585 的运行时形态、拆解与边界。"""
import types
import typing


def mean(values: list[float]) -> float:      # 3.9 合法注解
    return sum(values) / len(values)


if __name__ == "__main__":
    alias = list[int]
    print("list[int] 类型:", type(alias), isinstance(alias, types.GenericAlias))
    print("拆解:", typing.get_origin(alias), typing.get_args(alias))
    print("dict[str, int]:", dict[str, int])
    print("tuple[int, ...]:", tuple[int, ...])

    print("mean([1, 2, 3]):", mean([1.0, 2.0, 3.0]))

    try:
        str[int]
    except TypeError as exc:
        print("str 不可参数化:", exc)

    try:
        isinstance([], list[int])
    except TypeError as exc:
        print("isinstance 拒绝参数化泛型:", exc)
```

**追问**:1) 3.9 之前怎么做到「内置泛型」的效果?——只能 `typing.List[int]`,PEP 585 把参数化能力直接挂到了内置类型上,运行时不再依赖 typing 的别名体系。2) PEP 585 的收益面?——list[int]/dict[str, int] 直写;typing.List 等别名自 3.9 标记弃用(3.12+ 逐步移除路径);get_origin/get_args 对两类对象统一拆解(Q2616)。3) 与 PEP 604 的组合?——3.10 起 X | Y 替代 Union;`list[int | None]` 全新语法链;旧版本兼容用 from __future__ import annotations(Q2104)。4) 生产陷阱?——3.8 直接写 list[int] 语法错误(运行时注解求值);typing.List 与 list[int] 混用;isinstance 误用参数化泛型(Q2616)。
