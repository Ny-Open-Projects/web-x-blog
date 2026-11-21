---
title: [Q429] CPython 对象的内存布局:PyObject 头部与内存分配器
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q429 · CPython 对象的内存布局:PyObject 头部与内存分配器

> 难度:★★★★★ | 标签:内存布局, pymalloc, CPython

**问**:每个 Python 对象头部有什么?为什么说 CPython 有"三层内存分配"?`sys.getsizeof([])` 返回 56 意味着什么、不包括什么?`tracemalloc` 和 `sys.getsizeof` 什么时候对不上?

**答**:每个对象头部是 `PyObject`:`ob_refcnt`(8 字节)+ `ob_type`(8 字节),容器对象再加 `ob_size`/`_gc_next`/`_gc_prev`(GC 头 16 字节)。分配走三层:小对象(≤512 字节)用 pymalloc 的 arena/pool/block 三级池化(减少 malloc 碎片与系统调用),大对象直落 `malloc`,再底层是操作系统页。`sys.getsizeof([])` 只统计该对象自身结构(空 list 的表头),不含元素对象,也不含扩容后已分配的容量——`list` 过度分配(约 1.125 倍增长因子)让 `getsizeof` 与实际分配不符;`tracemalloc` 统计的是 malloc 层面的真实分配总量,含一切,所以两者对不上是常态:排查泄漏用 tracemalloc 快照 diff,估算单对象布局用 getsizeof/ctypes。

```python
# file: code/01_语言核心与底层/q429_object_layout.py
import ctypes
import sys
import tracemalloc

class Box:
    __slots__ = ("v",)
    def __init__(self, v):
        self.v = v

print("refcnt offset layout (CTypes 只读观察):")
raw = ctypes.cast(id(1), ctypes.POINTER(ctypes.c_ssize_t))
print("head value of small int 1:", raw[0])       # 3.12+(PEP 683)不朽对象此值是标记值;3.12 前是普通 refcnt(小整数被大量引用,同样很大)
print("type ptr equal to int type:", ctypes.cast(id(1), ctypes.POINTER(ctypes.c_void_p))[1] == id(int))

print("getsizeof:", sys.getsizeof([]), sys.getsizeof([None]),
      "list 过度分配:", sys.getsizeof([None] * 100))
tracemalloc.start()
data = [Box(i) for i in range(100_000)]
print("tracemalloc total MB:", round(tracemalloc.get_traced_memory()[0] / 2**20, 1))
print("getsizeof 不会告诉你元素成本")
```

**追问**:1) free-threading 构建下对象头多了什么?——biased refcount 扩展为本地+共享两部分、以及每对象锁位,头部更大,这是 free-threading 内存开销的主要来源之一。2) pymalloc 的 arena 为什么有时不还给 OS?——arena 释放要求整块页全空,碎片化后出现 "arena 不释放、RSS 高位平台期" 的经典现象,3.6 后已大幅缓解但仍需理解。
