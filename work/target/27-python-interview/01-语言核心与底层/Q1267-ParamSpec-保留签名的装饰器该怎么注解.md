---
title: [Q1267] ParamSpec:保留签名的装饰器该怎么注解
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1267 · ParamSpec:保留签名的装饰器该怎么注解

> 难度:★★★★☆ | 标签:typing, ParamSpec, 装饰器

**问**:写一个透传所有参数的装饰器,类型注解怎么写才能让 mypy 知道 `add(1, 2)` 依然合法?`Callable[..., R]` 差在哪?

**答**:`Callable[..., R]` 的 `...` 把参数类型「蒸发」了——被装饰后调用 `add(1, "x")` 静态检查器不再报错。3.10 的 `ParamSpec`(PEP 612)解决这件事:`P = ParamSpec("P")`,装饰器签名写作 `(func: Callable[P, R]) -> Callable[P, R]`,P 是「参数列表本身」的类型变量,把被装饰函数的参数形状原样搬到返回的 Callable 上;配合 `Concatenate[P, X]` 还能表达「装饰器注入了首个参数」的变换(如给 handler 前面塞一个 logger)。运行时配 `functools.wraps`(Q013)保住 `__name__`/`__doc__`/`__wrapped__`,静态配 ParamSpec 保住签名——两件事是互补的,面试里要能分开说。3.9 及以前只能用 `TypeVar("F", bound=Callable)` 做恒等透传,见 Q1270 的对比。

```python
# file: code/01_语言核心与底层/q1267_paramspec.py
from __future__ import annotations

import functools
import inspect

try:
    from typing import Callable, ParamSpec, TypeVar
    P = ParamSpec("P")
    R = TypeVar("R")
    HAS_PARAMSPEC = True
except ImportError:                      # 3.9:typing.ParamSpec 尚不存在
    from typing import Callable, TypeVar
    P = None
    R = TypeVar("R")
    HAS_PARAMSPEC = False


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("call", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@logged
def add(a: int, b: int = 0) -> int:
    return a + b


if __name__ == "__main__":
    print("HAS_PARAMSPEC:", HAS_PARAMSPEC)
    print("runtime signature preserved:", inspect.signature(add))
    print("name preserved:", add.__name__, "| call:", add(2, b=3))
    if HAS_PARAMSPEC:
        print("静态层: func: Callable[P, R] -> Callable[P, R]")
    else:
        print("3.9 请用 TypeVar bound=Callable 的恒等式写法, 见 q1270")
```

**追问**:1) ParamSpec 能表达「包装器少一个参数」吗?——能,`Callable[Concatenate[str, P], R]` 表示包装后首位固定为 str,其余参数跟随 P,3.10 起可用。2) ParamSpec 与 TypeVar 的分工?——TypeVar 保持「类型不丢」(T 进 T 出),ParamSpec 捕获「整个参数表」;包装体内用 P.args/P.kwargs 转发,调用方签名与返回类型都保留。3) 运行时形态?——ParamSpec/Concatenate 是纯静态元数据,解释器不校验;检查器需要新版 mypy/pyright 才完整支持。4) 生产陷阱?——装饰器注解成 **kwargs: Any,调用方全部丢类型;3.10- 退化成 Callable[..., R];Concatenate 只能固定头部参数,尾部固定表达不了。
