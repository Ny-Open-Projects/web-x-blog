---
title: [Q1808] 协作式多继承:super 链上的 kwargs 传递与耗尽
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1808 · 协作式多继承:super 链上的 kwargs 传递与耗尽

> 难度:★★★★★ | 标签:多继承, super, MRO

**问**:多继承里每个 mixin 的 __init__ 都收 **kwargs 再 super().__init__(**kw),这套协作式初始化的正确姿势与失败形态是什么?

**答**:协作式多继承的契约是:每个 __init__ 只认领自己关心的命名参数,其余原样 **kw 传给 super(),沿 MRO(Task -> TimedMixin -> TaggedMixin -> Base)逐层消化;链尾用 Base 接住没人认领的 kwargs 并不再上传——若继续 super() 到 object.__init__,多余关键字会 TypeError,这就是「kwargs 的耗尽」必须在链尾处理的原因。失败形态两类:① 直接调父类名 Base.__init__(self) 绕过 super 链,后续 mixin 全部初始化——Q032 说的「super 是沿 MRO 的下一个」在这里具体成灾,demo 里 Broken 的 timeout 就是没拿到;② 链尾不留收尾层,遗留 kwargs 打到 object 上报错。混入设计三条军规:mixin 不调 object.__init__、签名一律带 **kw、认领参数全部 keyword-only 以免位置参数错位。

```python
# file: code/01_语言核心与底层/q1808_cooperative_mi.py
"""协作式多继承:super 链上的 kwargs 传递与耗尽。"""


class Base:
    def __init__(self, **kw):
        self.leftover = kw          # 链尾:接住没人认领的 kwargs,不再上传
        print("Base 收尾,剩余:", set(kw))


class TimedMixin:
    def __init__(self, timeout=None, **kw):
        self.timeout = timeout
        print("TimedMixin 认领 timeout")
        super().__init__(**kw)


class TaggedMixin:
    def __init__(self, tags=(), **kw):
        self.tags = tags
        print("TaggedMixin 认领 tags")
        super().__init__(**kw)


class Task(TimedMixin, TaggedMixin, Base):
    pass


class Broken(Task):
    def __init__(self, **kw):
        Base.__init__(self)         # 反例:绕过 super 链,其他 mixin 全饿死


if __name__ == "__main__":
    print("MRO:", [c.__name__ for c in Task.__mro__])
    t = Task(timeout=5, tags=("a",), name="job1")
    print("timeout:", t.timeout, "| tags:", t.tags, "| 没人认领:", t.leftover)
    print("--- 反例 ---")
    b = Broken(timeout=9)
    print("Broken.timeout:", getattr(b, "timeout", "没拿到"))
```

**追问**:1) MRO 顺序写反会怎样?——认领顺序变化,默认值覆盖关系跟着变;参数不冲突时行为相同,冲突时后进链的默认值赢,这正是「mixin 在前、基类在后」惯例的来源。2) kwargs 协作协议?——每层认领自己关心的 kwargs、其余原样转发;耗尽到 object.__init__ 时必须为空,残留即 TypeError——这就是「不认领要转发」的强制力。3) 协作式初始化的完整链?——super().__init__(**kwargs) 按 MRO 走,每个 mixin 只处理自己的部分;菱形继承下 __init__ 只走一次(MRO 线性化)。4) 生产陷阱?——某层吞掉 kwargs 不转发,object 收到残留崩溃;**kwargs 与显式参数混用时签名漂移;默认值在两层重复定义,链序决定谁赢。
