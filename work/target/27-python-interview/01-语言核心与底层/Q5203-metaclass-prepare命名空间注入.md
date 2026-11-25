---
title: "[Q5203] metaclass __prepare__：在类体执行前接管命名空间"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5203 · metaclass __prepare__：在类体执行前接管命名空间

难度：P7 ｜ 标签：metaclass、`__prepare__`、命名空间、声明式 DSL、字段顺序

**问**：想在类定义时收集字段的**声明顺序**，普通 `__new__` 拿到的 namespace 已经是 dict，Python 3.7+ 虽然保序，但重复定义、注解、注入默认值都很难拦。`__prepare__` 到底在什么时机被调用？返回一个自定义 mapping 能做什么、不能做什么？为什么很多框架（Enum、声明式 ORM）宁可写它而不是在 `__new__` 里事后补？

**答**：
结论：类语句的执行顺序是：解析 bases → 调 `metaclass.__prepare__(name, bases, **kw)` 得到命名空间 → 执行类体，所有赋值/`def` 都以 `STORE_NAME` 写进这个 mapping → 把 mapping 传给 `metaclass.__new__` 造类 → `__init__`。所以 `__prepare__` 是**唯一能在类体执行前**布控的钩子：可以在 mapping 里预置名字（类体里能直接读到）、拦截重复键、记录写入顺序、把注解与默认值配对。

取舍：a) 只要"事后处理"，用 `__new__` 就够，简单且不引入自定义 mapping；b) 要"类体里就能用"的注入（比如 DSL 的 `Column` 自动登记、Enum 的成员重复检测），必须 `__prepare__`；c) 返回对象只要求是 mapping（实现 `__setitem__`/`__getitem__`/`keys` 等），不必是 dict，但 `type.__new__` 最终需要真实 dict，通常 `dict(ns)` 拷一份再传；d) 自定义 mapping 里的元数据（顺序、重复记录）在 `__new__` 里读出来后要显式挂到类上，否则类造完就丢了；e) 别在 `__prepare__` 里做重 IO 或依赖类体结果，它跑在类体之前。

实战：事故形态是"配置 DSL 用普通 dict 收集字段，同名字段被后写的静默覆盖，直到线上发现某张表的 `timeout` 列不见了；改成 `__prepare__` 返回记录写入轨迹的 mapping，重复定义在类创建期直接报错"。下面演示命名空间注入、顺序记录与重复检测。

```python
class Namespace(dict):
    def __init__(self):
        super().__init__()
        self.order = []
        self.duplicates = []

    def __setitem__(self, key, value):
        if key in self and not key.startswith("__"):
            self.duplicates.append(key)
        super().__setitem__(key, value)
        if not key.startswith("__"):
            self.order.append(key)


class ModelMeta(type):
    @classmethod
    def __prepare__(mcls, name, bases, **kwargs):
        print(f"[prepare] 为 {name} 创建命名空间，bases={[b.__name__ for b in bases]}")
        ns = Namespace()
        ns["__dsl_version__"] = 1      # 类体里可直接读到
        return ns

    def __new__(mcls, name, bases, ns, **kwargs):
        cls = super().__new__(mcls, name, bases, dict(ns))
        cls.fields = [k for k, v in ns.items()
                      if not k.startswith("_") and not callable(v)]
        cls.declared_order = list(ns.order)
        cls.duplicates = list(ns.duplicates)
        return cls


class User(metaclass=ModelMeta):
    print("[body] 注入的名字可见:", __dsl_version__)
    id = 1
    name = "alice"
    timeout = 30
    timeout = 60                  # 重复定义：被记录

    def greet(self):
        return self.name


print("[1] 字段（按声明顺序）:", User.fields)
print("[2] 全部写入轨迹（含方法）:", User.declared_order)
print("[3] 重复定义:", User.duplicates)
print("[4] 实例正常:", User().greet())
```

**追问一**：`__prepare__` 能拿到父类的命名空间吗？—— 不能。它只收到 `name`、`bases` 和类关键字参数，父类已经造好了，你要继承字段得自己沿 MRO 合并。这也是声明式框架要在 `__new__` 里做"父类字段 + 本类字段"合并的原因；`__prepare__` 只负责本层类体的收集。

**追问二**：为什么 `Enum` 要用自定义 mapping？—— `enum.EnumMeta.__prepare__` 返回 `_EnumDict`，在类体执行时就能识别"某个名字是否已经定义为成员"，从而在 `class Color: RED = 1; RED = 2` 这种重复定义上立刻报错，并且能区分成员、方法、`_ignore_`、`__dunder__`。如果等到 `__new__` 再看 dict，重复键早被覆盖，信息已经丢了——这就是"必须在写入时拦截"的典型场景。

## 背诵要点
- 时序：`__prepare__` → 执行类体（写入 mapping）→ `__new__` → `__init__`。
- `__prepare__` 返回任意 mapping；可预置名字、记录顺序、拦截重复，但最终要转成 dict 造类。
- 父类命名空间不可见；跨层字段合并放在 `__new__` 沿 MRO 做。

## 复盘追问
- 声明式 DSL 想在类体里直接用 `Column()` 自动登记，钩子放哪？（`__prepare__`）
- 为什么重复字段只能在 `__prepare__` 阶段发现？（dict 覆盖后信息丢失）
