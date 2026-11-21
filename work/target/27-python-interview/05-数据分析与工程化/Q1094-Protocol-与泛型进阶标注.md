---
title: [Q1094] Protocol 与泛型进阶标注
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1094 · Protocol 与泛型进阶标注

> 难度:★★★★ | 标签:typing, Protocol

**问**:函数参数想要"任何有 close 方法的对象",用基类太重,typing 怎么解?

**答**:用 `Protocol`(结构化子类型,静态 duck typing):定义 `class Closer(Protocol): def close(self) -> None`,任何长出 close 方法的类都天然满足,无需继承;`@runtime_checkable` 还能配合 isinstance 做运行时检查。泛型用 `Generic[T]`/PEP 695 的 `class Box[T]` 让容器保住元素类型。组合价值:库代码面向 Protocol 编程,调用方零耦合;资源管理函数参数标注为 Protocol,测试里随手写的 fake 也能通过类型检查。

```python
# file: code/05_数据分析与工程化/q1094_protocol_generic.py
from typing import Generic, Protocol, TypeVar, runtime_checkable

@runtime_checkable
class Closer(Protocol):
    def close(self) -> None:
        pass

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def get(self) -> T:
        return self.item

class Conn:
    def close(self) -> None:
        print("conn closed")

def shutdown(resource: Closer) -> None:
    resource.close()

if __name__ == "__main__":
    shutdown(Conn())               # 结构满足协议,无需继承
    b: Box[int] = Box(3)
    print(b.get() + 1)
    print("isinstance 运行时检查:", isinstance(Conn(), Closer))
```

**追问**:
- 追问 1:Protocol 和 ABC 怎么选?—— ABC 表达"显式契约 + 共享实现",Protocol 表达"结构匹配",跨层级解耦场景 Protocol 更轻。
- 追问 2:runtime_checkable 检查什么?—— 只检查方法名存在,不检查签名,签名正确性仍靠 mypy 静态保证。
