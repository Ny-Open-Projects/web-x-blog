---
title: "[Q6721] Handler_read_*：不打开慢日志也能定位读放大"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6721 · Handler_read_*：不打开慢日志也能定位读放大

难度：P6 ｜ 标签：MySQL、Handler 计数器、读放大、覆盖索引

基线：Python 3.12；MySQL 5.7/8.0 `SHOW GLOBAL STATUS LIKE 'Handler_read%'`；纯 Python 模拟计数器语义。

**问**：线上 QPS 没涨、慢日志也没有明显慢 SQL，但 InnoDB 的读 IOPS 一直偏高。DBA 让你先用 `Handler_read_*` 做一次归因，这几个计数器分别代表什么？怎么只看计数器就判断是"全表扫太多"还是"回表太多"？

**答**：
- **结论**：`Handler_read_*` 统计的是**存储引擎层向上层交付行的方式**，不是 SQL 次数。关键四个：`Handler_read_first`（索引/表的第一条，全索引扫或全表扫的起点）、`Handler_read_next`（按索引顺序读下一行）、`Handler_read_rnd`（按行号随机定位，通常是回表）、`Handler_read_rnd_next`（数据文件顺序读下一行，全表扫的典型信号）。诊断口径：`read_rnd_next` 增长快 → 全表扫多；`read_next` 高而 `read_rnd` 也高 → 索引扫了但大量回表（未覆盖）；`read_next` 高、`read_rnd` 低 → 覆盖索引生效。再配合 `Innodb_rows_read` 与 `Innodb_buffer_pool_read_requests` 算每行成本。
- **取舍**：计数器是**实例级累计值**，只能做趋势与增量归因，不能直接指到某条 SQL；要按业务时段做差值（两次采样），并与 `performance_schema` 的 SQL 摘要关联才能定位单条语句。`read_rnd` 并不必然坏：小结果集回表比全表扫便宜；把 `read_rnd` 打到零往往要靠覆盖索引，代价是索引变宽、写放大与 buffer pool 占用上升。
- **实战**：① 固定 1 分钟采样 `SHOW GLOBAL STATUS` 做差值，按 `read_rnd_next / read_next` 比值告警；② 比值突增先查是否有人加了 `LIKE '%x'`、函数包裹列、隐式类型转换；③ `read_rnd` 高时用 `EXPLAIN` 看是否 `Using index` 缺失，优先补联合索引而不是加单列索引；④ 计数器重启归零，必须用监控平台的 rate 而非原始值。

```python
"""用计数器增量归因读放大：全表扫 / 索引扫 / 回表三种路径。"""


class HandlerStats:
    def __init__(self) -> None:
        self.first = 0
        self.next = 0
        self.rnd = 0
        self.rnd_next = 0

    def snapshot(self) -> dict[str, int]:
        return {"first": self.first, "next": self.next,
                "rnd": self.rnd, "rnd_next": self.rnd_next}

    def diff(self, before: dict[str, int]) -> dict[str, int]:
        return {k: v - before[k] for k, v in self.snapshot().items()}


def full_scan(stats: HandlerStats, rows: int) -> None:
    stats.first += 1                 # 定位到第一行
    stats.rnd_next += rows           # 顺序读完整张表


def index_scan_with_lookup(stats: HandlerStats, rows: int) -> None:
    stats.first += 1                 # 索引上定位第一条
    stats.next += rows               # 按索引顺序读
    stats.rnd += rows                # 每行按主键回表


def covering_index_scan(stats: HandlerStats, rows: int) -> None:
    stats.first += 1
    stats.next += rows               # 索引里就有全部列，不回表


def diagnose(delta: dict[str, int]) -> str:
    if delta["rnd_next"] > delta["next"] * 2:
        return "全表扫为主：查谓词是否可索引"
    if delta["rnd"] > delta["next"] * 0.8:
        return "索引扫 + 大量回表：考虑覆盖索引"
    if delta["next"] > 0 and delta["rnd"] == 0:
        return "覆盖索引生效"
    return "读路径混合，需下钻单条 SQL"


if __name__ == "__main__":
    rows = 10_000
    for name, fn in (("全表扫", full_scan),
                     ("索引+回表", index_scan_with_lookup),
                     ("覆盖索引", covering_index_scan)):
        stats = HandlerStats()
        before = stats.snapshot()
        fn(stats, rows)
        delta = stats.diff(before)
        print(f"{name:6s} {delta} -> {diagnose(delta)}")

    # 关键比值：回表行数 / 索引读行数，接近 1 说明几乎每行都回表
    stats = HandlerStats()
    index_scan_with_lookup(stats, 1000)
    ratio = stats.rnd / stats.next
    print(f"回表比 {ratio:.0%}；把 SELECT * 改成只取索引列可降到 0")
```

**追问一**：`Handler_read_rnd_next` 很高，但 `EXPLAIN` 显示走了索引，怎么解释？
→ 解析：`EXPLAIN` 只描述访问路径，不保证没有额外扫。常见原因：① 索引失效后退化成全表扫，但你看的是旧计划；② 子查询/派生表被物化后全表读；③ `ORDER BY` 无法用索引导致 filesort 读全量；④ 统计信息过期让优化器在运行时选了另一条路径。要用 `EXPLAIN ANALYZE` 的实际行数与 `Handler` 增量对齐，而不是只看 `type` 列。

**追问二**：为什么不能直接用 `Handler_read_rnd` 的绝对值判断"回表太多"？
→ 解析：它是实例级累计值，包含所有库表、所有连接，且随重启归零。绝对值没有分母，无法区分"业务量涨了"和"单行成本变高"。必须做时间窗口差值，再除以 `Innodb_rows_read` 或 QPS 得到**每行读放大**，才有可比性。
