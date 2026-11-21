---
title: [Q2337] 真值判定的默认规则:没写 __bool__ 就恒为真
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2337 · 真值判定的默认规则:没写 __bool__ 就恒为真

> 难度:★★★☆☆ | 标签:__bool__, __len__, 真值

**问**:一个自定义类的实例在 `if` 里永远为真吗?什么情况下会为假?

**答**:默认规则是:对象恒为真,除非类定义了 `__bool__` 且返回 False,或定义了 `__len__` 且返回 0——两者都没有,任何实例(哪怕内部数据全空)都是 True。判定优先级是先 `__bool__` 后 `__len__`,只定义其一就按其为准,这常造成误判:比如拿到一个文件对象,`if f:` 判断的是「对象存在」(恒真),不是「文件非空」,想判内容要用 `if f.read():`。`and`/`or` 的短路返回的是操作数本身而不是布尔值,所以 `x or 默认值` 能原样返回 x。写容器类时若忘记实现 `__len__`/`__bool__`,空容器会被误认为真,这是自定义集合类最常见的语义漏洞之一。

```python
# file: code/01_语言核心与底层/q2337_default_truthiness.py
"""真值判定的默认规则:不定义 __bool__ 与 __len__ 的对象恒为真。"""
import io


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


class EmptyBox:
    """什么协议都没定义:内部再空也恒为真。"""


class Box:
    """定义 __len__ 后,空箱为假。"""

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    print("Point(0,0) 真值:", bool(Point(0, 0)))     # True:默认规则
    print("EmptyBox() 真值:", bool(EmptyBox()))      # True

    box = Box()
    print("空 Box 真值:", bool(box))                 # False
    box.items.append("x")
    print("装东西后真值:", bool(box))                # True

    empty_file = io.StringIO("")
    print("空文件对象恒真:", bool(empty_file))        # True
    print("但读出的内容为假:", bool(empty_file.read()))

    print("or 短路返回操作数本身:", Point(0, 0) or "默认点")
```

**追问**:1) 只定义 `__len__` 不定义 `__bool__`,实例真值由谁决定?——由 `__len__` 决定,返回 0 即假;两个都定义时 `__bool__` 优先,`__len__` 是它的回退。2) 默认规则的机制?——PyObject_IsTrue 先查 nb_bool 槽、再查 sq_length、都没有恒真(Q532 的槽位故事);bool(x)、if、while、and/or 全走同一条路。3) 设计含义?——「没写 __bool__ 就恒真」让无 __len__ 的自定义对象空/非空语义要显式实现;与 __eq__/__len__ 的语义一致性是容器类的责任。4) 生产陷阱?——容器类忘写 __len__ 导致空对象为真;__bool__ 返回非 bool 被 CPython 拒绝(TypeError);__bool__ 与 __len__ 矛盾造成 truthiness 漂移。
