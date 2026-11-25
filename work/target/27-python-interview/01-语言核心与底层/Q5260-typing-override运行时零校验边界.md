---
title: "[Q5260] typing.override 的运行时零校验：它只写一个标记，谁在真正守护契约"
date: 2026-11-25
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5260 · typing.override 的运行时零校验：它只写一个标记，谁在真正守护契约

难度：P6 ｜ 标签：typing.override、PEP 698、运行时校验、mypy、pyright、LSP、final

**问**：给一个基类的 `handle()` 加 `@override` 时手滑写成了 `hnadle()`，单测全绿、线上也"正常"（因为调用方调的是父类方法），直到某次重构把父类方法删了才发现子类那个函数从来没被调用过。`@override` 到底做了什么运行时检查？为什么它不阻止"覆盖一个不存在的方法"？和 `@final`、`abc.abstractmethod` 分别管什么？如果团队不跑 mypy/pyright，这个装饰器还有价值吗？

**答**：

- **结论**：`@override`（3.12 进标准库，PEP 698）在运行时**只做一件事**：把被装饰对象的 `__override__` 属性设为 `True`，然后原样返回该对象。它不查 MRO、不检查父类是否有同名方法、不改变描述符行为、不影响调用、不产生警告——`class Child(Base): @override def hnadle(self)` 里的拼写错误在运行时完全合法。它还必须**裸用**：3.12 的 `@override()`（带括号）会报 TypeError，因为实现签名是 `override(method)`。真正拦截"覆盖不存在的方法"的是静态检查器（mypy/pyright），它们看到 `__override__` 标记后会沿 MRO 找同名成员，找不到就报错。所以它的定位是"给类型检查器的意图声明"，不是运行时契约。

- **取舍**：a) 有类型检查的团队：全量加 `@override` 的收益很高——重命名父类方法时，所有子类会立刻红，而不是静默退化成"新方法 + 旧方法仍被调用"；b) 没有类型检查的团队：`@override` 只是给函数加了个属性，价值接近于零，反而制造"我加了保护"的错觉；这时应该用运行时自检（见实战）或直接依赖测试覆盖；c) 与 `@final` 的区别：`override` 是"我声明在覆盖"，`final` 是"我声明不许被覆盖"；两者运行时都只是标记（`__final__`/`__override__`），真正的强制在类型检查器和代码评审；d) 与 `abc.abstractmethod` 的区别：抽象方法是**运行时**机制（未实现时实例化报 TypeError），`override` 是**静态**机制，三者正交，可以叠用。

- **实战**：事故形态是"父类方法改名，子类覆盖变成死代码"——`Base.handle` 重命名为 `Base.process`，子类 `@override def handle` 没有报错（因为没跑类型检查），调用方走 `Base.process`，子类的 `handle` 永远不被调用，监控上看是"某个业务分支再也不执行"。修复：CI 加 mypy `--strict`（或 pyright），把 `@override` 纳入规范；同时对没有类型检查的历史模块加一条运行时冒烟断言：遍历类里带 `__override__` 的函数，检查 `any(hasattr(base, name) for base in cls.__mro__[1:])`，不满足就在测试期失败。注意这条自检对"基类通过 `__getattr__` 动态提供方法"会误报，需按模块白名单关掉。

```python
# typing.override: 运行时只写 __override__, 不查 MRO、不阻止拼写错误
from typing import final, override

class Base:
    def handle(self):
        return "base"

class Child(Base):
    @override
    def handle(self):
        return "child"

    @override
    def hnadle(self):          # 拼写错误: 运行时完全合法
        return "typo"

print("→ 标记:", Child.handle.__override__, Child.hnadle.__override__)
assert Child.handle.__override__ is True
assert Child.hnadle.__override__ is True
assert "__override__" in vars(Child.hnadle)      # 属性在函数对象上
assert Child().hnadle() == "typo"                # 运行时没有任何校验
assert Child().handle() == "child"

# 继承来的函数对象仍带标记(标记跟着函数走, 不是类)
class Grand(Child):
    pass
assert Grand.handle.__override__ is True

# @override() 带括号在 3.12 不支持
call_form = ""
try:
    @override()
    def free_func():
        return 1
except TypeError as e:
    call_form = str(e)
    print("→ @override() 带括号:", e)
assert "missing" in call_form

# override 也可以用在普通函数上: 运行时不限制上下文
@override
def detached():
    return 2
assert detached.__override__ is True

# 与 @final 叠加: final 标在基类方法上, override 标在子类方法上
class Sealed:
    @final
    def run(self):
        return "sealed"

class Breaker(Sealed):
    @override
    def run(self):
        return "broken"

print("→ 基类 final 标记:", Sealed.run.__final__, "| 子类 override 标记:", Breaker.run.__override__)
assert Sealed.run.__final__ is True
assert Breaker.run.__override__ is True
assert not hasattr(Breaker.run, "__final__")      # 标记跟着函数对象, 不随覆盖继承
assert Breaker().run() == "broken"                # 运行时也不阻止覆盖 final

# 可以自己写的运行时自检: 覆盖目标必须存在于某个基类
def check_overrides(cls):
    missing = []
    for name, obj in vars(cls).items():
        if callable(obj) and getattr(obj, "__override__", False):
            if not any(hasattr(base, name) for base in cls.__mro__[1:]):
                missing.append(name)
    return missing

print("→ 运行时自检发现的问题方法:", check_overrides(Child))
assert check_overrides(Child) == ["hnadle"]
assert check_overrides(Breaker) == []            # Sealed.run 存在, 只是违反 final
```

**追问一**：为什么 PEP 698 不在运行时做 MRO 校验？—— 三个原因：①**成本**：要在类创建时遍历所有基类、解析描述符/`__getattr__`/元类动态注入，import 期开销不可控，而绝大多数类根本不需要这层检查；②**语义不确定**：基类可能来自 C 扩展、可能通过 `__getattr__` 动态提供属性、可能是未解析的 `Protocol`，运行时"找不到"不等于"契约不存在"，误报会逼用户关掉检查；③**职责分离**：Python 的类型系统本来就是"静态检查器 + 运行时协议"两层，`override` 属于前者，让它保持零成本、零行为改变，才能被无痛加进任何代码库。代价就是本卡开头的事故：没有静态检查时它不提供任何保护。

**追问二**：`@override`、`@final`、`abc.abstractmethod` 三者的执行时机与强制力有什么不同？—— `abc.abstractmethod` 是**运行时**：`ABCMeta` 在实例化时检查 `__abstractmethods__`，未实现就抛 TypeError；`@final` 是**静态 + 标记**：运行时只设 `__final__ = True`，不阻止子类覆盖，mypy/pyright 报错，部分框架（如 dataclass）会读这个标记；`@override` 是**纯静态**：运行时只设 `__override__ = True`，连"父类有没有"都不看。强度排序（运行时）：abstractmethod > final ≈ override（后两者为零）。所以"防止子类改坏"要靠 abstractmethod 或组合（模板方法把可变步骤做成抽象方法），"防止改错名"要靠 override + 类型检查，"禁止覆盖"要靠 final + 评审，三者不能互相替代。

## 背诵要点

- `@override` 运行时只设 `__override__ = True` 并返回原对象：不查 MRO、不校验父类同名、不影响调用；3.12 必须裸用，`@override()` 报 TypeError。
- 真正的守护者是 mypy/pyright：沿 MRO 找同名成员，找不到报错；没有类型检查时它只是标记，价值接近零。
- 三者分工：`abstractmethod` 运行时强制实现、`final` 静态禁止覆盖、`override` 静态声明覆盖；可叠加，互不替代。

## 复盘追问

- 为什么拼错方法名的 `@override` 在运行时不会报错？（PEP 698 明确零运行时校验，只写属性；只有静态检查器读这个标记）
- 没有 mypy 的团队怎么用 override 获得保护？（测试期遍历 `vars(cls)` 检查 `__override__` 方法在 MRO 中存在，白名单处理动态基类）
