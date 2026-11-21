---
title: [Q2889] 惰性求值的属性缓存:可失效的 cached_property
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2889 · 惰性求值的属性缓存:可失效的 cached_property

> 难度:★★★☆☆ | 标签:cached_property, 惰性求值, 缓存

**问**:一个属性算起来很贵,想第一次访问才算、之后走缓存,数据变了还要能重算,有几种实现?怎么失效?

**答**:两条路线:**手写版**用 `@property` 加一个 `_stats = None` 的缓存槽,首次计算后写入,`invalidate()` 置 None 触发重算,失效时机完全自己掌控,适合知道「什么变化该失效什么」的领域对象;**cached_property 版**把结果直接写进实例 `__dict__`,同名键遮蔽类上的描述符,后续访问零开销,失效就是 `del instance.attr`,删除后下次访问自动重算。选型看失效语义:数据被原地修改时两个版本都不会自动感知,必须显式失效——这是缓存属性的共性,不存在免费的自动失效。线程维度上,functools.cached_property 的 3.8-3.11 版本自带类级写锁,并发首次访问不会重复计算(但争用高);3.12 起 gh-90459 移除了锁,并发首次访问可能重复计算(最后写入者胜);手写版要么接受偶发的重复计算,要么自己加锁。

```python
# file: code/01_语言核心与底层/q2889_lazy_cached_attr.py
"""惰性求值的属性缓存:手写可失效的缓存属性与 cached_property 对比。"""
import functools


class Report:
    """手写版:显式缓存槽 + invalidate 方法,失效时机自己掌控。"""

    def __init__(self, rows):
        self.rows = rows
        self._stats = None

    @property
    def stats(self):
        if self._stats is None:
            print("  -> Report 计算一次")
            total = sum(self.rows)
            self._stats = {"total": total, "mean": total / len(self.rows)}
        return self._stats

    def invalidate(self):
        self._stats = None


class Dataset:
    """cached_property 版:缓存藏在实例 __dict__,删除键即失效。"""

    def __init__(self, rows):
        self.rows = rows

    @functools.cached_property
    def summary(self):
        print("  -> Dataset 计算一次")
        return {"total": sum(self.rows), "count": len(self.rows)}


if __name__ == "__main__":
    r = Report([3, 1, 2])
    print(r.stats)
    print(r.stats)                 # 第二次读缓存,不再打印计算
    r.rows.append(100)
    r.invalidate()
    print("失效后重算:", r.stats)

    d = Dataset([1, 2, 3])
    print(d.summary)
    print("缓存在实例字典里:", "summary" in vars(d))
    del d.summary                  # 删除键即失效,下次访问重算
    print("删除键后重算:", d.summary)
```

**追问**:1) 为什么 cached_property 敢把缓存写进实例 __dict__?——属性查找顺序里实例 __dict__ 优先于类上的非数据描述符,首次经由描述符计算后,同名实例键从此短路掉描述符调用,这正是 Q452 那套「用完即拆」的机制。2) 可失效缓存的实现面?——invalidate 方法 pop 实例字典键(Q452);或主动重算后写回;失效点要明确(数据变更处);多线程并发首次访问有重复计算(缓存击穿最小模型)。3) 与 slots/frozen 的兼容?——slots 无 __dict__ 不适用(Q2074);frozen 不可变字段缓存要另找容器;3.12 前类级锁在嵌套访问时可能死锁(Q452)。4) 生产陷阱?——缓存值引用 self 的对象图滞留;失效逻辑遗漏(数据变了缓存没变);fork 前已缓存状态被子进程复制。
