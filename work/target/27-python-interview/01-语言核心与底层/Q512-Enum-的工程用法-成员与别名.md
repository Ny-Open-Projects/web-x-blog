---
title: [Q512] Enum 的工程用法:成员与别名
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q512 · Enum 的工程用法:成员与别名

> 难度:★★★☆ | 标签:Enum, 常量

**问**:为什么状态码该用 Enum 而不是模块级常量?Enum 的别名机制与 @unique 有什么关系?

**答**:Enum 给常量加上「类型、可迭代、比较安全、防拼错」四重收益:Status.OK 拼错在静态期报错,字符串 "OK" 拼错运行时才发现;数据驱动功能(根据成员属性计算,如行星重力)直接挂在成员上。别名机制:同名值自动成为第一个成员的别名(Color.RED is Color["red"] 类似场景),适合兼容旧名;不要别名就 @unique 强制唯一,重复值在定义期报错。注意 IntEnum 能与 int 互转(方便 JSON/DB),但也因此失去「防混用」的部分收益,按需选择。

```python
# file: code/01_语言核心与底层/q512_enum.py
from enum import Enum, auto, unique

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

@unique
class Status(Enum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500

class Planet(Enum):
    MERCURY = (3.3e23, 2.4e6)
    EARTH = (6.0e24, 6.4e6)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    @property
    def gravity(self):
        return 6.674e-11 * self.mass / self.radius ** 2

if __name__ == "__main__":
    print(Color.RED.name, Color.RED.value)
    print(Status(404).name)
    print("members:", [m.name for m in Color])
    print("earth heavier pull:", Planet.EARTH.gravity > Planet.MERCURY.gravity)
    try:
        Status.OK.value = 201
    except AttributeError as e:
        print("immutable:", e)
```

**追问**:1) Enum 成员能比较大小吗?——默认只能判等,继承 IntEnum/IntFlag 后获得整数比较;纯 Enum 要排序需要实现 __orderings__ 或自定义 mixin,通常说明它在建模「无序集合」,排序是设计信号。2) 别名机制与坑?——同值成员自动成为别名(Color.red is Color.crimson),_ignore_ 可排除;不想要别名用 @unique 或 unique 校验抛错,否则「以为多了个成员其实还是同一个」。3) 底层机制?——EnumType(3.11 前叫 EnumMeta)在类创建时拦截成员构造,维护 _member_map_ 与 _value2member_map_ 双表;__members__ 含别名;查找按名字或值都走这张表。4) 生产陷阱?——DB 存 name 与 value 口径不一致,迁移改 value 后旧数据失配;IntEnum 与任意 int 相等破坏类型墙;对外 API 序列化应统一 str 值。
