---
title: [Q2887] __init_subclass__ 的插件自动注册:声明即注册
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2887 · __init_subclass__ 的插件自动注册:声明即注册

> 难度:★★★★☆ | 标签:__init_subclass__, 插件注册, 元编程

**问**:实现一个插件系统,要求子类定义出来就自动进注册表、重名立刻报错、缺方法立刻报错,用标准库怎么做到?

**答**:`__init_subclass__` 是比 metaclass 轻得多的钩子:基类定义一次,每个子类**在 class 语句执行的那一刻**被回调,拿到类对象与 class 语句传来的关键字(name=、priority=)。注册逻辑三步:键名取显式 name 或类名小写;重名抛 ValueError;按 required 元组检查必需方法,缺失抛 TypeError。对比装饰器注册器(Q442),它的优势是**注册无法被忘记**——写对了继承就一定注册,import 即生效,漏写装饰器这类静默事故在结构上不可能发生,而且错误在定义期暴露,比运行期首次调用才发现早得多。注意注册表是类属性 dict,测试之间要清空或重载模块做隔离,否则前一个测试注册的插件会漏到后一个测试里。

```python
# file: code/01_语言核心与底层/q2887_plugin_registry.py
"""__init_subclass__ 的插件自动注册:声明即注册,重名即报错。"""


class PluginBase:
    registry = {}

    def __init_subclass__(cls, name=None, priority=100, **kwargs):
        super().__init_subclass__(**kwargs)
        key = name or cls.__name__.lower()
        if key in PluginBase.registry:
            occupied = PluginBase.registry[key].__name__
            raise ValueError(f"插件名重复:{key} 已被 {occupied} 占用")
        required = getattr(cls, "required", ())
        missing = [m for m in required if not callable(getattr(cls, m, None))]
        if missing:
            raise TypeError(f"插件 {cls.__name__} 缺少必需方法:{missing}")
        cls.priority = priority
        PluginBase.registry[key] = cls

    @classmethod
    def sorted_plugins(cls):
        return sorted(cls.registry.items(), key=lambda kv: kv[1].priority)


class Cleaner(PluginBase, name="clean", priority=10):
    required = ("run",)

    def run(self):
        return "cleaning"


class Report(PluginBase, name="report", priority=50):
    required = ("run",)

    def run(self):
        return "reporting"


if __name__ == "__main__":
    for key, cls in PluginBase.sorted_plugins():
        print(f"插件 {key:<7} priority={cls.priority:<4} run -> {cls().run()}")

    try:
        class Dup(PluginBase, name="clean"):
            def run(self):
                return "dup"
    except ValueError as e:
        print("重名拦截:", e)

    try:
        class HalfDone(PluginBase, name="half"):
            required = ("run",)
    except TypeError as e:
        print("缺方法拦截:", e)
```

**追问**:1) 和 ABC 的 abstractmethod 有什么分工?——abstractmethod 拦的是「实例化时缺方法」,运行到实例化才报;__init_subclass__ 拦的是「定义时缺方法」,还能顺带做注册、改名、优先级这类 ABC 管不了的事,两者可以叠加使用。2) 声明即注册的完整链?——子类定义时 __init_subclass__ 校验 + 注册(Q455);cls.__dict__ 检查防止继承误判;kwargs 携带声明式配置;与 __set_name__ 管字段级互补(Q1834)。3) 与元类的取舍?——90% 场景 __init_subclass__ 足够且无元类冲突;需要控制类创建全程(__prepare__/__call__)才上元类。4) 生产陷阱?——钩子抛错让 import 失败(报错要带类名);注册表被子类覆盖(Q455);校验用 dir(cls) 误放行。
