---
title: [Q1261] 不朽对象 PEP 683:为什么 refcount 观测失真了
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1261 · 不朽对象 PEP 683:为什么 refcount 观测失真了

> 难度:★★★★☆ | 标签:引用计数, PEP 683, CPython

**问**:`sys.getrefcount(None)` 返回的数字在 3.12 里突然变成 40 多亿,是 bug 吗?不朽对象解决什么问题?

**答**:不是 bug。3.12 的 PEP 683 把内置单例(None、True、False、小的 int、部分静态字符串)做成「不朽对象」:refcount 被固定为一个特殊大值,永远不增不减,也不再参与 GC 跟踪。动机是 free-threading(PEP 703,Q411):共享的引用计数需要昂贵的原子操作或锁,而单例本来就不该被回收,冻结其计数后增减可以直接跳过;顺带也省掉了海量小对象(如 False)的计数器写,降低多核缓存争用。副作用是依赖 getrefcount 观测引用情况的老代码、以及靠计数判断「唯一持有」的 C 扩展,在这些对象上会失真——这正是本题的考点:refcount 是实现细节,不是 API 契约。

```python
# file: code/01_语言核心与底层/q1261_immortal_objects.py
import sys

if __name__ == "__main__":
    print("python:", sys.version.split()[0])
    print("getrefcount(None) :", sys.getrefcount(None))
    print("getrefcount(True) :", sys.getrefcount(True))
    print("getrefcount(2**60):", sys.getrefcount(2 ** 60))
    x = object()
    print("plain object      :", sys.getrefcount(x), "传入即临时 +1")
    if sys.version_info >= (3, 12):
        print("3.12+ PEP 683:内置单例是不朽对象,计数恒为巨大常量")
    else:
        print("当前版本:以上是真实计数,会随全局引用增减")
```

**追问**:1) 怎么判断一个对象是否不朽?——3.12 起有私有 C API `_Py_IsImmortal`;Python 层没有公开 API,只能用 getrefcount 的大小与不变性间接推断,不要在生产逻辑里依赖它。2) 不朽对象为什么让 refcount 观测失真?——引用计数字段取饱和值永不增减,getrefcount 返回巨大常数;释放路径直接跳过——基于 refcount 波动的内存诊断脚本对 None/True/小整数等会误判。3) 不朽的收益?——fork 写时复制友好(共享对象不再被计数写触发拷贝,1b Q404 的 fork+COW 故事)、GC 免扫常驻对象、去掉「小整数数组计数更新」的锁竞争。4) 生产陷阱?——3.12+ 与旧版本 refcount 行为不一致,跨版本工具要分支;依赖「计数差值」做 instrumentation 的库全部失真。
