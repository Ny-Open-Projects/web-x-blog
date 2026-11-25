---
title: "[Q5162] 延迟注解的框架兼容事故：局部作用域 NameError"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5162 · 延迟注解的框架兼容事故：局部作用域 NameError

难度：P7 ｜ 标签：PEP 563、PEP 649、注解求值、get_type_hints、事故复盘

**问**：`from __future__ import annotations` 把注解变成字符串后，为什么一个在函数里定义的类（局部作用域类）会让 `typing.get_type_hints` 抛 `NameError`，而模块级类却没事？3.14 的 PEP 649 延迟求值（lazy evaluation）声称"不再有字符串注解问题"，它真的能解决这个事故吗？作为一个注解消费者（框架作者），正确的兜底姿势是什么？

**答**：
结论：事故的根因是**注解的字符串化与命名空间缺失的错位**，而不是延迟求值本身。开启 PEP 563 后，`ref: Inner` 实际存的是字符串 `"Inner"`；`get_type_hints(C)` 默认只用 `C.__globals__` 加内置名字做 `eval`。当一个类的注解引用了**定义在函数内部的兄弟类**时，那个类不在模块全局里，而在已退出的函数局部——局部命名空间随函数返回被销毁，注解字符串里的 `Inner` 成了悬空引用，`eval` 必然 `NameError`。PEP 649 在 3.14 改成"注解对象惰性求值、用到才算"，但它计算时同样依赖声明处的作用域链：局部作用域类一旦离开声明帧，惰性计算的上下文也会失效，所以**这个事故在 3.14 依然可能发生**，只是失败时机从"读取注解"推迟到"首次求值"。

取舍：框架侧的防线不是"猜用户意图"，而是**显式收口**：① 消费者调用 `get_type_hints` 时永远传 `localns`，把需要的名字注入；② 对局部类/动态生成类，宁可在定义处就把注解解析成真实对象（关掉 future annotations 或提前求值），不要让字符串跨作用域漂移；③ 在入口对每个模型做一次"可解析性自检"，失败时给出明确报错而不是等到请求路径上炸。绝不能用裸 `eval(h, vars(sys.modules[cls.__module__]))` 硬来——它同样拿不到局部名，还可能执行任意代码。

实战：这类事故的高发场景是"工厂函数里定义 Pydantic 模型/Dataclass 并返回"——模块级注册看着没问题，真正 `model_rebuild()` 或字段解析时才 `NameError`。下面用最小复现抓住三步：字符串化 → 默认解析失败 → 注入 `localns` 后修复。3.14 PEP 649 的惰性形态用 text 块示意，不在本机执行。

```python
from __future__ import annotations          # PEP 563：注解全部字符串化
from typing import get_type_hints

def build_models():
    class Inner:                            # 局部类，随函数返回销毁
        pass
    class Outer:
        ref: Inner                          # 存的是字符串 "Inner"
    return Outer, Inner

Outer, Inner = build_models()
print("raw annotations:", Outer.__annotations__)   # {'ref': 'Inner'}

# 1) 默认解析：只用 globals，拿不到已销毁的局部 Inner -> NameError
try:
    get_type_hints(Outer)
except NameError as e:
    print("default resolve ->", type(e).__name__, ":", e)

# 2) 修复：显式注入 localns
print("with localns  :", get_type_hints(Outer, localns={"Inner": Inner}))

# 3) 模拟"注解消费者"的自检：先解析、失败即抛业务异常
def consume(cls, localns=None):
    try:
        return get_type_hints(cls, localns=localns or {})
    except NameError as e:
        raise ValueError(f"模型 {cls.__name__} 的注解无法解析: {e}") from e

for ns in ({}, {"Inner": Inner}):
    try:
        print("consume:", consume(Outer, ns))
    except ValueError as e:
        print("consume failed:", e)
```

```text
# PEP 649（3.14 默认）惰性注解的形态示意，本机 3.12 不执行：
class Outer:
    ref: Inner          # 3.14 存的是"求值器"，首次读 __annotations__ 时才算 Inner
                        # 若 Inner 是局部名且声明帧已销毁 -> 仍然 NameError（时机推迟而已）
```

**追问一**：为什么说"延迟求值的 PEP 649 与字符串注解的 PEP 563 不是一回事，但都救不了局部作用域"？——PEP 563 是把注解**永久字符串化**（`__annotations__` 里就是 str），PEP 649 是存**可调用求值器**（`__annotations__` 首次访问时惰性算出真实对象），差别在"何时算、是不是字符串"；但两者解析名字时都按声明处可见的命名空间进行，局部作用域类在声明帧退出后对二者都不可见——一个是"取字符串后 eval 失败"，一个是"惰性求值时 NameError"，病根相同。

**追问二**：框架如果不给 `localns`，还有什么更稳的办法让局部模型可解析？——最稳的是**定义处即固化**：在工厂函数内用 `typing.get_type_hints(Outer, localns=locals())` 立刻解析一次，把结果写回 `Outer.__annotations__`，让字符串变对象后再返回；这样下游消费者不再需要任何局部信息。代价是工厂函数必须自己是"注解求值点"，且要处理 `locals()` 在类体与函数体之间名字可见性的差异。

## 背诵要点
- 事故链：PEP 563 字符串注解 + 局部作用域类 → 局部命名空间随函数销毁 → `get_type_hints` 默认只用 globals → `NameError`。
- PEP 649 把失败时机从"读注解"推迟到"首次求值"，但局部作用域类离开声明帧后仍不可解析，救不了这个事故。
- 防线：消费者传 `localns`；工厂函数内在 `locals()` 可见时提前固化 `__annotations__`；入口做可解析性自检。

## 复盘追问
- 工厂函数里用 Pydantic 定义模型，单测正常、线上请求进来才 `NameError`，如何复盘并建立防回归？（还原局部命名空间销毁链路、定义处固化注解、入口自检，讨论测试要覆盖"返回后解析"而非"定义时解析"）
- 为什么用 `eval` + 模块 globals 兜底是危险写法？（拿不到局部名只是其一，执行任意注解字符串是注入面，讨论用 `get_type_hints` 受控 API 替代）
