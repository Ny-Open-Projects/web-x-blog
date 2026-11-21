---
title: [Q466] dataclass 深水区:field 与 __post_init__
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q466 · dataclass 深水区:field 与 __post_init__

> 难度:★★★★ | 标签:dataclass

**问**:dataclass 里可变默认值怎么写?__post_init__ 和 InitVar 配合能做什么?

**答**:可变默认值必须用 `field(default_factory=list)`,让每个实例拿到新对象——和函数默认参数同源的坑,但 dataclass 在定义期就会对 `tags: list = []` 直接报 ValueError 拦截。field 还能控制 init(False 不进 __init__)、repr、compare 等「这个字段参与哪些生成方法」。__post_init__ 在生成的 __init__ 末尾被调用,做派生字段与跨字段校验;InitVar 声明「只参与初始化」的参数:它进 __init__、传给 __post_init__,但不成为真实字段,不参与 repr/eq。

```python
# file: code/01_语言核心与底层/q466_dataclass_field.py
from dataclasses import dataclass, field, InitVar

@dataclass
class Inventory:
    name: str
    tags: list = field(default_factory=list)          # 可变默认值的正确姿势
    qty: int = 0
    initial_qty: InitVar[int] = 0                     # 只参与初始化
    _cache: dict = field(init=False, default_factory=dict,
                         repr=False, compare=False)   # 内部缓存不参与比较

    def __post_init__(self, initial_qty):
        if initial_qty:
            self.qty = initial_qty

    @property
    def label(self):
        if "l" not in self._cache:
            self._cache["l"] = f"{self.name}:{self.qty}"
        return self._cache["l"]

if __name__ == "__main__":
    a = Inventory("apple", initial_qty=5)
    b = Inventory("banana", tags=["fresh"])
    print(a)
    print(b, b.label)
    print("eq:", a == Inventory("apple", initial_qty=5))
    print("initial_qty is a real field:", "initial_qty" in Inventory.__dataclass_fields__)
```

**追问**:1) field(init=False) 的字段如何在构造后赋值?——只能在 __post_init__ 里赋(它不接收 InitVar 之外的参数,但可以读写 self),或用 object.__setattr__ 配合 frozen。2) InitVar 与普通字段的本质区别?——InitVar 进 __init__、传给 __post_init__,但不是 __dataclass_fields__ 成员,不参与 repr/eq/asdict;适合「只属于构造期的上下文参数」。3) dataclass 的代码生成机制?——装饰器读 __annotations__ 与 field 元数据,生成 __init__ 等方法源码并 exec;frozen/eq/kw_only(3.10+)等开关改变生成模板,生成物带 __dataclass_fields__ 反射入口。4) 生产陷阱?——default_factory 引用模块级可变状态造成实例串数据;有默认值字段后插入新必选字段,位置实参调用方全错——新增字段要么带默认值要么走版本化迁移。
