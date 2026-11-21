---
title: [Q468] frozen dataclass 与 __hash__
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q468 · frozen dataclass 与 __hash__

> 难度:★★★☆ | 标签:dataclass, 不可变

**问**:frozen=True 的 dataclass 为什么自动有了 __hash__?「不可变」到底保证了什么?

**答**:普通 dataclass 设 eq=True 生成 __eq__ 同时把 __hash__ 置 None(可变对象可哈希会破坏哈希表契约);frozen=True 生成禁止赋值的 __setattr__(抛 FrozenInstanceError),解释器据此同时生成 __hash__。但「不可变」只到第一层:字段引用的 list/dict 内容依然可改,真正的深不可变需要字段本身不可变(tuple、frozenset)并在 __post_init__ 里对入参做防御性转换。「修改」的惯用法是 dataclasses.replace 生成新实例,配合值语义让对象可安全共享、可做 dict key。

```python
# file: code/01_语言核心与底层/q468_frozen_dataclass.py
from dataclasses import dataclass, field, replace, FrozenInstanceError

@dataclass(frozen=True)
class Config:
    host: str
    port: int = 8080
    tags: tuple = field(default_factory=tuple)   # frozen 也要配不可变容器

if __name__ == "__main__":
    c = Config("db.local", tags=("primary",))
    print(c)
    print("hashable:", hash(c) is not None)
    try:
        c.port = 9090
    except FrozenInstanceError as e:
        print("immutable:", e)
    c2 = replace(c, port=9090)            # 修改 = 派生新实例
    print(c2)
    print({c: "main", c2: "standby"})     # 可作 dict key
    print("same tags object:", c.tags is c2.tags)   # 浅共享:tuple 本身不可变才安全
```

**追问**:1) frozen 实例如何在 __post_init__ 里给自己字段赋值?——生成的 __setattr__ 会拦,惯用法是 `object.__setattr__(self, "x", v)`,绕过冻结仅限初始化期使用。2) 为什么 eq=True 会顺手禁用 __hash__?——可哈希契约要求生命周期内 hash 不变,可变对象的 eq 随内容变化必然违反;dataclass 在「可变+eq」组合上直接把 __hash__ 置 None,强制开发者显式决策。3) frozen 的实现层次?——Python 层拦截:生成抛 FrozenInstanceError 的 __setattr__/__delattr__,底层创建仍走 object.__setattr__,所以不是 C 层只读,绕过手段(以及风险)都在。4) 生产陷阱?——frozen 字段持有 list/dict,浅冻结被误当深冻结,内容照样可变;用 frozen 实例做 dict key 但字段混入可变容器,哈希不变而 eq 漂移,查找行为诡异——字段要么真不可变要么不参与 hash。
