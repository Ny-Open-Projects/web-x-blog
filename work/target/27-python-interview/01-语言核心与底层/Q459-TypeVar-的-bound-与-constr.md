---
title: [Q459] TypeVar 的 bound 与 constrained
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q459 · TypeVar 的 bound 与 constrained

> 难度:★★★★ | 标签:typing, 泛型

**问**:TypeVar("T", str, bytes) 和 TypeVar("T", bound=str) 的求解规则有什么本质区别?

**答**:constrained 形式枚举有限取值,调用时所有出现位置必须「精确取同一个成员」:concat("a", "b") 解为 str,concat(b"x", b"y") 解为 bytes,混用直接报错;适合表达 AnyStr 这类「同类才兼容」的约束。bound 形式给上界,实参可以是任意子类型,整次调用统一解为最具体的公共类型:`scale_all` 传入 list[int] 时 T 解为 int,返回类型保持 int,信息不丢失。经验法则:约束「不能混用」用 constrained,约束「至少能做什么」用 bound。

```python
# file: code/01_语言核心与底层/q459_typevar_bound.py
from typing import TypeVar, List

AnyStr2 = TypeVar("AnyStr2", str, bytes)     # constrained:只能是这几个
NumberT = TypeVar("NumberT", bound=float)    # bound:上界,可为子类

def concat(a: AnyStr2, b: AnyStr2) -> AnyStr2:
    """constrained:同一次调用中两个参数必须同类型"""
    return a + b

def scale_all(items: List[NumberT], factor: float) -> List[NumberT]:
    """bound:输入是什么类型,返回就保持什么类型"""
    return [x * factor for x in items]

if __name__ == "__main__":
    print(concat("a", "b"), concat(b"x", b"y"))
    print(scale_all([1.5, 2.5], 2.0))
    print(scale_all.__annotations__)
    # concat("a", b"b") 在 mypy 下报错:同一个 TypeVar 求解出两个冲突类型
```

**追问**:1) TypeVar 名字里的 "T" 为什么要带引号且与变量名一致?——它是运行时对象的名字标识,静态检查器按字符串匹配同一 TypeVar 的多次出现,名字不一致会让约束对不上。2) constrained 混用报错的本质?——同一个 TypeVar 在一次调用内必须单值求解,concat("a", b"b") 解出 str 与 bytes 两个冲突解,检查器拒绝;这是解方程模型,不是运行时检查。3) 泛型求解发生在什么阶段?——静态检查器在调用点做 unification,运行时 GenericAlias 只是元数据、解释器完全不校验;类型安全只在 mypy/pyright + CI 里成立。4) 生产陷阱?——同一 TypeVar 标注两个语义无关的参数(如 def f(a: T, b: T)),调用方被迫传同型或 cast;语义独立就用不同 TypeVar。
