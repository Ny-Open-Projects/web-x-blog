---
title: "[Q5085] rich comparison 的反射机制与 NotImplemented 的分派原理"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5085 · rich comparison 的反射机制与 NotImplemented 的分派原理

难度：★★★★☆ ｜ 标签：比较协议 / 原理深挖 / NotImplemented

**问**：`a < b` 在 CPython 里到底发生什么？`__lt__` 返回 `NotImplemented` 和返回 `False` 有什么本质区别？为什么 `a == b` 与 `b == a` 在自定义类型上可能一个 True 一个 False？

**答**：
- **结论**：rich comparison 有六个方法（`__lt__ le__ gt__ ge__ eq__ ne__`），CPython 调用规则是**先左后右、带反射**：`a < b` 先试 `type(a).__lt__(a, b)`；若返回 `NotImplemented` 且 `type(b)` 不是 `type(a)` 的合适子类例外，再试反射 `type(b).__gt__(b, a)`；两者都不支持才退到 `id` 比较并抛 `TypeError`。`NotImplemented` 是"我不懂这个操作数组合，请问对方"的协议信号；返回 `False` 则是断言"我懂，答案就是不等"——直接终止反射链。
- **取舍**：`==` 特殊：解释器对 `==`/`!=` 还允许左右两侧**互为反射尝试且不强制同型**，且 `object` 的默认 `__eq__` 是 identity，所以自定义 `__eq__` 返回 NotImplemented 会**回落到默认 identity 语义**（而不是报错）——这是"部分实现"的常用技巧：只声明与同类可比，异类交给对方或 identity。
- **实战**：写跨类型比较的正确姿势：1）异类先 `isinstance` 检查，不认识就返回 `NotImplemented`（别返回 False）；2）子类继承父类比较逻辑时要意识到 MRO 分派顺序（若右操作数类型是左操作数类型的子类，CPython **先试右侧的反射方法**，让子类有机会覆盖）；3）`functools.total_ordering` 能从 `__eq__` + 一个序关系补全其余四个，但每层比较多一次方法调用，热路径可手写全量。

```python
"""rich comparison 反射分派演示（标准库，Python 3.9+）"""
from functools import total_ordering

class Meters:
    def __init__(self, v): self.v = v
    def __repr__(self): return f"Meters({self.v})"
    def __eq__(self, other):
        print(f"  Meters.__eq__ 被调用: {self!r} vs {other!r}")
        if isinstance(other, Meters):
            return self.v == other.v
        return NotImplemented            # 不认识 → 交给对方反射
    def __lt__(self, other):
        print(f"  Meters.__lt__ 被调用: {self!r} vs {other!r}")
        if isinstance(other, Meters):
            return self.v < other.v
        return NotImplemented

class Feet:
    def __init__(self, v): self.v = v
    def __repr__(self): return f"Feet({self.v})"
    def __gt__(self, other):             # Feet 只实现了反射方向
        print(f"  Feet.__gt__ 被调用: {self!r} vs {other!r}")
        if isinstance(other, Meters):
            return self.v * 0.3048 > other.v
        return NotImplemented

print("a < b 分派过程:")
result = Meters(1) < Feet(4)             # 左侧 __lt__ 交白卷 → 反射 Feet.__gt__
print("结果:", result)

print("NotImplemented vs False 的差别:")
class No:
    def __eq__(self, other): return NotImplemented
print(f"No() == 'x' : {No() == 'x'}")     # 双方都 NotImplemented → 回落 identity → False
print(f"No() == No() : {No() == No()}")   # identity 不同 → False（不是 TypeError）
class Wrong:
    def __eq__(self, other): return False # 自断反射链
print(f"Wrong() == 'x' : {Wrong() == 'x'}")

# total_ordering 补全
@total_ordering
class Score:
    def __init__(self, v): self.v = v
    def __eq__(self, o): return isinstance(o, Score) and self.v == o.v
    def __lt__(self, o): return isinstance(o, Score) and self.v < o.v
print("total_ordering:", Score(1) <= Score(2), Score(3) > Score(1))
```

**追问链**
1. `a == b` 的完整分派序是什么？子类何时优先？
   1. 若 `type(b)` 是 `type(a)` 的真子类且覆盖了反射方法，CPython 先调 `type(b).__eq__(b, a)` 再试左侧——保证子类语义优先；其余按"左 → 右反射 → identity 回落"。
   2. 追问：`!=` 默认实现是什么？——3.x 默认 `__ne__` 会自动取 `__eq__` 结果取反（除非显式覆盖），所以覆盖 `__eq__` 时通常不必再写 `__ne__`。
2. 为什么 `NotImplemented` 不能写成 `raise NotImplementedError`？
   1. 后者是"此操作不支持"的异常信号，会直接炸调用栈；前者是协议内协商信号，解释器借此继续尝试反射/回落。混用会让跨类型容器操作（sort、in、dict 查找）无谓抛错。
   2. 追问：hash 和 eq 必须同步的理由在这里如何体现？——dict 查找先 hash 定桶再 `__eq__` 验证，eq 改了 identity 语义而不改 hash，桶内验证就错位（另见 Q5041 事故）。

## 背诵要点
- 分派规则：左方法 → 右反射（子类真子类时右侧优先）→ identity 回落；全 NotImplemented 才 TypeError。
- NotImplemented = "问对方"的协商信号，False = 终止反射的断言；异类比较不认识就返回 NotImplemented。
- `==` 回落 identity，`!=` 默认自动取反 `__eq__`；total_ordering 从 eq+lt 补全但多一层调用。

## 复盘追问
- 代码评审中如何一眼识别"__eq__ 返回 False 应为 NotImplemented"的隐患？用什么测试用例暴露？
- 排序稳定性依赖 `__lt__`，如果比较函数有浮点 NaN 会发生什么？
