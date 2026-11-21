---
title: [Q531] 反射运算符:__radd__ 与分派顺序
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q531 · 反射运算符:__radd__ 与分派顺序

> 难度:★★★☆ | 标签:运算符, 双下方法

**问**:`10 + v`(v 是自定义类)时 Python 怎么找到正确的加法?NotImplemented 在其中的角色?

**答**:二元运算 a + b 的分派顺序:先试 type(a) 的 __add__,若返回 NotImplemented(或缺失)且 type(b) 不是 type(a) 的子类,再试 type(b) 的 __radd__;两者都 NotImplemented 才抛 TypeError。NotImplemented 不是异常而是哨兵,意思是「我不处理,请给别人机会」——抛 NotImplementedError 反而中断分派链,是自定义运算符最常见的错误。__radd__ 的 self 与参数互换:定义 `__radd__(self, other)` 处理 other + self。反射运算让自定义类型能与 int/str 等内置类型自然协作,无需修改对方。

```python
# file: code/01_语言核心与底层/q531_radd.py
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        if isinstance(other, int):
            return Vector(self.x + other, self.y + other)
        return NotImplemented             # 哨兵:交给对方或失败

    __radd__ = __add__                    # 10 + v 分派到 v.__radd__(10)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

if __name__ == "__main__":
    v = Vector(1, 2)
    print(v + Vector(3, 4))
    print(v + 10)                         # v.__add__(10)
    print(10 + v)                         # int 不支持 → v.__radd__(10)
    try:
        v + "x"                           # 双方都 NotImplemented
    except TypeError as e:
        print("TypeError:", e)
```

**追问**:1) 子类在前有什么例外规则?——若右操作数类型是左操作数类型的**子类**,即使左边有 __add__ 也先试右边的 __radd__,保证子类对运算结果类型的控制权。2) 分派顺序为什么左优先?——左操作数「更可能」知道如何组合,先试左 __add__;返回 NotImplemented 才轮到右 __radd__;两侧都 NotImplemented 解释器抛 TypeError。3) NotImplemented 的角色?——它是哨兵对象不是异常,槽方法必须「无法处理时返回它」;直接抛错会中断整个双分派链,这是自定义数值类型最常见的实现错误。4) 生产陷阱?——自定义类型漏 __radd__ 导致 int + obj 报错;与 numpy 交互时还要考虑 __array_ufunc__ 的分派权;反射方法忘 mirror 对称语义,顺序不同结果不同。
