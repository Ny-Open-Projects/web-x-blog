---
title: [Q6508] 慢查询治理:pg_stat_statements 与计划回归
date: 2026-11-18
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6508 · 慢查询治理:pg_stat_statements 与计划回归

> 难度:★★★ | 标签:PostgreSQL, 性能, 观测

**问**：线上某接口时好时坏，慢查询日志抓到的 SQL 都是同一条，EXPLAIN 又很快。这种"薛定谔的慢查询"怎么系统性治理？pg_stat_statements 在里面扮演什么角色？

**答**：结论：慢查询治理的闭环是"pg_stat_statements 定位Top SQL → 真实参数 EXPLAIN (ANALYZE, BUFFERS) 定位计划 → 归因统计信息漂移或索引缺失 → 治理并固化基线做计划回归"。时好时坏的经典根因是**计划回归**：表数据分布变化后 ANALYZE 不及时，planner 在 Index Scan 和 Seq Scan 之间跳变；或 plan_cache_mode 下 prepared statement 用了通用计划（generic plan）而实际参数选择性差异巨大。

实战路径：
- `pg_stat_statements` 按 `queryid` 聚合：看 `total_exec_time`（累计）、`mean_exec_time`（均值）、`calls`（频次）、`shared_blks_read`（ IO 压力）。定位要按 total 排（累计伤害最大），不是单次 mean。它是"事后统计全景"，慢日志是"逐条记录"，两者互补。
- 计划回归的判据：同 queryid 的 mean_exec_time 方差异常大。治理手段：`ANALYZE 表` 刷统计、必要时 `SET plan_cache_mode = force_custom_plan`（参数化但选择性差异大的语句）、补索引或改写 SQL。SQLAlchemy 侧的 `executemany`/绑定参数风格会影响计划形态，治理要落到 ORM 层。
- 固化防线：每天巡检 Top 20 SQL 的 mean/total 并与基线对比，漂移 > 50% 告警；重大发布前对核心 SQL 跑一次 EXPLAIN 快照 diff。这就是"计划回归测试"的朴素落地，比等用户报障便宜两个数量级。

```python
# 基线:Python 3.9+ 标准库;巡检 pg_stat_statements Top SQL 并做基线对比(可运行)
BASELINE = {  # queryid -> 昨日 mean_exec_time(ms)
    101: 12.0, 102: 3.5,
}

TODAY = {     # 模拟今天 pg_stat_statements 查询结果(queryid, calls, mean_ms)
    (101, 8000, 45.0),   # 均值回归:12ms -> 45ms
    (102, 2, 3.6),
    (103, 900, 80.0),    # 新晋 Top
}

def drift_report(threshold: float = 0.5) -> list[str]:
    out = []
    for qid, calls, mean in sorted(TODAY, key=lambda x: -x[1] * x[2]):
        base = BASELINE.get(qid)
        if base and mean > base * (1 + threshold):
            out.append(f"[REGRESS] queryid={qid} mean {base}ms -> {mean}ms "
                       f"({(mean/base-1):.0%}) calls={calls}")
        elif not base and calls * mean > 50_000:
            out.append(f"[NEW-TOP] queryid={qid} total={calls*mean/1000:.1f}s calls={calls}")
    return out or ["OK"]

if __name__ == "__main__":
    print("\n".join(drift_report()))
    # [REGRESS] queryid=101 ...
    # [NEW-TOP] queryid=103 ...
```

**追问**：
- 一层追问：为什么"EXPLAIN 很快"不能证明线上没问题？——EXPLAIN 默认不带参数与真实数据规模，且不吃执行期缓存状态；必须用真实慢参数跑 `EXPLAIN (ANALYZE, BUFFERS)`，对比 estimated rows 与 actual rows，差一个数量级以上就是统计信息问题。
- 二层追问：prepared statement 的 generic plan 什么时候启用、怎么关？——PG 判定自定义计划累计成本不占优后（默认 5 次后评估）切通用计划；参数选择性差异大的语句会受害。会话级 `plan_cache_mode=force_custom_plan` 或应用侧不用 server-side prepared 即可规避，代价是计划开销。
- 三层追问：pg_stat_statements 自身的代价？——需 `shared_preload_libraries` 并占共享内存，哈希上限（pg_stat_statements.max）外的查询会被合并计入"其他"，监控大库要调大 max 并理解 queryid 在 pg 升级/统计重置后会变。
