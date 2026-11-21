---
title: [Q2619] Enum 的 _missing_ 钩子:自定义 value 查找与容错
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2619 · Enum 的 _missing_ 钩子:自定义 value 查找与容错

> 难度:★★☆☆☆ | 标签:Enum, _missing_, 容错解析

**问**:枚举按 value 查找失败就抛 ValueError,有没有官方的容错入口?

**答**:有——`Enum` 的类方法钩子 `_missing_(cls, value)`:按值查找 `Color("red")` 找不到成员时,解释器会先调它,返回成员则成功、返回 None 则照常抛 ValueError。这一个钩子就能覆盖最常见的三类容错:大小写归一、空白清洗、把字符串/数字混着解析。注意两条查找路径的区别:`Color("red")` 按 **value** 查(走 `_missing_`),`Color["RED"]` 按 **name** 查(抛 KeyError,不走 `_missing_`),报错信息也不同。3.11 起标准库还支持 `_missing_` 里用 `cls._member_map_` 做更多花活,但 3.9 用最朴素的遍历就够了。

```python
# file: code/01_语言核心与底层/q2619_enum_missing.py
"""Enum 的 _missing_ 钩子:大小写与空白容错的按值查找。"""
import enum


class Color(enum.Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    @classmethod
    def _missing_(cls, value):
        """按值查找失败时进入这里:归一化后重试,失败返回 None。"""
        if isinstance(value, str):
            normalized = value.strip().lower()
            for member in cls:
                if member.value == normalized:
                    return member
        return None


if __name__ == "__main__":
    print("标准查找:  ", Color("red"))
    print("容错查找:  ", Color("  RED "))
    print("按名字查找: ", Color["GREEN"])

    try:
        Color("purple")
    except ValueError as exc:
        print("value 查找失败:", exc)

    try:
        Color["PURPLE"]
    except KeyError as exc:
        print("name 查找失败:", exc)
```

**追问**:1) `_missing_` 里返回了非成员会怎样?——比如返回任意对象,解释器不做类型检查会把它当查找结果返回,所以钩子内要么返回真成员要么返回 None。2) _missing_ 的调用时机?——Color("red")/Color["red"] 查找失败时调用;可做大小写容错、别名映射、旧值迁移;不影响成员枚举与 __members__。3) 与 value/name 双查的关系?——默认按 value 查;_missing_ 补 name 查与自定义映射;查找路径的确定性要文档化。4) 生产陷阱?——钩子返回非成员的「幽灵值」;在 _missing_ 里做重 IO(高频查 Enum);容错映射掩盖数据错误(要记日志)。
