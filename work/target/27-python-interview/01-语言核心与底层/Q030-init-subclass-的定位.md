---
title: [Q030] __init_subclass__ 的定位
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q030 · __init_subclass__ 的定位

> 难度:★★☆ | 标签:类, 元编程

**问**:很多「以前必须用 metaclass」的需求,现在可以用什么替代?

**答**:基类定义 `__init_subclass__(cls, **kwargs)`,每个子类创建时自动调用,kwargs 接收类定义里的关键字参数(如 `class A(Base, key="v")`)。它比 metaclass 轻量:无继承冲突、可读性好,能完成子类注册、自动收集、参数校验等大部分场景。注册表、插件发现优先用它。

```python
# file: code/01_语言核心与底层/q030_init_subclass.py
class Plugin:
    plugins = []

    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.slug = name or cls.__name__.lower()
        Plugin.plugins.append(cls)

class EmailPlugin(Plugin, name="email"):
    def run(self):
        return "sending email"

class SmsPlugin(Plugin):
    def run(self):
        return "sending sms"

if __name__ == "__main__":
    for p in Plugin.plugins:
        print(p.slug, "->", p().run())
    print(EmailPlugin.slug)
```

**追问**:1) 类定义里的关键字参数如果基类没处理会怎样?——Python 会报 `TypeError: ... unexpected keyword argument`,这是显式的拼写保护,比 metaclass 静默吞掉更安全。2) __init_subclass__ 替代不了元类的什么?——它收不到正在创建的类的 namespace,无法增删方法或改写字段集合;需要「改写类体」仍要元类或类装饰器,纯注册/校验场景它足够。3) 它常和什么钩子配合?——`__set_name__`:描述符被赋给类属性时拿到属主类与属性名,两者组合可实现无元类的声明式字段系统(自动命名、注册)。
