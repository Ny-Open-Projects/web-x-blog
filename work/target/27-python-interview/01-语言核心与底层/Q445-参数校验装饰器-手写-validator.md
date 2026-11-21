---
title: [Q445] 参数校验装饰器:手写 validator
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q445 · 参数校验装饰器:手写 validator

> 难度:★★★★ | 标签:装饰器, 校验

**问**:不依赖 pydantic,如何用装饰器 + inspect 实现声明式的参数校验?

**答**:装饰器先 `inspect.signature(func).bind(*args, **kwargs)` 把实参归一化成「参数名 → 值」的映射(apply_defaults 补齐默认值),再按声明逐个校验:规则是类型就用 isinstance,是可调用对象就当谓词。bind 的好处是位置参数/关键字参数/默认值统一处理,不用自己解析。失败时抛 TypeError(类型不符)或 ValueError(值不合法),并报出参数名与实际类型,这是手写校验层的最小可用骨架。

```python
# file: code/01_语言核心与底层/q445_param_validator.py
import functools
import inspect

def validate(**rules):
    """按参数名校验:type 表示类型约束,callable 表示谓词"""
    def deco(func):
        sig = inspect.signature(func)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            for name, checker in rules.items():
                value = bound.arguments[name]
                if isinstance(checker, type):
                    if not isinstance(value, checker):
                        raise TypeError(
                            f"{name} must be {checker.__name__}, got {type(value).__name__}"
                        )
                elif not checker(value):
                    raise ValueError(f"{name} failed predicate with {value!r}")
            return func(*args, **kwargs)
        return wrapper
    return deco

def positive(v):
    return v > 0

@validate(x=int, y=positive)
def scale(x, y):
    return x * y

if __name__ == "__main__":
    print(scale(3, 2.5))
    try:
        scale("3", 2)
    except TypeError as e:
        print("TypeError:", e)
    try:
        scale(3, -1)
    except ValueError as e:
        print("ValueError:", e)
```

**追问**:1) 校验放装饰器还是函数体第一行?——装饰器把契约与实现分离、可跨函数复用;但运行时校验有开销,高频路径要么删掉、要么静态化(类型注解 + mypy)。2) 为什么用 signature.bind 而不是手工拼参数?——bind 统一处理位置/关键字/默认值/*args/**kwargs/仅位置参数(3.8+)各种声明,手工解析必然漏边角;bind 失败抛 TypeError,顺带完成参数数量校验。3) signature 解析的成本结构?——反射解析有开销,标准做法是 import 期解析一次存进装饰器闭包;运行期每次调用多一次 bind 加规则循环,这就是「高频路径静态化」的量化依据。4) 生产陷阱?——`x=int` 对 bool 放行(bool 是 int 子类),isinstance 语义坑要显式排除 bool;以及惯性把校验写成 assert,在 -O 下整层消失。
