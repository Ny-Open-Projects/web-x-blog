---
title: [Q035] typing 与泛型
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q035 · typing 与泛型

> 难度:★★☆ | 标签:typing

**问**:类型注解在运行时生效吗?Generic、TypeVar 怎么用?

**答**:注解默认不参与运行时行为,价值在静态检查(mypy/pyright)、IDE 补全与文档。`TypeVar` 声明泛型变量让输入输出类型关联;Python 3.12 起可用 `def f[T](x: T) -> T` 语法;内置容器直接支持下标 `list[int]`、`dict[str, float]`(3.9+)。常见工具还有 `Optional[X]`(3.10+ 才可简写为 `X | None`,3.9 及以下注解若被运行时求值须写 Optional)、`Union`、`Callable`、`TypedDict`、`Literal`。

```python
# file: code/01_语言核心与底层/q035_typing.py
from __future__ import annotations   # 注解惰性求值,低版本也可安全书写新式注解

from typing import Optional, TypeVar, Generic, TypedDict

T = TypeVar("T")

def first(items: list[T]) -> Optional[T]:   # 3.10+ 可写 T | None
    return items[0] if items else None

class Config(TypedDict):
    host: str
    port: int

class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item
    def get(self) -> T:
        return self.item

if __name__ == "__main__":
    print(first([1, 2]), first([]))
    b: Box[str] = Box("hello")
    print(b.get().upper())
    cfg: Config = {"host": "localhost", "port": 8080}
    print(cfg)
    print(__import__("typing").get_type_hints(first))  # 运行时可读取注解
```

**追问**:1) 运行时如何强制类型?——注解本身不强制,可在 `__init_subclass__`、描述符或 pydantic 类库中读取 `__annotations__` 做校验。2) `X | None` 在什么版本能直接写在运行时注解里?——3.10+;3.9 会 TypeError,除非加 `from __future__ import annotations` 让注解延迟成字符串不求值。3) TypeVar 的 bound 与 constraints 有何区别?——`T bound=Animal` 表示任意子类都行(上界);`T = TypeVar('T', int, float)` 表示限定集合,值只能是列举类型之一,重载语义不同。
