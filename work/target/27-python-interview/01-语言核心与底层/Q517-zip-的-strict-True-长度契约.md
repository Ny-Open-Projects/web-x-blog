---
title: [Q517] zip 的 strict=True:长度契约
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q517 · zip 的 strict=True:长度契约

> 难度:★★☆☆ | 标签:zip, 迭代器

**问**:zip 静默截断短的那个序列,为什么是坑?strict=True 之后呢?

**答**:zip 按最短者停止——设计上适合无穷流配对,但两个「本应等长」的序列(字段名与值、keys 与 rows)长度不一致时,截断会把 bug 变成静默数据丢失,等下游发现已经离案发地很远。Python 3.10 给 zip 加 strict=True:长度不齐立即 ValueError,把契约违例暴露在案发现场(strict 参数为 3.10+ 新增,低版本解释器不接受该关键字,演示自动跳过)。经验法则:长度是「必须相等」的语义(表格列、坐标对)用 strict=True;「以短为准」的语义(配对可用项)才允许默认截断;itertools.zip_longest 处理「以长为准 + 填充」。

```python
# file: code/01_语言核心与底层/q517_zip_strict.py
import sys

names = ["a.txt", "b.txt"]
sizes = [100, 200, 300]                       # 长度不齐的脏数据

if __name__ == "__main__":
    for name, size in zip(names, sizes):      # 默认:静默丢掉 300
        print("truncating:", name, size)

    if sys.version_info >= (3, 10):
        try:
            for name, size in zip(names, sizes, strict=True):
                print("strict:", name, size)
        except ValueError as e:
            print("strict caught:", e)
    else:
        print(f"该特性需要 Python 3.10+,当前 {sys.version_info.major}.{sys.version_info.minor},演示跳过")

    from itertools import zip_longest
    for name, size in zip_longest(names, sizes, fillvalue=0):
        print("longest:", name, size)
```

**追问**:1) strict 是运行时检查,静态能防吗?——不能,长度只有运行时可知;静态能做的是把「并行序列」重构为「对象列表」,长度错在构造时就报出来。2) 默认截断语义掩盖了什么?——多余元素被静默丢弃,配对数据(id/成绩)错位而不报错;strict=True(3.10+)长度不等抛 ValueError,把数据漂移从「线上错账」提前到「当场炸」。3) 底层机制?——zip 是迭代器组合,任一方 StopIteration 即停止;strict 模式在停止后还检查其余迭代器是否耗尽;zip_longest 用填充值补长尾,是另一路语义。4) 生产陷阱?——并行 list 模式应重构为 dataclass/TypedDict 对象列表(构造期校验);把 zip_longest 用在等长数据上掩盖真实错误;数据漂移只在统计报表里被发现,损失已造成。
