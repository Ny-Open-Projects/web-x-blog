---
title: [Q461] Protocol 的 runtime_checkable 边界
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q461 · Protocol 的 runtime_checkable 边界

> 难度:★★★☆ | 标签:typing, Protocol

**问**:@runtime_checkable 的 isinstance 检查了什么?为什么它不能验证方法签名?

**答**:runtime_checkable 让 Protocol 可以做运行时 isinstance/issubclass,检查方式是「结构匹配」:只要对象(或其类)拥有协议声明的成员名即通过,不继承、不校验签名、不校验属性类型。签名正确性只能由静态检查器在调用点保证。运行时协议的正当用途是「特性探测」(有没有 close/has this capability)和优雅降级;把它当接口契约做深度校验是误用——那是 ABC + 抽象方法或 pydantic 的职责。

```python
# file: code/01_语言核心与底层/q461_runtime_checkable.py
from typing import Protocol, runtime_checkable

@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None:
        """协议方法:只关心名字存在"""

class DBConn:
    def close(self) -> None:
        print("db closed")

class FileHandle:
    def close(self) -> None:
        print("file closed")

def close_all(resources):
    for r in resources:
        if isinstance(r, Closeable):      # 运行时结构检查:只看成员名
            r.close()

if __name__ == "__main__":
    close_all([DBConn(), FileHandle(), object()])
    print(isinstance(DBConn(), Closeable))
    print(issubclass(DBConn, Closeable))

    class Fake:
        close = 42                        # 签名完全不对也能通过
    print(isinstance(Fake(), Closeable))  # True:证明它不检查签名
```

**追问**:1) Protocol 与 ABC 的本质区别?——ABC 是名义子类型(显式继承才算),Protocol 是结构子类型(长得像就算),后者能接纳无法修改的第三方类型。2) isinstance(x, Protocol) 检查了什么、漏了什么?——逐成员验证名字存在,不验签名、类型与属性种类;3.12 起对含非方法成员的 protocol 做 issubclass 直接 TypeError;开销随成员数线性。3) 结构检查的底层实现?——Protocol 把成员名集合登记在注册表,runtime_checkable 后由 __instancecheck__/__subclasshook__ 做名字比对;与 ABCMeta 的名义注册表互不相干。4) 生产陷阱?——把 runtime_checkable 协议当完整契约校验入参,Fake 的 close=42 也能通过;能力探测可以,深度校验要交给 ABC 或 pydantic。
