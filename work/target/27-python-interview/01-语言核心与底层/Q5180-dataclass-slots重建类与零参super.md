---
title: "[Q5180] dataclass(slots=True) 重建类与零参 super 失效"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5180 · dataclass(slots=True) 重建类与零参 super 失效

难度：P7 ｜ 标签：dataclass、slots、super、__classcell__、类重建

**问**：为了省内存给一个继承体系加上 `@dataclass(slots=True)`，上线后子类方法一调用就 `TypeError: super(type, obj): obj must be an instance or subtype of type`。方法里写的是最常见的零参 `super().describe()`，语法没错、基类也没变，为什么一加 `slots=True` 就崩？`dataclass` 到底做了什么？为什么 `__init_subclass__` 还会被触发两次、注册表出现重复项？本题与 Q1273（slots 内存收益）、Q559（多继承布局）、Q5140（C3/super）的边界在哪？

**答**：
结论：`@dataclass(slots=True)` 不是"给原类加 `__slots__`"，而是**新建一个类**：它用 `type(cls)(cls.__name__, cls.__bases__, namespace)` 重新创建，把字段搬进 `__slots__`，再返回新类。原类的方法对象被复用，但方法里零参 `super()` 依赖编译器生成的 `__class__` 闭包单元，这个单元**仍指向被装饰的原类**。新类实例的 `type(obj)` 是新类，和闭包里的旧类不是同一个对象 → `super(旧类, obj)` 抛 `TypeError`。同理，重建类会再次触发基类的 `__set_name__`/`__init_subclass__`，按列表追加的注册表会出现两条同名记录；按 `cls` 做键的注册表会保留旧类对象，造成泄漏/身份判断错乱。Q559 讲的是 `__slots__` 与多继承布局冲突（`TypeError: multiple bases have instance lay-out conflict`），Q5140 讲 C3/MRO 与 `super` 的解析顺序；本题专攻"类被重建后 `__class__` cell 失效"。

取舍：`slots=True` 的收益是每实例省一个 `__dict__`（几十到几百字节），代价是失去动态属性、弱引用默认没了（要手动加 `__weakref__`）、pickle 需要 `__getstate__`、以及这类 `super()` 陷阱。继承体系里最稳的做法是：基类不用 slots、只在叶子类用；或者干脆不用零参 `super()`，显式写 `Base.describe(self)` / `super(Child, self)`；再或者用 `attrs`/手写 `__slots__` 并接受同样的约束。给"会被大量实例化、字段固定"的 DTO 用 slots 值得，给"有继承、有 mixin、有 `super()` 链"的领域模型用 slots 往往得不偿失。

实战：事故形态是"内存优化 PR 只加了一个 `slots=True`，单测覆盖了构造/序列化但没覆盖 `super()` 方法，上线后某个子类方法 500"。排查时打印 `Child.describe.__closure__[0].cell_contents is Child` 为 `False` 就是铁证。下面同时展示：闭包 cell 指向旧类、零参 `super()` 报错、显式 `super(Child, self)` 和直接基类调用可用；另外用 `__init_subclass__` 计数说明重建会触发两次钩子。

```python
from dataclasses import dataclass


class Base:
    def describe(self):
        return "base"


@dataclass(slots=True)
class Child(Base):
    x: int

    def describe(self):
        return super().describe() + f":{self.x}"


inner = Child.describe.__closure__[0].cell_contents if Child.describe.__closure__ else None
print("方法闭包里的 __class__ is Child:", inner is Child)

try:
    print(Child(1).describe())
except TypeError as e:
    print("零参 super() ->", type(e).__name__, e)

print("显式 super(Child, self):", super(Child, Child(1)).describe())
print("直接调基类:", Base.describe(Child(1)))
print("__slots__ =", Child.__dict__.get("__slots__"))

calls = []


class HookBase:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        calls.append(cls.__name__)


@dataclass(slots=True)
class HookChild(HookBase):
    y: int


print("__init_subclass__ 调用:", calls)
```

**追问一**：为什么零参 `super()` 会依赖闭包，而不是运行时查 `type(self)`？——编译器看到方法体里出现 `super` 这个名字，就把 `__class__` 作为自由变量塞进方法的闭包，运行时 `super()` 展开成 `super(__class__, <first arg>)`；`__class__` cell 在类体执行时由编译器填充为"正在创建的那个类"。`dataclass(slots=True)` 返回的是另一个类对象，cell 不会跟着更新，于是"旧类 + 新类实例"不匹配。显式 `super(Child, self)` 用的是新类，所以能工作。

**追问二**：重建类还会带来哪些不易察觉的副作用？——至少四类：a) `__init_subclass__`/`__set_name__` 对同一个类名再跑一次，注册表重复（下面用 `calls` 计数可复现）；b) 旧类对象可能被描述符/注册表/`__mro_entries__` 元数据持有，形成"看不见的第二个类"，`isinstance`/`is` 判断分裂；c) `__slots__` 与基类布局冲突（Q559），多继承时直接 `TypeError`；d) pickle 依赖的 `__qualname__`/模块路径指向新类，旧 pickle 可能反序列化失败。给框架类加 slots 前，先 grep 一遍 `super()` 和 `__init_subclass__`。

## 背诵要点
- `dataclass(slots=True)` 会新建类；方法闭包里的 `__class__` 仍指向旧类，零参 `super()` 抛 `TypeError`。
- 修复：显式 `super(Child, self)`/直接基类调用，或基类不用 slots，或避免零参 super。
- 重建会二次触发 `__set_name__`/`__init_subclass__`，注册表重复、旧类对象悬挂；slots 还有多继承布局冲突。

## 复盘追问
- 加 `slots=True` 后子类 `super()` 全崩，如何用 `__class__` cell 解释并给出三种修复？（类重建、闭包旧类、显式 super/基类调用）
- 为什么加 slots 会让插件注册表出现两条同名记录？（类重建二次触发 `__init_subclass__`，按列表/按类对象建键的不同后果）
