---
title: "[Q5171] __init_subclass__ 忘记 super 与泛型基类注册时序"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5171 · __init_subclass__ 忘记 super 与泛型基类注册时序

难度：P7 ｜ 标签：PEP 487、Generic、__init_subclass__、__parameters__、插件注册

**问**：插件框架用 `Generic[T]` 做基类、用 `__init_subclass__` 自动注册子类。为什么某个子类明明写的是 `class Handler(Base[int])`，运行时却还能被 `Handler[str]` 二次下标？`__init_subclass__` 里到底该在 `super()` 之前还是之后读 `__parameters__`？这和 Q455（init_subclass 注册与约束）、Q5139（init_subclass 与 class_getitem 插件演进）的边界在哪？

**答**：
结论：`type.__new__` 创建类时先对新类里的描述符调用 `__set_name__`，再调用**直接父类**的 `__init_subclass__`；而 `Generic` 的 `__parameters__` 推导正是挂在 `Generic.__init_subclass__` 里的。子类 hook 里如果只写业务逻辑、忘记 `super().__init_subclass__(**kwargs)`，`Generic` 的钩子就不会执行：具体子类 `Base[int]` 会**继承父类的 `(T,)`**，于是 `Handler[str]` 被运行时接受，类型参数契约彻底失真。更隐蔽的是：hook 执行到 `super()` 之前读 `__parameters__`，看到的是父类继承下来的 `(T,)`；`super()` 之后才变成 `()`。所以注册逻辑要放在 `super()` 之后，且必须 cooperative。

取舍：`__init_subclass__` 适合"类创建即注册"的轻量插件体系，但它没有强制力（挡不住实例化），强约束仍需 `abc`/metaclass。注册表建议用 `cls` 对象而不是类名字符串做键——`@dataclass(slots=True)` 这类会重建类的装饰器会让同名类出现两次（Q5180），字符串键会静默覆盖、列表键会重复。若框架需要拿原始泛型实参，读 `__orig_bases__`（3.12 可用 `types.get_original_bases`），不要指望 `__bases__`，后者已经被 `__mro_entries__` 解析成真实基类了（Q5172）。

实战：事故形态是"插件上线后同一个 handler 被调用两次/被当成模板再次参数化"。下面同时展示正确与错误两条链：正确链在 hook 里调 `super()`，具体子类 `__parameters__ == ()`；错误链漏掉 `super()`，具体子类仍是 `(~T,)`，`BrokenInt[str]` 被错误放行。

```python
from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)      # 关键：继续走 Generic 的钩子
        Box.registry[cls.__name__] = cls
        print(f"  register {cls.__name__}: parameters={cls.__parameters__}")


class IntBox(Box[int]):
    pass


class StrBox(Box[str]):
    pass


class StillGeneric(Box[T]):
    pass


print("IntBox.__parameters__ =", IntBox.__parameters__)
print("StillGeneric.__parameters__ =", StillGeneric.__parameters__)
print("registry =", sorted(Box.registry))


class Broken(Generic[T]):
    def __init_subclass__(cls, **kwargs):
        pass                                     # 忘记 super()


class BrokenInt(Broken[int]):
    pass


print("BrokenInt.__parameters__ =", BrokenInt.__parameters__)   # 本应是 ()
print("BrokenInt[str] 被错误接受 ->", BrokenInt[str])
```

**追问一**：为什么 `super()` 之前读 `__parameters__` 会看到 `(~T,)`，之后才变成 `()`？——`__init_subclass__` 是父类的类方法，`cls` 是刚创建的子类；在 `Generic.__init_subclass__` 运行之前，子类还没有自己的 `__parameters__`，属性查找沿 MRO 落到父类 `Box` 的 `(~T,)`。`Generic` 的钩子根据 `__orig_bases__` 重新推导并写回子类，具体化 `Box[int]` 得到 `()`，仍带自由变量的 `Box[T]` 得到 `(~T,)`。所以"注册时读参数"必须放在 `super()` 之后，否则拿到的是父类的旧值。

**追问二**：既然 `__orig_bases__` 保留了 `Box[int]`，为什么不能直接拿它做运行时类型判断？——`Box[int]` 是 `typing._GenericAlias`，不是类，`isinstance(x, Box[int])` 会抛 `TypeError: Subscripted generics cannot be used with class and instance checks`；它只承载"基类 + 实参"的元数据。运行时判断要用 `__orig_bases__` 里的 `typing.get_origin()` / `get_args()` 自行比对，或者用 `isinstance(x, Box)` 再做参数校验；`__bases__` 只反映解析后的真实基类 `Box`。

## 背诵要点
- 顺序：`__set_name__` → 父类 `__init_subclass__`；`Generic.__parameters__` 由 `Generic.__init_subclass__` 在 `super()` 链里推导。
- 忘记 `super().__init_subclass__()`：具体子类继承父类 `(~T,)`，`Concrete[str]` 被错误接受；hook 内读参数要放在 `super()` 之后。
- 注册表用类对象做键；`__orig_bases__` 保留泛型实参，`__bases__` 已被 `__mro_entries__` 解析成真实基类。

## 复盘追问
- 插件注册表里出现同名类两条记录、且 `Concrete[str]` 不报错，如何用时序与 `__parameters__` 解释并修复？（`super()` 链断裂、参数继承、slots 重建类导致 hook 二次触发）
- 运行时如何从 `class Handler(Base[int])` 中拿回 `int`？为什么不能直接 `isinstance`？（`__orig_bases__` + `get_origin/get_args`，`Box[int]` 不是类）
