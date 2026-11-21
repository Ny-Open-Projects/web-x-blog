---
title: [Q1811] property setter 的副作用设计:归一化与派生字段联动
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1811 · property setter 的副作用设计:归一化与派生字段联动

> 难度:★★★☆☆ | 标签:property, 不变量, API 设计

**问**:setter 里做校验之外,什么时候该做「副作用」?边界在哪?

**答**:setter 的三个正用:① 校验与归一化——非法值抛 ValueError,合法值做类型归一 float(value),保证对象内不变量;② 派生字段联动——width/height 变化时同步刷新 area,把「多字段一致性」收口在唯一入口,调用方不可能改一半忘一半;③ 触发轻量通知——脏标记、缓存失效(Q452 的失效语义)。边界同样清楚:setter 里不做 IO、不加锁等待、不抛非值类异常,副作用要幂等可重入;纯派生量建议做成只读 @property 实时计算而不是存字段,只有读多写多、计算贵时才落地存储。Q027 讲 property 原理与 descriptor 替代,本题讲行为设计:属性赋值是「看起来像字段的行为」,副作用就藏在这一次赋值里。

```python
# file: code/01_语言核心与底层/q1811_property_side_effect.py
"""property setter 的副作用设计:归一化与派生字段联动。"""


class Rectangle:
    def __init__(self, width, height):
        self._w = self._h = 0.0
        self.area = 0.0            # 派生字段,由 setter 联动维护
        self.width = width         # 走 setter 完成校验与归一化
        self.height = height

    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width 必须为正数")
        self._w = float(value)
        self._sync_area()

    @property
    def height(self):
        return self._h

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height 必须为正数")
        self._h = float(value)
        self._sync_area()

    def _sync_area(self):
        self.area = self._w * self._h


if __name__ == "__main__":
    r = Rectangle(3, 4)
    print("初值:", r.width, r.height, "面积:", r.area)
    r.width = 10                   # setter 联动刷新派生字段
    print("改宽后:", r.width, "面积:", r.area)
    try:
        r.height = -1
    except ValueError as e:
        print("非法值被 setter 拦下:", e)
    print("面积未被污染:", r.area)
```

**追问**:1) __init__ 里走 setter,构造到一半抛异常会留下半成品对象吗?——会,这是 setter 校验的代价;彻底解法是模块级工厂函数先验参再构造,或 dataclass __post_init__ 统一校验。2) setter 副作用的设计边界?——归一化(strip/NFC)与派生字段联动是正当用途;重逻辑(查库、网络)不该进 setter;构造期抛异常的对象不逃逸是前提——工厂函数保证「验证过了才 new」。3) property 联动的风险?——setter 触发其他 property 又反向触发自己 → 无限递归;派生字段更新要防环;只读派生用 @property 计算而不是缓存变量。4) 生产陷阱?——半成品对象被引用日志/调试器看到;setter 里做 IO;校验逻辑分散在构造与 setter 两处口径漂移。
