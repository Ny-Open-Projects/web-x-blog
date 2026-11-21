---
title: [Q1270] 装饰器类型保持三式:TypeVar、ParamSpec 与 overload
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1270 · 装饰器类型保持三式:TypeVar、ParamSpec 与 overload

> 难度:★★★☆☆ | 标签:typing, 装饰器

**问**:不丢类型的装饰器注解,有哪几种流派?各适合什么场景?

**答**:三种主流写法。其一,恒等式 `F = TypeVar("F", bound=Callable[..., object])`,装饰器 `-> F`:最简单,表达「进什么出什么」,适合不改变签名、不改默认值的透明装饰器,3.9 也能用。其二,ParamSpec(PEP 612,见 Q1267):能表达签名变换,如注入参数、可选化参数,是 3.10+ 的首选。其三,`@overload`:装饰器行为因参数而异(如 register 装饰器返回原函数或注册器)时,为包装器枚举具体签名,静态检查器按调用形态匹配。运行时永远配 `functools.wraps`;三式的选择标准是「签名是否被改变」,面试时按这个判断链讲最清晰。

```python
# file: code/01_语言核心与底层/q1270_decorator_typing.py
from __future__ import annotations

import functools
import inspect
from typing import Callable, TypeVar

F = TypeVar("F", bound=Callable[..., object])   # 流派一:恒等透传


def log_calls(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@log_calls
def greet(name: str, punct: str = "!") -> str:
    return "hi " + name + punct


if __name__ == "__main__":
    print("runtime signature:", inspect.signature(greet))
    print(greet("lily"))
    print("流派二 ParamSpec 见 q1267;流派三 @overload 适合返回类型随参数变化的注册器")
```

**追问**:1) 为什么 `bound=Callable[..., object]` 而不是 `bound=Callable`?——裸 Callable 缺类型参数,静态检查器会拒绝;`[...]` 表示「任意参数表」,是 bound 场景的标准写法。2) 三式怎么分工?——TypeVar(F, bound=Callable) 保持「整个函数对象」类型;ParamSpec 保留参数表并允许改造返回值;overload 表达分支签名;装饰器工厂(带参数)要多包一层泛型函数。3) bound 捕获的细节?——F 约束到 Callable 后,装饰器返回 F 即原函数类型;要在包装体内改签名就用 ParamSpec 而不是 F。4) 生产陷阱?——装饰器返回 Any 让下游全部失明;漏 wraps 丢签名与元信息;overload 桩与实现不一致导致 "no overload variant" 误报。
