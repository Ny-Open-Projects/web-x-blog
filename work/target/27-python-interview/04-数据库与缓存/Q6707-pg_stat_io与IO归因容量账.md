---
title: "[Q6707] pg_stat_io 与 IO 归因容量账"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6707 · pg_stat_io 与 IO 归因容量账

难度：P6 ｜ 标签：容量成本账、PostgreSQL 16、IO 观测、性能定位

基线：Python 3.12；PostgreSQL 16+；纯 Python 聚合演示。

**问**：磁盘 IO 打满了，但 `iostat` 只能告诉你"设备在忙"，说不清是业务查询、checkpoint 还是 autovacuum 干的。PG16 之前只能靠猜，PG16 给了什么新视图来做归因？怎么用它算一笔 IO 容量账？

**答**：
- **结论**：PostgreSQL 16 引入 `pg_stat_io`，按 backend_type（client backend / checkpointer / background writer / autovacuum worker 等）、context（read / write / extend）、object（relation / temp relation）三个维度统计 IO 操作次数与字节数。它第一次让"这些 IO 是谁产生的"有了权威答案：client backend 的 read 多说明缓存命中不足；checkpointer/bgwriter 的 write 多说明 checkpoint 压力；autovacuum 的 read 多说明膨胀或清理频繁。
- **取舍**：它统计的是 PostgreSQL **自己发起**的 IO，不含文件系统预读、其他进程、复制的简单读；要配合 OS 层 `iostat` 交叉验证。它是一个"归因方向盘"，不是开箱即用的告警阈值——阈值要结合业务基线定。
- **实战**：容量账这样算——用 `reads - hits` 估算缓存未命中、算出有效命中率；用 checkpointer 的 write 字节估算 checkpoint 写入带宽，进而调 `max_wal_size`/`checkpoint_timeout`；把 autovacuum 的 IO 单独拎出来评估是否需要限流（`autovacuum_vacuum_cost_limit`）。

```python
from collections import defaultdict

IOEvent = tuple[str, str, int]  # (backend_type, context, bytes)


def summarize(events: list[IOEvent]) -> dict[tuple[str, str], int]:
    """按 (backend, context) 聚合 IO 字节，模拟 pg_stat_io 的归因视角。"""
    agg: dict[tuple[str, str], int] = defaultdict(int)
    for backend, context, nbytes in events:
        agg[(backend, context)] += nbytes
    return dict(agg)


if __name__ == "__main__":
    events: list[IOEvent] = [
        ("client backend", "read", 4096),
        ("client backend", "write", 8192),
        ("checkpointer", "write", 16384),
        ("autovacuum worker", "read", 4096),
    ]
    for (backend, context), total in sorted(summarize(events).items()):
        print(f"{backend}/{context}: {total} bytes")
    # 谁在产生 IO 一目了然：业务读、checkpoint 写、autovacuum 读分开看。
```

**追问一**：`pg_stat_io` 的 read 里为什么要区分 hit 和 miss？
→ 解析：hit 表示数据已在 shared buffer 中、没有真实磁盘读；miss 才是物理读。命中率 = hits/(hits+misses)，是判断内存是否够、索引是否有效的核心指标。

**追问二**：checkpointer 的 write 很高，该怎么调优？
→ 解析：说明 checkpoint 写压力大。可通过增大 `max_wal_size`、拉长 `checkpoint_timeout` 让 checkpoint 更稀疏，或调 `checkpoint_completion_target` 让写入更平滑；代价是崩溃恢复时间变长——这是典型的容量与 RTO 取舍。
