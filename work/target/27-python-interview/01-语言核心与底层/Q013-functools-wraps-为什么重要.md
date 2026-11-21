---
title: [Q013] functools.wraps 为什么重要
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q013 · functools.wraps 为什么重要

> 难度:★★☆ | 标签:装饰器

**问**:不加 `@functools.wraps` 会出什么问题?

**答**:包装后 `__name__`、`__doc__`、`__module__`、`__wrapped__` 等元信息会变成 wrapper 自己的,影响调试、日志、文档生成,以及依赖函数签名的框架(如 `inspect.signature`)。`functools.wraps` 通过 `functools.update_wrapper` 把原函数元信息拷贝到 wrapper 上,并设置 `__wrapped__` 指向原函数,便于用 `inspect.unwrap` 还原。

```python
# file: code/01_语言核心与底层/q013_wraps.py
import functools
import inspect

def deco_no_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def deco_with_wraps(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@deco_no_wraps
def f1():
    """doc of f1"""

@deco_with_wraps
def f2():
    """doc of f2"""

if __name__ == "__main__":
    print(f1.__name__, "|", f1.__doc__)  # wrapper | None
    print(f2.__name__, "|", f2.__doc__)  # f2 | doc of f2
    print(inspect.signature(f2))         # 还原真实签名
```

**追问**:1) 叠加了多层 wraps 的装饰器链,怎么拿到最原始的函数?——沿 `__wrapped__` 属性逐层向上,或用 `inspect.unwrap` 一步到位。2) wraps 具体拷贝什么?——通过 `functools.update_wrapper` 拷贝 `__module__`/`__name__`/`__qualname__`/`__doc__`/`__dict__`,并设置 `__wrapped__` 指向原函数供 `inspect.unwrap` 使用。3) 签名信息靠什么补齐?——`functools.wraps` 不改 wrapper 的参数列表;要签名也一致需在 wrapper 上设置 `__signature__ = inspect.signature(func)`,否则 `inspect.signature` 仍看到 `(*args, **kwargs)`。
