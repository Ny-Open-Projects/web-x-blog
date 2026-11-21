---
title: [Q1806] classmethod 多态构造器:from_xxx 与 cls 传递
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1806 · classmethod 多态构造器:from_xxx 与 cls 传递

> 难度:★★★☆☆ | 标签:classmethod, 构造器, 多态

**问**:为什么 from_xxx 系列构造器要用 classmethod 而不是模块级工厂函数?子类继承后行为如何?

**答**:`@classmethod def from_fahrenheit(cls, f): return cls(...)` 的关键是返回 cls(...) 而不是硬编码 Temperature:Kelvin.from_fahrenheit(100) 时 cls 是 Kelvin,自动得到子类实例,多态构造免费获得——这是 Q034 用 __new__ 控制实例化之外的第二条正路。工程约定:① from_xxx 命名成对出现(from_json/from_fahrenheit/from_row),__init__ 保持唯一主构造;② 继承体系里子类若改了 __init__ 签名,要么同步覆写 from_xxx,要么保持 cls(**kwargs) 风格让参数表稳定;③ 比「硬编码类名的工厂函数」可测试得多——测试子类即可覆盖整条构造链,而且 classmethod 能被覆写后经由 super() 组合。Q512 的 Enum 成员访问、Q455 的注册器都建立在「cls 跟随实际类」这个语义上。

```python
# file: code/01_语言核心与底层/q1806_cls_poly_ctor.py
"""classmethod 多态构造器:from_xxx 与 cls 的多态传递。"""
import json


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)      # cls 是实际调用的类,不是硬编码

    @classmethod
    def from_json(cls, payload):
        data = json.loads(payload)
        return cls(data["celsius"])

    def __repr__(self):
        return "{}({:.1f}C)".format(type(self).__name__, self.celsius)


class Kelvin(Temperature):
    def __init__(self, celsius):
        super().__init__(celsius)
        self.kelvin = celsius + 273.15


if __name__ == "__main__":
    print(Temperature.from_fahrenheit(100))
    print(Kelvin.from_fahrenheit(100))    # 子类上调用,cls 是 Kelvin:多态构造
    print(Kelvin.from_json('{"celsius": 25}'))
```

**追问**:1) classmethod 构造器与 Q442 的注册器怎么配合?——注册表把配置名映射到 cls,基类 from_config(cls, cfg) 负责按 cls 解析并实例化,两层各司其职。2) cls 传递为什么是多态关键?——from_xxx 里用 cls(...)(而不是硬编码类名)实例化,子类调用得到子类实例;这是替代构造器与继承能共存的原因。3) 构造器链的组织?——from_config 可委托其他 from_xxx;classmethod 可被子类重写定制解析逻辑;返回值一律 cls 实例。4) 生产陷阱?——构造器里写死 Base(...) 破坏多态;classmethod 与 property/staticmethod 混用顺序错;构造链共享模块级状态导致并发问题。
