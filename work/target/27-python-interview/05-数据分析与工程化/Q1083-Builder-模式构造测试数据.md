---
title: [Q1083] Builder 模式构造测试数据
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1083 · Builder 模式构造测试数据

> 难度:★★★☆ | 标签:测试数据, 设计模式

**问**:一个接口要 20 个字段,测试只关心 2 个,怎么构造测试数据不把用例淹没?

**答**:Builder 模式:构造器内置一组合法默认值,链式方法只覆盖测试关心的字段,`UserBuilder().with_age(17).inactive().build()` 一行造出"恰好体现意图"的数据。默认值的设计原则是"合法且中性",让断言失败的噪音最小;关键属性显式写、无关属性靠默认。相比裸 dict,Builder 还能把"合法组合"的知识沉淀下来,新增字段时只改一处默认值,几十个测试自动跟随。

```python
# file: code/05_数据分析与工程化/q1083_builder_pattern.py

class UserBuilder:
    def __init__(self):
        self._data = {"id": 1, "name": "alice", "age": 30, "active": True}

    def with_name(self, name):
        self._data["name"] = name
        return self

    def with_age(self, age):
        self._data["age"] = age
        return self

    def inactive(self):
        self._data["active"] = False
        return self

    def build(self):
        return dict(self._data)

def is_active_minor(user):
    """业务规则:未成年且处于激活态是非法组合"""
    return user["age"] < 18 and user["active"]

if __name__ == "__main__":
    base = UserBuilder().build()
    minor = UserBuilder().with_age(17).build()
    minor_inactive = UserBuilder().with_age(17).inactive().build()
    assert not is_active_minor(base), "默认成年用户是合法组合"
    assert is_active_minor(minor), "未成年且激活正是要测的非法组合"
    assert not is_active_minor(minor_inactive), "未成年但未激活是合法组合"
    print(base, minor, minor_inactive)
```

**追问**:
- 追问 1:Builder 和工厂函数怎么选?—— 两三个可变字段用工厂函数 `make_user(**kw)` 就够,字段多、组合语义复杂才上 Builder。
- 追问 2:默认值硬编码的坏处?—— 测试与生产校验规则脱节,好的做法是 Builder 默认值调用生产端的 schema 生成合法样本。
