---
title: [Q2886] super 在多继承混入中的协作:MRO 接力与默认落地
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2886 · super 在多继承混入中的协作:MRO 接力与默认落地

> 难度:★★★★☆ | 标签:super, 多继承, Mixin, MRO

**问**:写 Mixin 有一条铁律「方法里必须调用 super」,为什么?不调会怎样?

**答**:Mixin 的方法不知道自己最终被排进什么 MRO,`super().fetch(key)` 不是「调父类」,而是「调 MRO 里的下一个类」——可能是另一个 Mixin,也可能一路传到核心实现。本例 Client 的执行序是缓存 miss 到日志到核心取数,每一层做一件事再交棒。三个要点:第一,混入方法要**无条件**调 super,少调一次就把链条后面的实现整段吞掉,这是多继承最隐蔽的 bug;第二,`__init__` 同样要接力并用 `*args, **kwargs` 透传参数,否则 MRO 上某个类的初始化会被跳过;第三,接力必须有终点——终点类的方法不再调 super,链条断在 object 上时 `super().fetch` 会抛 AttributeError,本例的 Lone 演示了这条路。缺一层混入并不可怕,BrokenClient 照常工作,MRO 只要求终点存在。

```python
# file: code/01_语言核心与底层/q2886_cooperative_mixin.py
"""super 在多继承混入中的协作:MRO 接力与 object 默认落地。"""


class Fetcher:
    """核心实现:混入链最终接力到这里,object 是隐式终点。"""

    def fetch(self, key):
        return f"data:{key}"


class LoggingMixin:
    def fetch(self, key):
        print(f"  [log] 进入 {type(self).__name__}.fetch key={key}")
        return super().fetch(key)


class CacheMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)      # 参数沿 MRO 继续传递
        self.cache = {}

    def fetch(self, key):
        if key in self.cache:
            print(f"  [cache] 命中 {key}")
            return self.cache[key]
        value = super().fetch(key)
        self.cache[key] = value
        return value


class Client(CacheMixin, LoggingMixin, Fetcher):
    pass


class BrokenClient(LoggingMixin, Fetcher):
    """少一层混入也能工作:MRO 跳过缺失能力,只要终点存在。"""
    pass


if __name__ == "__main__":
    print("MRO:", [cls.__name__ for cls in Client.__mro__])
    c = Client()
    print("第一次:", c.fetch("user:1"))
    print("第二次:", c.fetch("user:1"))

    b = BrokenClient()
    print("缺 CacheMixin 的客户端:", b.fetch("user:1"))

    # 反例:混入链上没有可接力的终点,super 停在 object
    class LoneMixin:
        def fetch(self, key):
            return super().fetch(key)

    class Lone(LoneMixin):
        pass

    try:
        Lone().fetch("x")
    except AttributeError as e:
        print("接力断在 object:", e)
```

**追问**:1) 怎么在开发期发现「忘了调 super」的混入?——单元测试断言整条链的组合行为(缓存命中不该再打日志之类),或用 inspect 遍历 MRO 静态检查每个中间类的方法体里有 super 调用。2) MRO 接力的完整纪律?——每个混入方法第一行 super().method(**kwargs)(转发不认领的参数,Q1808);基类实现兜底落地;默认值冲突由 MRO 序决定——「mixin 在前、基类在后」。3) 转发协议?——认领自己的 kwargs、原样转发其余;耗尽到 object.__init__ 必须为空;**kwargs 转发链的签名漂移要 review(Q2373)。4) 生产陷阱?——某层不调 super 截断链(本题);object 收到残留 kwargs TypeError;菱形继承重复初始化。
