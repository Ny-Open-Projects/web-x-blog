---
title: "[Q5205] sys.getallocatedblocks：比 RSS 更早看到内存增长"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5205 · sys.getallocatedblocks：比 RSS 更早看到内存增长

难度：P7 ｜ 标签：内存、getallocatedblocks、分配器、泄漏趋势、tracemalloc

**问**：RSS 还没涨，但服务跑 12 小时后突然 OOM；等 RSS 抬头时已经晚了。`sys.getallocatedblocks()` 返回的是字节数吗？它能比 RSS 更早发现泄漏吗？为什么对象都删了，块计数还不回到基线？它和 `tracemalloc` 怎么配合？

**答**：
结论：`sys.getallocatedblocks()` 返回 CPython **当前分配的块数**（pymalloc 的 pool 块 + 大对象 malloc 块），不是字节数；块大小按 size class 分档，所以"块数 × 平均块大小"只是粗略估算。它的价值是**趋势**：如果每轮请求结束后 `gc.collect()` 再采样，基线持续上移，说明有对象/容器没释放；RSS 受 arena 保留、页回收、glibc 缓存影响，往往滞后。

取舍：a) 采样要"稳定态"：请求处理完、`gc.collect()` 后取，避免把临时峰值当泄漏；b) 块计数不降不一定是泄漏：分配器会保留 arena/pool，块可能被复用，但不会立刻还给 OS；c) 定位"谁分配"用 `tracemalloc` 快照对比，定位"哪个对象没释放"用 `gc.get_objects`/`get_referrers`；d) 只适用于 CPython，PyPy 的 GC/分配模型不同；e) 监控上报用差分和斜率（块/请求），不要用绝对值跨版本比较。

实战：事故形态是"任务队列每轮创建一个闭包注册到全局回调表，RSS 稳定了 10 小时，第 11 小时 arena 用尽开始向 OS 要内存，随后 OOM；如果每轮采样 allocated blocks，会在第 1 小时就看到基线单调上涨"。下面演示分配 5 万个 dict 后的块增量、释放后的回落，以及"不保证归零"的分配器行为。

```python
import gc
import sys

gc.collect()
base = sys.getallocatedblocks()

items = [{"i": i, "payload": [i] * 4} for i in range(50_000)]
peak = sys.getallocatedblocks()

print("[1] 分配块增量:", peak - base)
print("[2] 不是字节数，只是块计数:", peak > base)

del items
gc.collect()
after = sys.getallocatedblocks()
print("[3] 释放后相对基线的差:", after - base)
print("[4] 不保证归零：分配器会保留 arena:", after >= base)
print("[5] 泄漏看的是每轮稳定态基线是否持续上移")
```

**追问一**：为什么 `after` 有时等于基线、有时高很多？—— 取决于分配模式：大量同尺寸小对象会走 pymalloc pool，释放后 pool 可能留在 arena 里（块可复用但计数未必立刻降）；大对象直接 malloc/free，可能还给 OS。还有采样时解释器内部的缓存（类型缓存、free list）会占块。所以单点绝对值没意义，要看"多轮请求后的稳定态斜率"。

**追问二**：`tracemalloc` 和它怎么分工？—— `tracemalloc` 记录**分配点的 Python 栈**和字节数，适合回答"哪一行分配得多"；`getallocatedblocks` 是全局块计数，开销极低，适合做"是否在涨"的告警信号。组合用法：块计数触发告警 → 开 `tracemalloc` 抓两份快照 → 对比定位分配点 → 用 `gc.get_referrers` 找持有链。

## 背诵要点
- `sys.getallocatedblocks()` 是块数不是字节；稳定态基线持续上移 = 可能有泄漏。
- 释放后不保证归零：pymalloc arena 会保留；看趋势不看绝对值。
- 块计数做告警，`tracemalloc` 定位分配点，`get_referrers` 找持有者。

## 复盘追问
- RSS 没涨但 OOM，怎么提前发现？（每轮稳定态 allocated blocks 斜率）
- 对象删了块计数不降，是泄漏吗？（不一定，arena/pool 保留与 free list 复用）
