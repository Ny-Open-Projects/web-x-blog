---
title: [Q2339] += 与 __iadd__ 的返回值契约
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2339 · += 与 __iadd__ 的返回值契约

> 难度:★★★☆☆ | 标签:__iadd__, 运算符协议, 别名

**问**:为什么 `__iadd__` 忘了 return 会让对象变成 None?+= 的完整执行契约是什么?

**答**:`a += b` 的执行分两步:若 a 的类型定义了 `__iadd__`,调它做原地修改,然后把它的返回值重新绑定回名字 a——契约要求原地实现必须 `return self`,忘了 return 就隐式返回 None,a 从此指向 None;若没定义 `__iadd__`,回退到 `__add__` 新建对象再绑定。这解释了可变与不可变的分歧:list 定义了 `__iadd__` 返回自身,别名同步变化;tuple 没有,回退 `__add__` 生成新对象,别名不动。自定义可变类实现 `__iadd__` 时,「修改自身 + 返回 self」是必须成对出现的动作;而实现 `__add__` 的不可变类则绝不能改自身,必须返回新实例。混用两种语义是最常见的事故源。

```python
# file: code/01_语言核心与底层/q2339_iadd_contract.py
"""+= 的返回值契约:__iadd__ 的返回值会成为左侧名字的新绑定。"""


class Gauge:
    """正确示范:原地修改并 return self。"""

    def __init__(self, value):
        self.value = value

    def __iadd__(self, delta):
        self.value += delta
        return self


class BrokenGauge:
    """反面教材:只改内部忘了 return,隐式返回 None。"""

    def __init__(self, value):
        self.value = value

    def __iadd__(self, delta):
        self.value += delta
        # 缺了 return self


if __name__ == "__main__":
    a, b = [1, 2], None
    b = a
    a += [3]
    print("list += 原地改,b 同步变化:", b)

    t, alias = (1, 2), None
    alias = t
    t += (3,)
    print("tuple += 新建对象,alias 不动:", alias, "| t:", t)

    g = Gauge(10)
    g += 5
    print("Gauge += 后:", g.value)

    bg = BrokenGauge(10)
    bg += 5
    print("BrokenGauge += 后左侧名字变成:", bg)
```

**追问**:1) 不可变类型实现 `+=` 时该实现哪个方法?——只需 `__add__`(解释器回退调用),返回新对象;实现 `__iadd__` 反而会让别人误以为它是可变类型。2) 返回值契约?——__iadd__ 返回 self(就地修改)或新对象(重绑定语义),结果重新绑定到名字;+= 先试 __iadd__,NotImplemented/缺失才回退 __add__ 加赋值(Q530/2070 相关行为)。3) 与 CPython 特化的关系?——str += 的「id 不变」是 refcount==1 时的实现优化,语义上仍是新对象;自定义 __iadd__ 返回新对象完全合法。4) 生产陷阱?——__iadd__ 返回 None(以为不用返回值);可变语义与返回新对象混用让调用方困惑;多线程下 += 三步不原子。
