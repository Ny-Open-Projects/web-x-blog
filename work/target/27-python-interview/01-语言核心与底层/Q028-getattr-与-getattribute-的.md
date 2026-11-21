---
title: [Q028] __getattr__ 与 __getattribute__ 的区别
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q028 · __getattr__ 与 __getattribute__ 的区别

> 难度:★★★ | 标签:魔法方法, 类

**问**:两者何时触发?为什么 `__getattribute__` 里做逻辑容易出递归?

**答**:`__getattribute__` 是所有属性访问的总入口,无条件触发;`__getattr__` 只在常规查找失败后才被调用,适合做代理转发和惰性加载。在 `__getattribute__` 内访问 `self.anything` 会再次触发自身造成无限递归,必须改为 `super().__getattribute__(name)` 或 `object.__getattribute__`。对应地还有 `__setattr__`/`__delattr__`。

```python
# file: code/01_语言核心与底层/q028_getattr.py
class Lazy:
    def __init__(self):
        self.loaded = {}

    def __getattr__(self, name):     # 只在找不到时进入
        print(f"lazily computing {name}")
        self.loaded[name] = f"value-of-{name}"
        return self.loaded[name]

class Guarded:
    def __init__(self):
        self._x = 1

    def __getattribute__(self, name):
        print(f"access {name}")
        return super().__getattribute__(name)   # 必须 super 防递归

if __name__ == "__main__":
    o = Lazy()
    print(o.missing)     # 触发 __getattr__
    print(o.missing)     # 第二次走实例 dict,不再触发

    g = Guarded()
    _ = g._x
```

**追问**:1) 动态代理 RPC 客户端常用哪个?——`__getattr__`,把未知方法名转发给远端,避免拦截每一个内部属性访问带来的开销。2) __getattr__ 里的无限递归怎么发生?——在 `__getattr__` 内访问任何「不存在的」属性都会再次触发自身;安全写法是先访问 `self.__dict__` 或 `super().__getattribute__` 里的真实属性。3) 属性访问的完整查找顺序?——`type.__mro__` 上的 data descriptor → 实例 `__dict__` → non-data descriptor/类属性 → `__getattr__` 兜底;`__getattribute__` 是全量拦截入口,热路径上慎用。
