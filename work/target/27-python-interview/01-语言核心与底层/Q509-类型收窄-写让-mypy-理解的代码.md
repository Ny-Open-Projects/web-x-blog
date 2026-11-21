---
title: [Q509] 类型收窄:写让 mypy 理解的代码
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q509 · 类型收窄:写让 mypy 理解的代码

> 难度:★★★☆ | 标签:typing, mypy

**问**:Optional 值用之前 mypy 一直报错,怎么「收窄」才能让它闭嘴且不失检查?

**答**:收窄 nárrowing 是静态检查器根据控制流把类型缩小的行为:is None 判断、isinstance、assert、len() 判断等都会触发,分支内类型自动精确。反模式是用 cast 强行哄过或用 # type: ignore 注释——那是掩盖问题;收窄是「给检查器证明」而非「让它闭嘴」。写收窄友好的代码的习惯:尽早判 None 并提前 return、用 isinstance 分派而不是 hasattr 探测、dict.get 后立刻判空、避免把 Optional 存进可变容器(收窄会被后续赋值打破)。assert 也是收窄手段,但 -O 下消失,所以只用于内部不变式。

```python
# file: code/01_语言核心与底层/q509_type_narrowing.py
from typing import Optional, Union

def parse(raw: Optional[str]) -> int:
    if raw is None:                       # 收窄:此后 raw 是 str
        return 0
    return int(raw)

def to_str(value: Union[int, str]) -> str:
    if isinstance(value, int):            # isinstance 分支收窄
        return str(value)
    return value.upper()

def get_setting(store: dict, key: str) -> int:
    value = store.get(key)
    if value is None:
        return 0
    return value                          # mypy 已知是 int

if __name__ == "__main__":
    print(parse(None), parse("42"))
    print(to_str(7), to_str("hi"))
    print(get_setting({"k": 5}, "k"), get_setting({}, "k"))
```

**追问**:1) 为什么「Optional 存进 list 再取出来」会丢收窄?——收窄只作用于当前变量绑定,容器取值是新的表达式、类型回到 Optional;要在容器层面解决就换 TypedDict/dataclass 的确定字段。2) mypy 的收窄来自什么?——控制流分析:is 检查、真值判断、assert、海象表达式、match(3.10 结构化);重新赋值会使收窄失效;TypeGuard(PEP 647)可写自定义收窄函数。3) 收窄的底层模型?——检查器为每个分支维护绑定表(narrowed types),按语句更新;函数边界收窄丢失,因为类型是按签名传递的——所以「先收窄再传参」或把谓词做成 TypeGuard。4) 生产陷阱?——用 assert isinstance 做生产收窄,-O 下断言消失、语义也被滥用;把收窄结果传给另一个函数又回到 Optional;该用 Literal+match 的地方堆 if-else 链。
