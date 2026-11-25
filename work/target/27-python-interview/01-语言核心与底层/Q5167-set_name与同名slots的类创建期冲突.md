---
title: "[Q5167] __set_name__ 与同名 __slots__ 的类创建期冲突"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5167 · __set_name__ 与同名 __slots__ 的类创建期冲突

难度：P7 ｜ 标签：__set_name__、__slots__、描述符、type.__new__、类创建期

**问**：描述符的 `__set_name__` 到底在类创建的哪一步被调用？为什么 `__slots__ = ("d",)` 和类体里的 `d = SomeDescriptor()` **同名**会在类定义时直接抛 `ValueError`，而不是安静覆盖？如果 `__set_name__` 自身抛异常，外层看到的异常类型是什么、CPython 还会额外打印什么？这类"看起来只是省内存的写法"为什么会在 ORM/序列化库的字段收集逻辑里变成事故？

**答**：
结论：CPython 的 `type.__new__` 按固定顺序建类：① 处理 `__slots__`，为每个 slot 名创建 `member_descriptor` 并写进类字典；② 遍历类字典里所有带 `__set_name__` 的对象，调用 `owner.__set_name__(cls, name)`。当 `__slots__` 里的名字与类变量同名时，第一步已经放了一个 slot 描述符在 `d` 上，第二步的类字典里 `d` 又指向你的自定义描述符——两者冲突，`type.__new__` 直接抛 `ValueError: 'd' in __slots__ conflicts with class variable`，类根本创建失败（不是运行时行为）。至于 `__set_name__` 自身抛异常：3.12 里它**原样向外传播**（抛 `ZeroDivisionError` 就是 `ZeroDivisionError`，不包装成 `RuntimeError`），同时 CPython 会向 stderr 额外打印一行 `Error calling __set_name__ on ...` 诊断信息——所以排查时同一错误会出现两处输出，别误以为是两次调用。

取舍："用 `__slots__` 省内存"与"用描述符做字段收集"在命名上必须**显式避让**：slot 名与描述符名不能相同。ORM 库常用"描述符名 = 字段名"的约定（如 `name = Column(str)`），当用户图省事加 `__slots__ = ("name",)` 时就在 import 期炸——防线是在元类里检测 `__slots__` 与注解/描述符名的交集，给出比 `ValueError` 更可操作的报错；或者统一改用 `dataclass(slots=True)`（它帮你在生成 slots 时跳过已有字段描述符）。

实战：事故形态是"给 model 加 `__slots__` 优化内存，服务启动即崩"，堆栈止于类定义行、看不出是描述符冲突——记住两条特征：`ValueError ... conflicts with class variable` 与 stderr 上那行 `Error calling __set_name__ on ...`（后者是原异常外的附加诊断，不是包装）。排查先打印 `类.__dict__` 里同名键的两类描述符，再决定改名还是换 `dataclass(slots=True)`。下面把正常路径、同名冲突、`__set_name__` 异常原样传播三种情况跑出来。

```python
class Desc:
    def __set_name__(self, owner, name):
        print("  __set_name__:", owner.__name__, "->", name)
    def __get__(self, obj, owner=None):
        return "desc-value"

# 1) 正常路径：slot 名与描述符名不同，__set_name__ 在类创建时触发
class Ok:
    __slots__ = ("x",)
    d = Desc()
print("Ok:", Ok.__slots__, "dict?", hasattr(Ok(), "__dict__"))

# 2) 冲突：同名 -> 类定义直接 ValueError，类未创建
try:
    class Bad:
        __slots__ = ("d",)      # 与下面的类变量同名
        d = Desc()
except ValueError as e:
    print("ValueError  :", e)

# 3) __set_name__ 自身抛异常 -> 3.12 原样传播 + stderr 附加诊断行
class Boom:
    def __set_name__(self, owner, name):
        raise ZeroDivisionError("boom inside")

try:
    class Zap:
        field = Boom()
except ZeroDivisionError as e:                # 原异常类型，不是 RuntimeError
    print("propagated:", type(e).__name__, "|", str(e)[:60])
```

**追问一**：为什么 `__set_name__` 在 `type.__new__` 里同步调用，而不是延迟到首次访问？——因为它的设计目的就是"让描述符在类创建时知道自己的归属名与 owner"，从而提前缓存字段名、注册到 owner 的元数据里（ORM 列映射、Pydantic 字段收集都靠这个）。延迟到首次访问会让"字段清单"在类刚建好时还是空的，破坏框架的初始化时序；同步调用的代价就是类定义期异常会阻断 import，必须正确报错。

**追问二**：`dataclass(slots=True)` 为什么能绕开这个冲突，而手写 `__slots__` 不行？——因为 `dataclass(slots=True)` 是**先收集字段、再生成新类并把字段写进 `__slots__`**，它知道哪些名字已经被描述符/字段占用，生成时会避开；手写 `__slots__` 是你直接把名字塞进类字典，与类体里的同名描述符在 `type.__new__` 阶段硬碰硬。3.10+ 的 `slots=True` 正是把"避让规则"从用户搬到了装饰器里。

## 背诵要点
- 类创建顺序：type.__new__ 先建 slot member_descriptor，再对每个类变量调 `__set_name__`；同名 → `ValueError`，类创建失败。
- `__set_name__` 内抛的异常在 3.12 原样传播（不包 RuntimeError），stderr 另打印 `Error calling __set_name__ on ...` 诊断行。
- 避让：slot 名与描述符名不可同名；ORM 字段收集冲突用 `dataclass(slots=True)` 或元类预检。

## 复盘追问
- 给 ORM model 加 `__slots__` 后服务 import 即崩、堆栈只到类定义行，如何定位？（识别 ValueError conflicts / RuntimeError during __set_name__，打印类字典同名描述符，讨论 slots 优化与字段收集的命名冲突）
- 为什么不能简单把自定义描述符改成 non-data descriptor 来绕过同名冲突？（冲突发生在 type.__new__ 的 slots 与类变量同名检测，与 data/non-data 无关，讨论正确避让方式）
