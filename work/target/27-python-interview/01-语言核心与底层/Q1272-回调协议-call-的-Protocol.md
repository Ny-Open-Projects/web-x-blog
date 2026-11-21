---
title: [Q1272] 回调协议:__call__ 的 Protocol
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1272 · 回调协议:__call__ 的 Protocol

> 难度:★★★☆☆ | 标签:typing, Protocol, 回调

**问**:接口要求「一个可调用对象,签名是 (event, payload)」,用 ABC 还是 Protocol?runtime_checkable 能查出签名不匹配吗?

**答**:回调天然属于结构化类型——第三方传来的可能是一个函数、functools.partial、实现了 __call__ 的类实例,强行继承 ABC 不现实。正解是 Protocol 定义 `__call__(self, event: str, payload: int) -> None`,任何结构匹配的对象都满足,无需注册。注意 runtime_checkable 的 isinstance 只检查「方法/属性存在」,不检查签名:`isinstance(print, Handler)` 为 True,因为 print 有 __call__;签名是否真的兼容只有静态检查器知道。所以运行时守门用 `callable(fn)` 就够,签名契约交给 mypy;把两者混为一谈是本题最常见的错误答案。

```python
# file: code/01_语言核心与底层/q1272_callback_protocol.py
from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Handler(Protocol):
    def __call__(self, event: str, payload: int) -> None: ...


def register(fn: Handler) -> None:
    if not callable(fn):                 # 运行时只做这个守门
        raise TypeError("need a callable")
    fn("start", 1)


if __name__ == "__main__":
    def my_handler(event, payload):
        print("got", event, payload)

    register(my_handler)
    print("isinstance my_handler:", isinstance(my_handler, Handler))
    print("isinstance 'text'    :", isinstance("text", Handler))
    print("isinstance print     :", isinstance(print, Handler),
          "<- 只查 __call__ 存在,不查签名")
```

**追问**:1) Protocol 能约束属性吗?——能,类体里写 `conn: Connection` 即属性协议,结构与回调协议混用即可描述「带配置的可调用对象」。2) 回调 Protocol 比 Callable 强在哪?——Callable 只描述签名;带 __call__ 的 Protocol 还能要求实例属性(如 client、retry),静态层一起校验,runtime_checkable 还能做能力探测。3) 结构匹配机制?——检查器按成员名+签名比对;lambda/函数对象没有附加属性,只满足「纯签名」的协议——要带属性的回调必须是有状态的类。4) 生产陷阱?——把带属性约束的协议当 Callable 用,装饰过的函数过不了检查;runtime_checkable 对非方法成员的 issubclass 在 3.12 报 TypeError(Q461);协议里写方法体误导读者(协议方法是签名声明)。
