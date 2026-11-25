---
title: "[Q5172] __mro_entries__ 与非类型基类的真实替换"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5172 · __mro_entries__ 与非类型基类的真实替换

难度：P7 ｜ 标签：PEP 560、__mro_entries__、types.resolve_bases、泛型别名

**问**：`class X(list[int])` 为什么合法？`list[int]` 明明不是类，解释器怎么把它变成真实基类？自己写一个 `Table[int]` 风格的声明式别名，为什么 `X.__bases__` 里看到的是 `list` 而不是 `list[int]`？`__orig_bases__` 和 `__mro_entries__` 各保留了什么？与 Q5139（class_getitem 插件注册）、Q5161（PEP 695 类型参数内省）的边界在哪？

**答**：
结论：类创建时，解释器先对每个 base 调 `types.resolve_bases()`：若对象定义了 `__mro_entries__(bases)`，就用它的返回值**替换**该 base，且替换必须返回 tuple；`list[int]` 是 `types.GenericAlias`，它的 `__mro_entries__` 返回 `(list,)`，所以 `X` 真正继承的是 `list`，`list[int]` 只作为声明元数据留在 `__orig_bases__` 里。`__mro_entries__` 是"让非类型对象能出现在 class 语句基类位置"的唯一协议，也是 PEP 560 把 `typing` 特例下沉到语言层的关键：`Generic[T]`、`Protocol`、`List[int]` 都靠它。

取舍：这个协议只该用于"承载基类 + 元数据"的别名对象，不要把任意工厂对象伪装成基类——它会参与 MRO/C3、元类选择和 `__init_subclass__`，返回非类型或非 tuple 会直接 `TypeError`。运行时想恢复声明式实参，必须读 `__orig_bases__`（3.12 的 `types.get_original_bases()` 会处理继承链），`__bases__` 已经被解析、信息不可逆丢失。与 Q5139 的区别：那张卡讲"用 `__init_subclass__` + `__class_getitem__` 做插件注册"的应用层写法；本题讲"类创建前 base 如何被替换"的协议层机制。Q5161 则管 PEP 695 的 `__type_params__` 内省，不涉及 base 替换。

实战：事故形态是"框架用 `Table[int]` 做声明，运行时想根据 `int` 找列类型，结果遍历 `__bases__` 只看到 `Table`，元数据全丢"。下面现场实现一个带标签的别名，观察 `__mro_entries__` 的调用、`__bases__` 与 `__orig_bases__` 的差异，并演示返回值不是 tuple 时的报错。

```python
import types


class Base:
    tag = "base"


class Alias:
    def __init__(self, origin, label):
        self.origin = origin
        self.label = label

    def __mro_entries__(self, bases):
        print("  __mro_entries__ 收到 bases =", bases)
        return (self.origin,)

    def __repr__(self):
        return f"Alias({self.origin.__name__}, {self.label!r})"


class Demo(Alias(Base, "demo")):
    pass


print("Demo.__mro__ =", Demo.__mro__)
print("Demo.__orig_bases__ =", Demo.__orig_bases__)
print("resolve_bases =", types.resolve_bases((Alias(Base, "x"),)))
print("Demo().tag =", Demo().tag)
print("内置泛型别名:", types.resolve_bases((list[int],)))


class BadAlias:
    def __mro_entries__(self, bases):
        return 42                       # 必须是 tuple


try:
    class Nope(BadAlias()):
        pass
except TypeError as e:
    print("返回值不是 tuple ->", type(e).__name__, e)
```

**追问一**：`__mro_entries__` 的返回值还能再被解析吗？元类冲突按哪一组 bases 判定？——返回值里的元素仍会走同一套 base 解析（可以继续是带 `__mro_entries__` 的别名），最终必须落到类型；元类选择、C3 线性化、`__set_name__`/`__init_subclass__` 都用**解析后**的 bases，`__orig_bases__` 只用于内省。所以一个别名如果解析出两个基类，会实打实影响 MRO，不能把它当"注释"用。

**追问二**：为什么 `Demo.__orig_bases__` 在子类里可能"看起来不对"？——`__orig_bases__` 是普通类属性，子类没有自己的基类声明时会继承父类的值；多层继承下要沿 MRO 找"最近一个自己声明了 bases 的类"，或直接用 3.12 的 `types.get_original_bases(cls)`，它按 `__orig_bases__` 的语义做了继承链处理。直接读 `cls.__orig_bases__` 在中间层会拿到祖先的声明，是元数据框架常见的误判来源。

## 背诵要点
- 类创建前 `types.resolve_bases` 用 `__mro_entries__` 把非类型 base 替换成真实类型，返回值必须是 tuple。
- `list[int]` 的 `__mro_entries__` 返回 `(list,)`；`__bases__`/MRO 用解析结果，`__orig_bases__` 保留声明。
- `__orig_bases__` 会被继承；多层继承用 `types.get_original_bases()`，不要直接读属性。

## 复盘追问
- `class X(Table[int])` 能创建，但框架按 `__bases__` 找不到 `int`，如何解释并修复？（`__mro_entries__` 替换、`__orig_bases__`/`get_original_bases` 取实参）
- 自定义别名让 `__mro_entries__` 返回两个类会带来什么连锁影响？（MRO/C3、元类冲突、`__init_subclass__` 与描述符注册都按解析后的 bases 执行）

## 背诵要点
- 类创建前 `types.resolve_bases` 用 `__mro_entries__` 把非类型 base 替换成真实类型，返回值必须是 tuple。
- `list[int]` 的 `__mro_entries__` 返回 `(list,)`；`__bases__`/MRO 用解析结果，`__orig_bases__` 保留声明。
- `__orig_bases__` 会被继承；多层继承用 `types.get_original_bases()`，不要直接读属性。

## 复盘追问
- `class X(Table[int])` 能创建，但框架按 `__bases__` 找不到 `int`，如何解释并修复？（`__mro_entries__` 替换、`__orig_bases__`/`get_original_bases` 取实参）
- 自定义别名让 `__mro_entries__` 返回两个类会带来什么连锁影响？（MRO/C3、元类冲突、`__init_subclass__` 与描述符注册都按解析后的 bases 执行）
