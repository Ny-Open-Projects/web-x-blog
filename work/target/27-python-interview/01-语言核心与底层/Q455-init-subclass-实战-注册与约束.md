---
title: [Q455] __init_subclass__ 实战:注册与约束
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q455 · __init_subclass__ 实战:注册与约束

> 难度:★★★★ | 标签:元编程, __init_subclass__

**问**:不用元类,如何在子类定义的那一刻做校验和注册?关键字参数怎么传进 __init_subclass__?

**答**:基类定义 `__init_subclass__(cls, **kwargs)`,每个子类被创建时自动调用一次,类体里的关键字参数(`class Csv(Plugin, name="csv")`)原样传入,其余参数先交给 super().__init_subclass__ 消化。典型用途:强制子类实现某方法(检查 cls.__dict__ 而不是 cls,避免继承误判)、把子类写进注册表、按命名规范校验。它覆盖了元类 90% 的日常需求,且可被继承叠加,没有 metaclass 冲突问题。

```python
# file: code/01_语言核心与底层/q455_init_subclass_registry.py
class Plugin:
    """基类:自动注册子类并强制实现 run"""
    registry = {}

    def __init_subclass__(cls, name=None, strict=True, **kwargs):
        super().__init_subclass__(**kwargs)
        if strict and "run" not in cls.__dict__:
            raise TypeError(f"{cls.__name__} must implement run")
        key = name or cls.__name__.lower()
        if key in Plugin.registry:
            raise ValueError(f"plugin {key} already registered")
        Plugin.registry[key] = cls

class CsvPlugin(Plugin, name="csv"):
    def run(self, src):
        return f"csv from {src}"

class JsonPlugin(Plugin):
    def run(self, src):
        return f"json from {src}"

if __name__ == "__main__":
    try:
        class Broken(Plugin):             # strict 且没实现 run:定义即报错
            pass
    except TypeError as e:
        print("rejected at class creation:", e)

    print(sorted(Plugin.registry))
    print(Plugin.registry["csv"]().run("data.csv"))
```

**追问**:1) 检查 "run" in cls.__dict__ 而不是 "run" in dir(cls) 的原因?——dir 会包含继承来的方法,子类什么都不写也能通过检查;__dict__ 只看本类,才能强制「每个子类自己实现」。2) 与元类方案相比各自强在哪?——__init_subclass__ 无元类冲突、可继承叠加,覆盖注册/校验 90% 需求;元类能控制类创建全程(__prepare__ 命名空间、拦截 __call__ 做单例),需要「控制类本身行为」才上元类。3) 关键字参数如何传进来?——类体括号参数由 metaclass 收集后透传给 __init_subclass__(3.6+ 默认支持);super().__init_subclass__() 必须显式链式调用,否则基类钩子被跳过。4) 生产陷阱?——注册表写在基类可变属性上,子类同名赋值把它变成类属性覆盖,要用基类名显式访问;钩子在 import 期抛错,堆栈不直观,报错信息要带类名。
