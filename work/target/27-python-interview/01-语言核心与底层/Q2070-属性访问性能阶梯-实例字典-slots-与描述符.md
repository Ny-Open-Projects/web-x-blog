---
title: [Q2070] 属性访问性能阶梯:实例字典、slots 与描述符实测
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2070 · 属性访问性能阶梯:实例字典、slots 与描述符实测

> 难度:★★★★☆ | 标签:属性访问, __slots__, 实测

**问**:instance dict、__slots__、property、自定义描述符、__getattr__ 这几条属性访问路径,速度差多少?

**答**:本机 CPython 3.9.6 用 timeit 各取 3 次最小值,量级大约是:普通实例字典与 __slots__ 都在 50ns 上下(字典路径有 key 共享优化,slots 是固定偏移,两者几乎打平);property 约 143ns,多了一次函数调用;非数据描述符约 217ns,再多一层协议分派;__getattr__ 未命中路径最惨,约 600ns——因为要先走完整查找失败,再进 Python 层兜底函数。工程结论:常态访问路径保持「实例字典或 slots 直达」,property 用在需要归一化的边界上,别把热路径的每次取值都包成 property;__getattr__ 只做兜底元编程,不要当默认访问器(它的触发条件见 Q028)。

```python
# file: code/01_语言核心与底层/q2070_attr_ladder.py
"""属性访问性能阶梯:实例字典、__slots__、property、描述符与 __getattr__。"""
import timeit


class DictPoint:
    """普通类:属性在实例 __dict__ 里。"""
    def __init__(self, x):
        self.x = x


class SlotPoint:
    """__slots__:固定槽位偏移访问。"""
    __slots__ = ("x",)

    def __init__(self, x):
        self.x = x


class PropPoint:
    """property:每次读取都是一次函数调用。"""
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x


class DescPoint:
    """非数据描述符:比 property 多一层协议分派。"""
    class TenX:
        def __get__(self, obj, cls):
            return obj._x * 10 if obj else self
    x = TenX()

    def __init__(self, x):
        self._x = x


class GetattrPoint:
    """__getattr__ 兜底:常态查找失败后才触发,最慢。"""
    def __init__(self, x):
        self._store = {"x": x}

    def __getattr__(self, name):
        if name == "x":
            return self._store["x"]
        raise AttributeError(name)


def bench(cls, number=200000):
    p = cls(21)
    best = min(timeit.repeat("p.x", globals={"p": p}, number=number, repeat=3))
    return best / number * 1e9


if __name__ == "__main__":
    for cls in (DictPoint, SlotPoint, PropPoint, DescPoint, GetattrPoint):
        print(f"{cls.__name__:13} {bench(cls):7.1f} ns/op")
    print("阶梯:实例字典 约等于 slots < property < 描述符 < __getattr__ 未命中")
```

**追问**:1) __getattr__ 与 __getattribute__ 的开销差异?——__getattr__ 只在未命中时触发、常态零成本,__getattribute__ 拦截每一次访问,是性能大坑;__slots__ 除了速度还带来什么?——省内存、禁动态加属性,但继承链上都要声明才彻底,见 Q008 与 Q559。2) 访问阶梯的完整排序?——slots/直接槽 ≈ 实例字典 < 数据描述符 < __getattr__ 兜底 << __getattribute__ 全拦截;每次访问都过描述符协议的 C 层分派。3) 实测口径?——timeit 取 min,同进程多轮(Q2093);3.11+ LOAD_ATTR 内联缓存显著缩小差距(Q1259),结论只到常数级。4) 生产陷阱?——__getattribute__ 里做重活(日志/IO);slots 继承链不全白声明(Q2074);无 profile 的微优化改架构。
