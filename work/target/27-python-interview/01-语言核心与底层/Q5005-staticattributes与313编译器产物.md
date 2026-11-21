---
title: [Q5005] __static_attributes__ 与 3.13 编译器产物对代码分析工具的意义
date: 2026-11-18
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5005 · `__static_attributes__` 与 3.13 编译器产物对代码分析工具的意义

> 难度:★★★ | 标签:3.13, 代码分析, 编译器

**问**：3.13 给类对象新增的 `__static_attributes__` 和 `__firstlineno__` 是干什么的？编译器为什么要「多嘴」记录这些信息？静态分析工具和运行时框架各能拿它做什么？

**答**：结论：3.13 编译器在编译 `class` 体时把两类信息「顺手」记录到类命名空间：`__static_attributes__` 是类体内**静态可见的属性赋值目标名集合**（如 `self.name = ...` 里的 `name`），`__firstlineno__` 是类定义起始行号（替代旧的 `__firstlineno__` 仅为 repr 用途的行号推导）。动机：1) `__slots__`/`__match_args__` 类的自动推断——IDE、类型检查器与运行时框架可以不跑 AST 解析就拿到「这个类都往 self 上赋过什么」，推断 slot 字段、生成 dataclass 字段提示、做漏初始化检查；2) 调试与文档工具用 `__firstlineno__` 精确定位类体起始（继承链里多基类源码定位不再靠解析 `__module__` 文件再正则找类名）。边界要讲清：`__static_attributes__` 是**编译期静态可见**的集合——动态 `setattr(self, k, v)`、`self.__dict__.update` 都不在内，所以它是「提示」不是「保证」；且它出现在类体命名空间，子类不会自动合并父类的集合（要自己 union）。实战：给内部框架做「必填字段漏初始化报警」时，3.13 前要 parse 源码或靠 `__init__` 运行时埋点，3.13 直接读 `cls.__static_attributes__` 与 `__init__` 结束时的实例属性做差集即可。

```python
# 基线:Python 3.13+。3.12 及以下降级:退回 ast.parse 源码提取属性赋值目标。
import sys

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self._log = []

if sys.version_info >= (3, 13):
    print(User.__static_attributes__)   # {'name', 'email', '_log'}
    print(User.__firstlineno__)         # 类定义起始行号(本文件内为实际行)
    # 实战:实例化后比对「静态声明 vs 实际初始化」找漏赋值
    u = User("w", "w@x.com")
    missing = User.__static_attributes__ - set(vars(u))
    print("missing:", missing)          # 正常场景为空;漏写 self._log 时会报出
else:
    print("3.12-: 无 __static_attributes__,需要 ast.parse 源码做同样的事")
```

**追问**：
1) 它和 `__slots__` 什么关系？能不能自动生成 slots？——`__static_attributes__` 提供了自动推断 slot 的物料，但语言本身不自动生成：动态 setattr、property 交互、跨方法赋值顺序等边界让「自动 slots」有正确性风险；IDE 与第三方工具（如 dataclass slots 推断）用它做提示。
2) 为什么是「类体静态可见」而不是「运行时实际赋值」？——编译器只能在编译时看到 `self.x = ...` 的 AST 事实；把运行时行为记进来需要在每个赋值点插桩，违背「零开销元信息」的设计。两者用途互补：静态集合给工具，运行时行为靠 hook（`__setattr__`）。
3) `__firstlineno__` 对回溯/文档有什么实际改善？——3.12 及以前类的行号信息不精确（装饰器、多行基类列表会让定位偏移）；3.13 起文档生成器、调试器「跳到定义」直接取整数值定位类体，跨继承多文件工程里定位准确性是实打实的提升。
