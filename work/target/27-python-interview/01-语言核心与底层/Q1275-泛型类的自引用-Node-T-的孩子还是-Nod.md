---
title: [Q1275] 泛型类的自引用:Node[T] 的孩子还是 Node[T]
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1275 · 泛型类的自引用:Node[T] 的孩子还是 Node[T]

> 难度:★★★☆☆ | 标签:typing, 泛型, 数据结构

**问**:泛型树的节点类怎么写,才能让 `Node[int]` 的 children 静态上就是 `list[Node[int]]`?自引用注解为什么会 ForwardRef?

**答**:标准写法是 `class Node(Generic[T])`,字段注解 `children: list[Node[T]] = field(default_factory=list)`——T 在类作用域内自引用,定义时被当字符串前向引用处理(或直接写字符串),`from __future__ import annotations` 可以让所有注解延迟求值,自引用不再需要引号。运行时 `Node(1)` 与 `Node("a")` 是同一个类、不同参数化,类型参数纯静态存在,不产生任何运行时开销——这是「泛型是文档,不是运行时机制」的最好例证。坑在于 isinstance:`isinstance(node, Node[int])` 不合法(除非用 3.9+ 的参数化类但也被禁止用于 isinstance),运行时判断永远只到 `Node`。方法内部引用 T 需要方法签名也参数化,或直接用 Self(Q1269)表达返回同类。

```python
# file: code/01_语言核心与底层/q1275_generic_tree.py
from __future__ import annotations

from typing import Generic, List, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.children: List[Node[T]] = []   # 自引用:延迟求值

    def add(self, child: Node[T]) -> Node[T]:
        self.children.append(child)
        return child


def total(node: Node[int]) -> int:
    return node.value + sum(total(c) for c in node.children)


if __name__ == "__main__":
    root = Node(1)
    a = root.add(Node(2))
    root.add(Node(3))
    a.add(Node(4))
    print("sum:", total(root))
    print("isinstance 到参数化类是不允许的:", isinstance(root, Node))
```

**追问**:1) 3.12 的 PEP 695 有什么改善?——`class Node[T]: ...` 语法直接声明类型参数,作用域与惰性求值内建,不再需要 Generic 基类与模块级 TypeVar。2) 自引用泛型的成立条件?——类体注解里引用自身要么用字符串前向引用、要么加 from __future__ import annotations、要么 3.12 语法;运行时注解不解析就互不干扰。3) 惰性机制?——3.12 类型参数作用域内建、按需求值;3.10- 的 Generic[T] + 字符串引用靠 get_type_hints 递归解析,要有终止条件。4) 生产陷阱?——3.10- 直接 `child: Node[T]` 在类体报 NameError,要 future import;协变 TypeVar 用于参数位置被检查器拒绝(Q460);运行时解析递归注解性能差。
