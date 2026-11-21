---
title: [Q023] iter 函数的双参数形式与哨兵
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q023 · iter 函数的双参数形式与哨兵

> 难度:★★☆ | 标签:迭代器

**问**:`iter(callable, sentinel)` 这个少见的用法能解决什么问题?

**答**:两参形式返回一个迭代器,反复无参调用 callable,直到返回值等于 sentinel 才停,常见于「读到 EOF/空行为止」的循环,替代不断重复的 while+break 模式,让代码变成声明式的 for。

```python
# file: code/01_语言核心与底层/q023_iter_sentinel.py
from io import StringIO

def read_blocks(stream):
    # 每次调用 stream.readline,读到空字符串哨兵为止
    for line in iter(stream.readline, ""):
        yield line.rstrip("\n")

if __name__ == "__main__":
    fake = StringIO("alpha\nbeta\ngamma")
    for block in read_blocks(fake):
        print("block:", block)

    import functools
    import random

    def roll():
        return random.randint(1, 7)

    rolls = iter(roll, 7)          # 掷到 7 停,本例必停
    print(list(rolls))
```

**追问**:1) for 遍历文件对象时为什么不需要 sentinel?——文件对象自身是迭代器,`__next__` 内部已按行推进并在 EOF 抛 StopIteration。2) 哨兵比较用 == 还是 is?——文档语义是相等比较,所以哨兵要选不可被重载 `__eq__` 的对象(如 `object()` 实例),避免数据值恰好等于哨兵造成提前终止。3) 举个实际用法?——`iter(lambda: f.read(8192), b'')` 分块读二进制直到 EOF,把 while+break 改写成声明式 for,日志轮转读取同理。
