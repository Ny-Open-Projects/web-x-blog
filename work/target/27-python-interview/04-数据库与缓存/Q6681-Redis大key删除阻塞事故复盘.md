---
title: [Q6681] Redis 大 key 删除阻塞主线程事故复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6681 · Redis 大 key 删除阻塞主线程：一次 DEL 打挂全库的复盘

难度：P6 ｜ 标签：事故复盘、大 key、UNLINK、惰性释放
基线：Redis 4.0+ 支持 UNLINK 惰性删除；redis-py 5+ 的 `unlink()`。

**问**：运营后台一个 `hgetall` 出 800 万元素的 Hash 临时 key，下班前有人执行 `DEL`，整库命令延迟从 0.5ms 飙到数秒、上游大面积超时。事故链是什么？为什么删除一个 key 能阻塞整个实例？正确姿势是什么？

**答**：**结论**：Redis 命令执行是单线程，`DEL` 对集合类型要**同步释放所有元素**——百万级 field 的 Hash/ZSet/Set，释放本身的内存操作就要几十到几百毫秒，期间所有命令排队。事故链：临时 key 无 TTL → 无大 key 监控 → 手工 DEL 触发同步释放 → 主线程阻塞 → 从库同步等待 + 哨兵探测超时，放大成"全库抖动"。正确姿势：① 删集合类大 key 一律用 `UNLINK`（主线程只摘引用，释放交给后台 bio 线程异步做）；② 大 key 优先"渐进式清空"——`SCAN` 分批 + `HDEL` 小批量，或直接 `RENAME` 到垃圾前缀后小批量消费删除；③ 根治靠 TTL 兜底与写入前的体积闸（`MEMORY USAGE` 阈值拒绝）。

**取舍**：UNLINK 的代价是**异步释放期间的内存峰值**——元素还在被释放队列里，`used_memory` 短暂不降甚至上升，内存紧张实例可能触发淘汰甚至 OOM。所以内存富余用 UNLINK 一了百了；内存紧（接近 maxmemory）反而要**限速渐进删**，把释放摊到长时间窗口。RENAME+分批方案的优点是完全可控、可观测，缺点是多一次改名与代码路径。

**实战**：复盘后落地三件事：① 上大 key 巡检（`--bigkeys`/RDB 分析）与报警，阈值按 value 类型分别设；② 运维操作走工单脚本，禁手敲 DEL；③ 应用侧对"可变集合"设上限——Hash field 数超阈值告警，写路径拒绝。用标准库模拟渐进删除的账：

```python
# 大 key 渐进删除的模拟账：同步 DEL vs 分批 HDEL vs UNLINK
import time

TOTAL_FIELDS = 8_000_000          # 事故里的 Hash 大小
DEL_RELEASE_NS_PER_FIELD = 40     # 假设同步释放每 field ~40ns 的纯内存操作
hz_rate = 100_000                 # 后台释放线程每秒可释放的 field 数

# 方案 A：同步 DEL，主线程独占
blocking_ms = TOTAL_FIELDS * DEL_RELEASE_NS_PER_FIELD / 1e6
print(f"A) 同步 DEL 阻塞主线程约 {blocking_ms:,.0f} ms —— 上游 P99 全炸")

# 方案 B：UNLINK，主线程 O(1) 摘引用，后台线程释放
drain_s = TOTAL_FIELDS / hz_rate
print(f"B) UNLINK 主线程 <1ms；后台释放耗时约 {drain_s:,.0f}s，期间内存峰值不变")

# 方案 C：RENAME + 每批 5000 个 HDEL，限速保护内存
batch, per_cmd_ms = 5000, 0.3
batches = TOTAL_FIELDS // batch
wall_s = batches * per_cmd_ms / 1000
peak_fields = TOTAL_FIELDS  # 每批只删一小块，内存缓慢下降
print(f"C) 渐进删除总耗时约 {wall_s/60:,.0f} 分钟，"
      f"每批主线程占用 {per_cmd_ms}ms，内存线性下降")

# 体积闸：写入前拒绝超大集合
def guard_write(field_count: int, limit: int = 100_000) -> str:
    if field_count > limit:
        return f"REJECT: {field_count} > {limit}, 请拆分 key 或改结构"
    return "OK"

print(guard_write(80_000), guard_write(500_000))
```

**追问 1**：UNLINK 之后 `INFO` 里的 `used_memory` 为什么不立刻下降？什么信号能确认释放完成？
提示：释放挂在 bio 后台线程队列，`mem_fragmentation_ratio` 先升后回落；观察 `lazyfree_pending_objects` 归零即释放完毕。

**追问 2**：`SCAN` 渐进清理时为什么不能用 `KEYS` 配合？大 key 巡检本身会不会打挂实例？
提示：KEYS 是 O(N) 全库阻塞；巡检用 `SCAN` + `MEMORY USAGE` 抽样，且 `--bigkeys` 底层对集合做 LLEN/HLEN 只取元数据不拉全量，成本可控。

**追问 3**：如果这个大 key 是热读 key，渐进删除期间业务怎么读？
提示：RENAME 换名后旧 key 读不到即回源 DB——删除窗口要与低峰期对齐，或先建新结构双写，读切新 key 后再清旧 key。

## 背诵要点
1. 集合类大 key 的 `DEL` 是 O(N) 同步释放，会阻塞单线程主循环数百毫秒到秒级；Redis 4.0+ 用 `UNLINK` 摘引用后由 bio 线程异步释放。
2. UNLINK 代价是内存峰值不降（lazyfree_pending_objects 排队），内存紧张的实例改用"限速渐进删"。
3. 根治三件套：TTL 兜底、大 key 巡检报警（SCAN+MEMORY USAGE）、写入路径体积闸拒绝超大集合。

## 复盘追问
1. 这次事故里为什么监控没提前发现 800 万 field 的 Hash 在持续增长？巡检频率和阈值当时是怎么定的？
2. 复盘后的"禁手敲 DEL"如何落地成流程？谁有权限执行删除类运维命令，审计记录存在哪？
