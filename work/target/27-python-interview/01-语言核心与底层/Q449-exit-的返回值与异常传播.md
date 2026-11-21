---
title: [Q449] __exit__ 的返回值与异常传播
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q449 · __exit__ 的返回值与异常传播

> 难度:★★★☆ | 标签:上下文管理器, 异常

**问**:__exit__ 返回 True 就能吞异常,这个机制有哪些暗坑?__exit__ 自己抛异常会怎样?

**答**:with 在异常路径上调用 `__exit__(exc_type, exc, tb)`,返回真值表示「异常已处理」,解释器随后恢复正常执行;返回假值则异常继续向外传播。多个 with 嵌套时异常由内向外穿过每一层的 __exit__,每层都有机会拦截。两个暗坑:一,__exit__ 内抛出的新异常会取代原异常,原异常挂在 `__context__` 上形成链;二,正常路径(无异常)也会调用 __exit__,三个参数都是 None,清理逻辑必须兼容这条路径。contextlib.suppress 本质就是「返回 True 的最小实现」。

```python
# file: code/01_语言核心与底层/q449_exit_return_value.py
import contextlib

class Intercept:
    def __init__(self, swallow):
        self.swallow = swallow

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        name = exc_type.__name__ if exc_type else None
        print(f"exit sees: {name}")
        return self.swallow               # True:异常到此为止

class Replacer:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        raise RuntimeError("replaced inside exit")

if __name__ == "__main__":
    with Intercept(swallow=True):
        raise ValueError("swallowed")
    print("continues normally")

    try:
        with Intercept(swallow=False):
            raise ValueError("propagates")
    except ValueError as e:
        print("caught outside:", e)

    try:
        with Replacer():
            raise ValueError("original")
    except RuntimeError as e:
        print("new:", e, "| context:", repr(e.__context__))

    with contextlib.suppress(KeyError):
        {"a": 1}["b"]
    print("suppress done")
```

**追问**:1) with 块里 return 了,__exit__ 还执行吗?——执行,return/break/continue 走的是正常路径,__exit__ 三个参数为 None,资源照样释放。2) __exit__ 抛新异常时原异常去哪?——挂到 e.__context__ 形成隐式链,traceback 打印 "During handling of the above exception";显式因果用 raise ... from,有意丢弃用 from None。3) with 的字节码机制?——异常路径压入异常信息后调用 __exit__,按返回值真伪决定是否继续传播;正常路径同样调用 __exit__(None, None, None),清理逻辑必须兼容两条路径。4) 生产陷阱?——__exit__ 随手返回 True 吞掉一切异常掩盖业务错误,只应在明确处理的类型上返回真值;以及 __exit__ 里做可能失败的 flush/close,把资源清理升级成异常替换,要二次保护。
