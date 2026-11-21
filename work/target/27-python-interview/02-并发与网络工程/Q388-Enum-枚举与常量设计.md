---
title: [Q388] Enum 枚举与常量设计
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q388 · Enum 枚举与常量设计

> 难度:★★☆ | 标签:Enum, 常量, 设计

**问**:为什么不用裸字符串/数字常量表示状态?如何设计一个规范的枚举?

**答**:裸常量无类型检查、无成员约束、易拼错。`enum.Enum` 提供:成员不可变、可迭代、防重复(`@unique`)、可比较身份。设计规范:①值用 `auto()` 或稳定字符串(入库用 str 值,别让 DB 依赖 int 顺序);②持久化用 `StrEnum`(3.11+)或继承 `str, Enum`,序列化天然是字符串;③和值互转用 `Status("paid")` / `.name`;④非法值转换时捕获 ValueError。复杂状态流转建议在枚举上定义 `can_transition` 方法,把状态机收进类型。

```python
# file: code/02_并发与网络工程/q388_enum.py
"""枚举设计:StrEnum 风格状态机。"""
from enum import Enum, auto


class Status(str, Enum):     # 继承 str,JSON 序列化直接得到字符串
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DONE = "done"


# 合法状态流转表:把状态机收进类型
TRANSITIONS = {
    Status.PENDING: {Status.PAID},
    Status.PAID: {Status.SHIPPED},
    Status.SHIPPED: {Status.DONE},
    Status.DONE: set(),
}


def can_transition(src: Status, dst: Status) -> bool:
    return dst in TRANSITIONS[src]


if __name__ == "__main__":
    import json
    order = {"id": 1, "status": Status.PAID}
    print("序列化:", json.dumps(order))          # 直接输出 "paid"

    print("字符串转枚举:", Status("paid") is Status.PAID)
    try:
        Status("unknown")
    except ValueError as e:
        print("非法值报错:", e)

    print("paid -> shipped:", can_transition(Status.PAID, Status.SHIPPED))
    print("done -> paid  :", can_transition(Status.DONE, Status.PAID))
    print("遍历成员:", [s.value for s in Status])
```

**追问**:
- `IntEnum` 什么时候用?需要和 C/协议整数常量互通时;纯业务状态更推荐 str 枚举,可读且库表无需猜含义。
- 两个成员同值会怎样?后者成为前者的别名;要禁止用 `@unique` 装饰器,重复即抛错。
