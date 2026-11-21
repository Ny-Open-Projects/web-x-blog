---
title: [Q1809] 自定义 ABC:__subclasshook__ 结构判定与 register 承诺注册
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1809 · 自定义 ABC:__subclasshook__ 结构判定与 register 承诺注册

> 难度:★★★★☆ | 标签:ABC, 虚拟子类, 协议

**问**:Q477 讲了 collections.abc 的虚拟子类,自己写 ABC 时,__subclasshook__ 与 register 该怎么分工?

**答**:两条通道解决两类问题:① __subclasshook__ 做**结构判定**——classmethod 里检查 other 是否有 export 方法,有就拍板 True,拿不准返回 NotImplemented 把判定交还给注册表与常规检查;第三方类一个字不用改就通过,是「鸭子类型形式化」。② register 做**承诺注册**——LegacyAdapter 的方法名不匹配 hook,但团队承诺它兼容,register 一句声明 issubclass/isinstance 为 True,不校验任何方法、不继承实现,是纯粹的信任标记。注意 hook 拍板的 True/False 优先于注册表,只有 NotImplemented 才会继续查 _abc_registry——这是两通道的优先级契约。抽象方法仍由 @abstractmethod 守门:常规子类不实现就不能实例化,虚拟子类不受限。

```python
# file: code/01_语言核心与底层/q1809_own_abc_hook.py
"""自定义 ABC:__subclasshook__ 结构判定与 register 虚拟子类。"""
from abc import ABC, abstractmethod


class Exporter(ABC):
    @abstractmethod
    def export(self, data):
        ...

    @classmethod
    def __subclasshook__(cls, other):
        if cls is Exporter and hasattr(other, "export"):
            return True                        # 结构判定认得,直接拍板
        return NotImplemented                  # 拿不准:交还注册表与常规检查


class CsvExporter(Exporter):
    def export(self, data):
        return ",".join(map(str, data))


class ThirdParty:
    """不能修改源码的第三方类,但恰好有 export。"""

    def export(self, data):
        return str(data)


class LegacyAdapter:
    """方法名不匹配 hook;团队用 register 做承诺性注册。"""

    def dump(self, data):
        return str(data)


Exporter.register(LegacyAdapter)


class NotAnExporter:
    pass


if __name__ == "__main__":
    print("常规子类:", issubclass(CsvExporter, Exporter))
    print("hook 结构判定(未注册未继承):", issubclass(ThirdParty, Exporter))
    print("注册后判定:", issubclass(LegacyAdapter, Exporter))
    print("注册后 isinstance:", isinstance(LegacyAdapter(), Exporter))
    print("无关类:", issubclass(NotAnExporter, Exporter))
    try:
        Exporter()
    except TypeError as e:
        print("抽象类实例化被拦:", str(e)[:42])
```

**追问**:1) register 之后再改判定有什么坑?——ABCMeta 会缓存 issubclass 结果,运行期 register 会失效缓存,但自定义 hook 改判定逻辑不会,动态场景要主动处理。2) __subclasshook__ 的契约?——类方法签名 hook(subclass),返回 True/False/NotImplemented;NotImplemented 落回 MRO 与注册表常规判定;collections.abc 的 Iterable 就靠 hook 检查 __iter__(Q477)。3) hook 与 register 的关系?——hook 是结构判定(长得像就算),register 是名义声明(我说它算);两者叠加时 hook 先行——设计协议前先决定走哪条路。4) 生产陷阱?——hook 误判(名字在但签名不对)让 isinstance 承诺过头;register 不验实现(Q477);hook 返回值忘 NotImplemented 覆盖了名义判定。
