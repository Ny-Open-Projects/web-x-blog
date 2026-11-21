---
title: [Q5053] gc 分代阈值与 gc.freeze 的容量规划
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5053 · gc 分代阈值调优与 gc.freeze 的容量规划

> 难度:★★★★ | 标签:gc, 分代回收, gc.freeze, fork COW, 容量规划

**问**：一个 fork 出 16 个 worker 的常驻服务，预热后做一次全量缓存加载，结果 worker 的 RSS 全部翻倍、P99 出现周期性毛刺。分代 GC 的触发条件是什么？`gc.freeze()` 解决什么问题？gc 调优在容量规划里怎么算账？

**答**：CPython 用三代分代回收处理**引用环**（纯引用计数的对象不归它管）。触发条件是计数器：0 代分配对象数减释放数超过阈值 0（默认 700）就触发 0 代回收；0 代每回收 10 次（阈值 1）触发 1 代，1 代每 10 次（阈值 2）触发 2 代。毛刺来源是**全量缓存让大量对象升级进 1/2 代**，2 代回收要扫描几十万个对象，一次就是几十毫秒的 STW 式暂停，周期性 P99 毛刺往往就是它。容量账两笔：a) **暂停账**——对象规模 × 扫描成本，把 2 代回收频率压下来或干脆 `gc.disable()` + 手动分片触发；b) **COW 账**——fork 后父子共享物理页，但 GC 改对象头里的引用计数会写页触发 COW，全 worker 的 RSS 各自翻倍。`gc.freeze()` 把**当前所有存活对象移入"永久代"不再参与回收**：预热完、fork 之前调用，子进程不再为这些对象写引用计数，COW 命中率大增（这就是 Instagram 那个著名优化的落地姿势）。注意 `gc.disable()` 的风险：只要存在引用环且对象带 `__del__`/大缓冲，环就永远不回收——禁 GC 的服务必须自己证明"无环"或定期 `gc.collect(0)` 分片兜底。

```python
# file: code/01_语言核心与底层/q5053_gc_freeze.py
import gc

# 1) 观察默认阈值与分代计数
print("默认阈值 (t0, t1, t2):", gc.get_threshold())      # (700, 10, 10)
print("当前各代计数:", gc.get_count())                    # 未达 t0 不会触发
print("历史回收次数(每代):", [s["collections"] for s in gc.get_stats()])

# 2) 压低 0 代频率: 高吞吐服务常用手法
gc.set_threshold(2000, 20, 20)
batch = [{} for _ in range(1500)]     # 1500 < 2000, 不触发 0 代
print("分配 1500 个对象后计数(未触发):", gc.get_count())

# 3) freeze: 预热完成后, fork 之前调用
cache = [bytearray(64) for _ in range(10_000)]   # 模拟全量缓存
gc.collect()          # 先把环清干净再冻结
gc.freeze()           # 存活对象移入永久代, 不再参与回收 -> fork 后 COW 命中提升
print("freeze 后新增对象仍正常分代:", gc.get_count())

# 4) 验证冻结对象不进回收: collect 不清 cache (无环本就不清, 关键是不再扫描)
kept = gc.freeze.__doc__.splitlines()[0]
print("freeze 语义:", kept)
```

**追问**：1) `gc.disable()` 后引用环就完全不管了，怎么兜底？——请求级兜底：每个请求/批任务结束后调 `gc.collect(0)`（只扫 0 代，成本可控），定时任务里低峰跑 `gc.collect(2)` 全量；同时用 `gc.set_debug(gc.DEBUG_SAVEALL)` 离线复现环泄漏。2) `gc.freeze()` 后新分配对象还正常回收吗？——正常，freeze 只把"当时存活"的对象移入永久代，之后新增对象照常分代；所以调用时机必须放在"预热完成、fork 之前"，早了冻不住缓存、晚了白冻。3) free-threading（no-GIL）构建下这套调优还成立吗？——分代 GC 被换成更复杂的并行方案，`gc.freeze` 的 COW 收益仍在（fork 场景），但阈值语义与暂停模型完全不同，不能照搬数字。

## 背诵要点
- 默认阈值 (700, 10, 10)：分配-释放差超 700 触发 0 代，代间按 10 倍晋升；2 代全扫是 P99 周期毛刺的经典来源。
- 预热完成 → `gc.collect()` → `gc.freeze()` → fork：冻结对象不参与回收，fork 后 COW 命中大增，RSS 不再翻倍。
- `gc.disable()` 必须配 `gc.collect(0)` 请求级兜底，否则引用环（含 `__del__`/大缓冲）永久泄漏。

## 复盘追问
- 你们服务 2 代 GC 的触发频率和单次耗时观测过吗？怎么观测？（提示：`gc.callbacks` 挂钩记录 phase="start/stop" 的时间差与 get_stats）
- 全量缓存加载后 worker RSS 翻倍，你怎么证明是 GC 写页触发 COW 而不是缓存本身？（提示：freeze 前后对比 fork 子进程 RSS，或用 `smaps_rollup` 看 Shared_Clean 占比）
