---
title: [Q2622] frozen dataclass 的逃生门:object.__setattr__ 与 __dict__ 直写
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2622 · frozen dataclass 的逃生门:object.__setattr__ 与 __dict__ 直写

> 难度:★★★☆☆ | 标签:dataclass, frozen, 不变性

**问**:frozen dataclass 真的不可变吗?`object.__setattr__` 为什么能绕过去?

**答**:frozen dataclass 的不变性靠的是生成的 `__setattr__`/`__delattr__` 抛 `FrozenInstanceError`,属于「约定级」保护而非语言级只读。两条公认逃生门:`object.__setattr__(obj, name, value)` 直接调 object 层的赋值逻辑,绕过被重写的 `__setattr__`;或者干脆改 `obj.__dict__`。这不是 bug——标准库自己就这么用:dataclass 的 `__post_init__` 处理 frozen 字段、以及 `dataclasses.replace` 的内部实现都依赖 `object.__setattr__`。工程边界:frozen 的目的是防止**意外修改**与提供可哈希性,不是安全边界;真需要不可变防御时用 `__slots__` + 覆盖 `__setattr__` 抛错,或把状态设计成「创建后只派生新对象」的函数式风格。

```python
# file: code/01_语言核心与底层/q2622_frozen_escape.py
"""frozen dataclass 的保护机制与两条逃生门。"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    host: str
    port: int


if __name__ == "__main__":
    cfg = Config("db1", 5432)

    try:
        cfg.port = 1
    except Exception as exc:
        print("常规赋值被拦:", type(exc).__name__, exc)

    object.__setattr__(cfg, "port", 15432)     # 逃生门一:object 层赋值
    print("object.__setattr__ 后:", cfg.port)

    cfg.__dict__["port"] = 15433               # 逃生门二:直写实例字典
    print("__dict__ 直写后:", cfg.port, cfg)

    try:
        hash(cfg)
        print("frozen 实例可哈希:", hash(cfg) is not None)
    except TypeError as exc:
        print("不可哈希:", exc)
```

**追问**:1) 为什么 frozen dataclass 默认可哈希?——frozen 生成 `__eq__` 时同步生成 `__hash__`,不可变前提成立才允许哈希;非 frozen 的可变对象被显式排除出可哈希阵营。2) 逃生门的边界?——object.__setattr__(self, name, v) 只该出现在 __post_init__;直写 __dict__ 绕过全部校验(Q2071);frozen 是 Python 层拦截,不是 C 层只读(Q468)——逃生门同样对数据类外的代码敞开。3) replace 派生是正道?——dataclasses.replace 走 __init__ 重跑校验(Q1830);逃生门仅限「构造期补字段」;热更新用「重建+原子替换」。4) 生产陷阱?——逃生门滥用让 frozen 名存实亡;__dict__ 直写绕过 slots/key-sharing 假设;哈希可用的对象字段混入可变容器(Q468)。
