---
title: [Q404] weakref 的生产级应用:缓存与解耦观察者
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q404 · weakref 的生产级应用:缓存与解耦观察者

> 难度:★★★★☆ | 标签:weakref, 内存管理

**问**:为什么用 dict 直接做对象缓存会造成"越用越占内存"?weakref 如何在"持有引用"和"阻止回收"之间取得平衡?哪些内建类型不能被弱引用?

**答**:强引用缓存让对象计数永远 ≥ 1,GC 永远不回收,缓存变成事实上的内存泄漏。`weakref` 提供不增加计数的"旁路引用":对象真实生命周期仍由业务强引用决定,缓存、观察者列表、回调注册表只挂弱引用,对象死亡时弱引用自动失效(或回调被触发)。典型应用:`weakref.WeakValueDictionary` 做实例缓存、`WeakSet` 做监听器集合(避免监听器反过来延长发布者生命周期)、`weakref.finalize` 管理外部资源。`list`、`dict`、`str`、`int` 等内建类型默认不支持弱引用,需要子类化后才行——这是面试里的高频陷阱。

```python
# file: code/01_语言核心与底层/q404_weakref_cache.py
import weakref

class Heavy:
    def __init__(self, name):
        self.name = name

cache = weakref.WeakValueDictionary()   # 值是弱引用

obj = Heavy("model")
cache["model"] = obj                    # 缓存不阻止回收
print("hit:", cache.get("model").name)

del obj                                 # 强引用消失
print("after del, hit:", cache.get("model"))   # None,条目自动蒸发

# 观察者模式:发布者不延长监听器生命周期
class Publisher:
    def __init__(self):
        self.listeners = weakref.WeakSet()
    def notify(self):
        for l in list(self.listeners):
            print("notify", l.name)

pub = Publisher()
listener = Heavy("listener")
pub.listeners.add(listener)
pub.notify()
del listener                            # 监听器可被独立回收
```

**追问**:1) `WeakValueDictionary` 遍历时抛 `KeyError`/`RuntimeError` 怎么回事?——遍历过程中弱引用可能恰好死亡,必须先 `list(d)` 快照再迭代。2) `weakref.ref` 与 `WeakKeyDictionary` 的区别?——前者是裸引用需手动调用取值,后者以对象为键,常用于给第三方对象挂附加元数据。
