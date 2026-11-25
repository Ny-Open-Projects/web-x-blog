---
title: "[Q6774] worker 配比拉满反而更慢：PG 并行查询与全局池的争抢账"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6774 · worker 配比拉满反而更慢：PG 并行查询与全局池的争抢账

难度：P6 ｜ 标签：PostgreSQL、并行查询、max_parallel_workers、Gather、容量规划

基线：Python 3.12；建模并行扫描的 setup 成本、收益递减与全局 worker 池争抢，逐点扫描找最优 per_gather 配比，全标准库实跑。

**问**：`max_parallel_workers_per_gather` 拉满到 8，报表查询却没快多少，高峰期反而更慢。并行查询的代价模型里有哪些隐藏成本？worker 池是共享的吗，多个并行查询同时跑时怎么分？per_gather 应该配多大？

**答**：
- **结论**：并行查询不是免费分身，三笔隐藏成本：① **setup 成本**：Gather 节点要 fork worker、初始化上下文、汇总结果——小表上这笔比扫描本身还贵，所以有 `min_parallel_table_scan_size` 门槛先挡；② **收益递减**：worker 不是线性加速，leader 合并子结果、进程间通信都有开销，4 worker 的实际加速常见只有 2-3 倍；③ **池争抢**：`max_parallel_workers` 是全局池，`per_gather` 只是单查询的**申请上限**——并发 4 条查询都申请 8 个时，每条实得 `max(1, 8/4)=2` 个，配置形同虚设且 planner 的代价估算（按申请数算）与实际执行（按实得数算）脱节，计划质量双双劣化。最优 per_gather 通常远小于核数：**用全局池除以预期并发来配**，宁可单查询少拿一点，也别让并发争抢。
- **取舍**：① 报表高峰与 OLTP 并存的库：per_gather=2~4、max_parallel_workers=核数的 50%-75%（留核给 OLTP 连接），避免报表把 CPU 吃光拖垮点查；② leader 是否参与扫描（`parallel_leader_participation`）：参与提高小并行度下的利用率，不参与降低 leader 成为瓶颈的概率，扫描代价大、worker 少时倾向参与；③ 并行只覆盖部分算子（seq scan、join、agg），计划里非并行段仍是串行瓶颈——看 EXPLAIN 先找 Gather 覆盖率（Q6638 EXPLAIN-ANALYZE 工具链）；④ 并行写不是并行：INSERT/UPDATE 大批量的瓶颈在锁与 WAL，别指望加 worker。
- **实战**：① 先量并发画像：高峰同时有几条并行查询，再定 per_gather（全局池/并发）；② 大促前的报表压测把 per_gather 各档跑一遍取拐点，别按文档默认值上生产；③ 监控 `pg_stat_activity` 里并行 worker 的实际占用 vs 配置上限，发现长期满池就是争抢信号；④ 会话级覆盖（`SET max_parallel_workers_per_gather`）给特定报表用小并行度，避免一刀切。

```python
"""Q6774 PG 并行查询 worker 配比: setup 成本+收益递减+并发争抢, 逐点找拐点。"""
SERIAL_COST = 100.0          # 全表扫描串行代价
SETUP_COST = 12.0            # Gather 节点启动/回传固定代价
TOTAL_WORKERS = 8            # max_parallel_workers 全局池
CONCURRENT_QUERIES = 4       # 同时在跑的并行查询数


def plan_cost(per_gather: int, concurrent: int) -> float:
    """单查询代价: setup + 扫描分摊 + 收益递减(通信合并开销)."""
    got = max(1, min(per_gather, max(1, TOTAL_WORKERS // concurrent)))  # 争抢折损
    scan = SERIAL_COST / got
    diminishing = SERIAL_COST * 0.04 * (got - 1)   # leader 合并/通信开销
    return SETUP_COST + scan + diminishing


if __name__ == "__main__":
    print("并发 4 条查询, 单查询配置 per_gather 的实际代价:")
    best_pg, best_cost = None, float("inf")
    for pg in range(1, 9):
        c = plan_cost(pg, CONCURRENT_QUERIES)
        print(f"  per_gather={pg}: worker 实得 {max(1, min(pg, TOTAL_WORKERS // CONCURRENT_QUERIES))}, "
              f"代价 {c:.1f}")
        if c < best_cost:
            best_pg, best_cost = pg, c
    serial = plan_cost(1, 1)
    print(f"\n最优 per_gather={best_pg} (代价 {best_cost:.1f}) vs 串行 {serial:.1f}")
    ok = best_pg == 2 and best_cost < serial
    print(f"校验: 小配置反而最快(争抢折损) -> {'通过' if ok else '异常'}")
    print("结论：并行收益 = max(1, 总池/并发) 截断后的实得数;")
    print("      per_gather 别拉满, 留余量给并发; 小表 setup 占大头, min_parallel 尺寸门槛先挡")
```

**追问一**：为什么 planner 的代价估算会与实际执行的 worker 数脱节？这会带来什么连锁问题？

→ 解析：planner 做 EXPLAIN 时按"申请数"（per_gather）估扫描分摊，实际执行时 worker 从全局池**尽力分配**——池子被别的查询占用时实得数更少，执行时间比估算长。连锁问题：① 估算的并行计划可能输给估算的串行计划（真实执行时并行实际更快/更慢都可能与估算相反），造成计划选择整体偏移；② 长期"实得 < 申请"会让某报表的执行时间方差变大（取决于它跑的时候有没有邻居），呈现为不可解释的延时抖动；③ 监控上 EXPLAIN 里 workers_planned 与 workers_launched 的差值就是争抢的直接证据。治理：per_gather 按并发画像收着配，让"申请≈实得"成为常态，估算与执行重新对齐。

**追问二**：并行 seq scan 的页是怎么分给 worker 的？为什么并行扫描反而可能让缓存命中率变差？

→ 解析：并行扫描用**动态块分配**：worker 轮流认领 chunk（每次 32KB 起，随扫描进度加大），谁扫完谁再领，不按范围预先切分（避免数据倾斜的 worker 拖尾）。缓存视角的问题：① 多个 worker 并发读不同区段，同一页被 leader 侧的后续算子再次需要时可能已被逐出——并行度放大了工作集瞬时大小，buffer pool 命中率下降；② 并行扫描倾向于整表顺序读，绕过缓存直接走大 IO，这是设计使然（它假设数据量大到缓存放不下）。所以"并行查询变慢"的排查要分两层：CPU 维度看争抢（本卡模型），IO 维度看 buffer 命中与 read 时延（Q6707 pg_stat_io 归因）。两者叠加时先降并行度再扩内存——争抢是配置错误，缓存是负载本性。
