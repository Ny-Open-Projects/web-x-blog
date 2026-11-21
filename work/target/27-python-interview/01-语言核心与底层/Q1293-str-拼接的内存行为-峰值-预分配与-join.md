---
title: [Q1293] str 拼接的内存行为:峰值、预分配与 join
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1293 · str 拼接的内存行为:峰值、预分配与 join

> 难度:★★★☆☆ | 标签:str, 内存, 性能

**问**:从内存视角看,`s += p` 循环和 `''.join(parts)` 的分配行为差在哪?为什么两者的「峰值」可能差不多?

**答**:join 的分配是一次性的:先对序列求长度(或 length_hint)预分配结果缓冲,再逐段拷入,峰值 ≈ 结果大小 + 各片段本身。`s += p` 走 CPython 的就地扩容优化(Q425):左值唯一持有时 realloc 原地增长,旧缓冲被复用,瞬时峰值同样 ≈ 结果大小——所以「峰值」区分不出两者,真正拉开差距的是 realloc 的次数与搬迁成本:条件一破(存在别名、异常帧持有引用、非 CPython),+= 退化成每次分配新串的 O(n²) 时空行为。结论顺序:内存敏感且片段已知 → join;流式累积且确在 CPython → += 可接受;跨实现可移植 → 永远 join 或 io.StringIO。注意 join 也不万能:对「生成器片段」它会先物化成 list,额外峰值要算进去。

```python
# file: code/01_语言核心与底层/q1293_str_concat_memory.py
import sys
import time
import tracemalloc


def run_concat(parts, keep_alias=False):
    tracemalloc.start()
    s = ""
    alias = s if keep_alias else None   # 别名破坏就地扩容条件
    for p in parts:
        s += p
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    assert alias is not None or not keep_alias
    return peak


def run_join(parts):
    tracemalloc.start()
    s = "".join(parts)
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return s, peak


if __name__ == "__main__":
    parts = ["chunk%06d" % i for i in range(20000)]
    t0 = time.perf_counter()
    p1 = run_concat(parts)
    t1 = time.perf_counter()
    p2 = run_concat(parts, keep_alias=True)
    t2 = time.perf_counter()
    s, p3 = run_join(parts)
    t3 = time.perf_counter()
    print("+= unique  peak %.2f MB  %.1f ms" % (p1 / 1e6, (t1 - t0) * 1000))
    print("+= alias   peak %.2f MB  %.1f ms" % (p2 / 1e6, (t2 - t1) * 1000))
    print("join       peak %.2f MB  %.1f ms" % (p3 / 1e6, (t3 - t2) * 1000))
    print("result getsizeof:", sys.getsizeof(s))
```

**追问**:1) 为什么峰值都是「结果大小」量级?——中间串要么被 realloc 复用、要么引用归零立即释放,「同时存活」的字符串决定峰值;区别在分配次数,不在峰值上限。2) += 与 join 的本质差?——join 先求总长一次精确分配;+= 依赖 CPython 的 refcount==1 原地扩容优化,不可移植且多引用时退化 O(n²)。3) 增量构建的正解?——join(先物化列表)适合已知项;io.StringIO 适合流式;f-string 编译期优化适合少量插值;海量重复小串配合 intern。4) 生产陷阱?——大循环 += 在 Pypy/多引用场景性能崩;join 直接接生成器(会先物化成列表,量级没变但要有预期);以为 concat 是 O(1)。
