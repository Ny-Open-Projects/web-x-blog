---
title: [Q2068] weakref 容器:弱引用字典与弱引用集合
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2068 · weakref 容器:弱引用字典与弱引用集合

> 难度:★★★★☆ | 标签:weakref, 缓存, 生命周期

**问**:WeakValueDictionary、WeakKeyDictionary、WeakSet 各适合什么场景?和普通容器差在哪?

**答**:三者共同点是容器本身不阻止对象被回收:键或值持有的是弱引用,对象在别处死亡后条目自动消失,容器不会内存泄漏。WeakValueDictionary 最常做缓存——值没有外部使用者就自动出缓存;WeakKeyDictionary 适合给别人的对象挂元数据,键销毁元数据跟着销毁,等价于「不改类定义的外挂属性表」;WeakSet 常用来追踪某类存活实例,做实例注册表或调试统计。注意三点:条目消失依赖弱引用回调,时机在对象销毁后同步触发(见 Q1289);值类型必须支持弱引用,__slots__ 类默认不行(Q2074);缓存语义与 lru_cache 互补——lru_cache 持强引用是泄漏高发点(Q045),弱引用容器让「没人用了就清理」成为默认行为。

```python
# file: code/01_语言核心与底层/q2068_weakref_containers.py
"""弱引用容器:缓存、元数据挂载与实例追踪三种场景。"""
import gc
import weakref


class Report:
    def __init__(self, rid):
        self.rid = rid


def value_cache_demo():
    cache = weakref.WeakValueDictionary()
    r1 = Report(1)               # 先持强引用
    cache["r1"] = r1             # 值侧是弱引用
    print("  放入后:", len(cache))
    del r1
    gc.collect()                 # 唯一强引用消失,条目自动移除
    print("  对象回收后:", len(cache))


def key_meta_demo():
    meta = weakref.WeakKeyDictionary()
    doc = Report(2)
    meta[doc] = {"last_open": "2026-01-01"}   # 键侧是弱引用
    print("  挂载元数据:", meta[doc])
    del doc
    gc.collect()
    print("  键销毁后:", len(meta))


def instance_tracking_demo():
    seen = weakref.WeakSet()

    class Node:
        def __init__(self):
            seen.add(self)

    a, b = Node(), Node()
    print("  存活实例数:", len(seen))
    del a, b
    gc.collect()
    print("  全部回收后:", len(seen))


if __name__ == "__main__":
    print("WeakValueDictionary 充当自动过期的缓存:")
    value_cache_demo()
    print("WeakKeyDictionary 给对象挂外挂元数据:")
    key_meta_demo()
    print("WeakSet 追踪存活实例:")
    instance_tracking_demo()
```

**追问**:1) WeakValueDictionary 与 lru_cache 什么关系?——lru_cache 强引用参数与结果,是泄漏高发点,弱引用值容器让缓存不阻止回收;条目移除的时机?——弱引用回调在对象销毁后同步触发,但遍历容器与回收竞争时行为要小心,见 Q1289。2) 两个容器的分工?——WeakValueDictionary 值弱(对象回收条目消失,适合「活着的资源注册表」);WeakKeyDictionary 键弱(身份索引,适合给外部对象挂元数据)。3) 与 lru_cache 的取舍?——强引用缓存保证命中,弱引用缓存「有人用才活」;热点数据弱引用缓存会反复失效——按「资源生命周期」选。4) 生产陷阱?——遍历中条目消失(先 list 快照,Q436);slots 类没 __weakref__ 进不了弱容器(Q2074);弱值容器存的「主数据」其实还有别处引用,回收时机与预期不符。
