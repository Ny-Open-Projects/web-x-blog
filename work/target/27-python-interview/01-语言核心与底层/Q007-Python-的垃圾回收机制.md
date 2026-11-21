---
title: [Q007] Python 的垃圾回收机制
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q007 · Python 的垃圾回收机制

> 难度:★★★ | 标签:GC, 内存

**问**:Python 是如何回收内存的?引用计数之外为什么还需要分代回收?

**答**:CPython 主机制是引用计数,对象引用数归零立即释放,实时性好;但它解决不了循环引用,所以引入分代 GC:0/1/2 三代,新对象在 0 代,扫描后存活者晋升,越老扫描频率越低。分代 GC 只处理容器对象,通过 `gc` 模块可手动触发或调整阈值。另有 `weakref` 弱引用不增加引用计数,常用于缓存。

```python
# file: code/01_语言核心与底层/q007_gc.py
import gc
import weakref

class Node:
    def __init__(self, name):
        self.name = name
        self.partner = None

if __name__ == "__main__":
    gc.disable()   # 演示引用计数与分代回收分离
    a = Node("a")
    b = Node("b")
    a.partner = b
    b.partner = a  # 循环引用
    ref = weakref.ref(a)

    del a, b       # 引用计数不为零,因为互相持有
    print(ref() is not None)  # True,还活着

    gc.collect()   # 分代 GC 打破循环
    print(ref() is None)      # True,已被回收
    gc.enable()
```

**追问**:1) 内存泄漏在 Python 里还可能吗?——可能:全局集合无限增长、对象被注册到全局回调、`__del__` 参与的旧式循环(3.4 起已缓解)、C 扩展泄漏等。2) 分代阈值 (700, 10, 10) 是什么语义?——0 代「净分配数」(分配减释放)达到 700 触发一次 0 代扫描;0 代扫描 10 次把幸存者升入 1 代,1 代扫描 10 次升 2 代,老对象扫描频率指数级降低。3) 带 `__del__` 的循环引用现在能回收吗?——能,CPython 3.4 起 PEP 442 逐个安全终结,`gc.garbage` 常态为空;「旧式循环滞留」是过时答案,面试提这句反而是加分点。4) gc 是万能的吗?——只跟踪容器对象;C 扩展用 Py_INCREF 持有却不参与 GC 跟踪的内存(如部分 ctypes、原生库)不受管辖,这类泄漏要靠 tracemalloc 或 valgrind 定位。
