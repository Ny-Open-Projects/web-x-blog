---
title: [Q5140] super() 与 C3 线性化 MRO 的原理深挖
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5140 · super() 与 C3 线性化 MRO 的原理深挖

难度：P7 | 标签：super、MRO、C3 线性化、协作多继承

**问**：`super()` 为什么不是"调用父类"而是"调用 MRO 的下一个"？C3 线性化如何解决菱形继承，什么继承结构会触发 `TypeError: Cannot create a consistent MRO`？零参数 super() 的魔法是怎么实现的？

**答**：

**结论**：Python 2.2+ 用 C3 线性化取代旧式深度优先 MRO：对 `class C(A, B)`，`C.__mro__` 保证 (1) 子类先于父类、(2) 基类间保持声明顺序、(3) 每个基类在序列中只出现一次且其派生类都在它前面。super(C, obj) 查的是 `type(obj).__mro__` 中 C 之后的下一个类，所以菱形结构 `D(B, C)`、`B(A)`、`C(A)` 下 A 只被初始化一次——前提是链条上每个类都用 `super().__init__()` 协作。谁破坏协作（直接 `A.__init__(self)` 或不调用 super），就会出现"跳过某个类"或"重复初始化"。MRO 不可满足的典型：`class X(A, B)` 而 B 是 A 的子类（基类顺序与"派生先于基类"冲突）。

**取舍**：零参数 super() 依赖编译器注入的两个隐藏参数 `__class__`（词法闭包单元格）与 `self`（第一个参数），所以它只在函数体内有效，`super()` 写进列表推导/独立函数会报 `RuntimeError: super(): no arguments`。混入类设计原则：Mixin 只用 super 链、构造参数用 `**kwargs` 透传、避免两个 Mixin 都"必占"同一参数名。

**实战**：Mixin 参数透传事故是协作多继承的高发雷区：两个 Mixin 各自消费同名 kw 后从 kwargs 删除，super 链上的其他类拿不到。诊断工具：`cls.__mro__` 直接看序列，`inspect.getmro` 等价。

```python
class A:
    def __init__(self, **kw):
        print("A init")
        super().__init__(**kw)          # 协作：透传给 MRO 下一环（object）

class B(A):
    def __init__(self, b_flag=False, **kw):
        print("B init, b_flag =", b_flag)
        super().__init__(**kw)

class C(A):
    def __init__(self, c_id=None, **kw):
        print("C init, c_id =", c_id)
        super().__init__(**kw)

class D(B, C):
    pass

print("D.__mro__ =", [c.__name__ for c in D.__mro__])
D(b_flag=1, c_id=7)                     # B -> C -> A，A 只跑一次

# super 的真实语义：MRO 上 D 之后是 B，即使你在 C 里写 super
class E(C):
    def __init__(self, **kw):
        print("E super ->", type(self).__mro__[1].__name__)
        super().__init__(**kw)
E()                                     # type(self) 是 E：下一环是 C

# C3 不可满足的例子
class Base: pass
class Mid(Base): pass
try:
    class Bad(Base, Mid):               # 基类顺序与派生优先冲突
        pass
except TypeError as e:
    print("C3 失败 ->", e)
```

**追问 1**：Python 2.2 引入 C3 前的旧式 MRO 有什么问题？
答：深度优先会在菱形结构里让公共基类被访问两次（初始化两次），且基类顺序可能与"派生先于基类"矛盾；C3 用线性化算法一次性解决一致性与局部优先级。

**追问 2**：`super().__init__` 与 `Parent.__init__(self)` 在多继承下的具体差异？
答：后者硬编码父类且在菱形里跳过其他协作类（A 可能漏初始化或双初始化）；前者沿 `type(self).__mro__` 动态走，是唯一保证菱形收敛的写法——但代价是调用目标依赖运行时实例类型，Mixin 里 super 的下一个类是声明顺序决定的，不可假设。

**追问 3**：如何让 super 链在某个 Mixin 处提前终止？
答：定义终点类重写方法且不调 super（类似 Django 中间件链的短路），或让 MRO 末端是 object——`object.__init__` 收到多余 kw 会抛 TypeError，这是排查"kwargs 没被消化完"报错的常见出处。

## 背诵要点

- super 是"MRO 下一环"不是"父类"；菱形收敛靠全链 super 协作，硬编码 Parent.__init__ 会漏/重初始化。
- C3 保证：子先于父、保持声明顺序、每类一次；`class X(A, B)` 且 B 是 A 子类则 TypeError。
- 零参 super 依赖编译器注入的 __class__ 单元格与 self，仅在函数体内有效；object.__init__ 拒收多余 kwargs。

## 复盘追问

- Mixin 框架如何防御"kw 被上游消费导致下游拿不到"？(提示：命名空间化参数前缀 + 启动期链路自检)
- 有没有办法在不跑代码的情况下验证 MRO 可满足？(提示：c3 线性化静态计算 + 单元测试固化 __mro__)
