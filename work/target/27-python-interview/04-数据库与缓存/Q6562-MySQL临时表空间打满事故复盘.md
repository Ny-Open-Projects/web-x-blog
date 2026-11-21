---
title: "[Q6562] MySQL 内部临时表空间打满事故复盘"
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6562 · MySQL 内部临时表空间打满事故复盘

难度：P6 ｜ 标签：MySQL / 临时表 / 排序 / 事故复盘

**问**：一条带大 GROUP BY 的报表 SQL 在夜里把 MySQL 磁盘写满，`ibtmp1` 涨到几百 GB，同实例所有写入报磁盘满错误。复盘：内部临时表为什么能涨这么大？怎么定位与治理？

**答**：

**结论**：MySQL 执行 GROUP BY / DISTINCT / ORDER BY（无索引可用）时若内存临时表（`temptable` 引擎或 memory 引擎，受 `tmp_table_size`/`max_heap_table_size` 限制）放不下，会转为磁盘临时表。8.0 的共享临时表空间 `ibtmp1` 只增不缩（重启才回收），多个并发大查询叠加就能把磁盘写满，殃及整个实例的写入。

**取舍**：三个治理层次——① 语句层：给 GROUP BY/ORDER BY 列建索引让它走索引避免物化临时表；实在不行用 `SQL_BIG_RESULT` 提示走排序而非临时表。② 实例层：把 `internal_tmp_mem_storage_engine`、`temptable_max_ram` 调大能延缓落盘但不能根治；8.0.16+ 可用 `GLOBAL TEMPORARY TABLESPACE` 独立盘。③ 架构层：报表流量打到从库或专用分析实例（如 ClickHouse/DuckDB），这是最终解。

**实战**：定位看 `EXPLAIN` Extra 列的 `Using temporary; Using filesort`、`information_schema.INNODB_SESSION_TEMP_TABLESPACES` 的体积列，以及 performance_schema 里 `SORT/MERGE_PASS`。应急是 kill 大查询 + 重启回收 ibtmp；预防是报表 SQL 上线前过 explain 门禁 + 报表库隔离。Python 侧要做的是：给报表类查询加独立超时与 `max_execution_time` hint，而不是让它无限跑。

```python
# 估算一条 GROUP BY 的临时表在内存/磁盘之间的边界与磁盘增长
# 仅标准库，Python 3.9+
from __future__ import annotations

ROW_FIXED_BYTES = 64  # 每行定长开销（估算）


def temp_table_size_bytes(rows: int, group_keys: int, row_width: int) -> int:
    """粗估内部临时表体积：分组行数 × 行宽。"""
    # 分组数上限受基数限制，这里假设每个分组平均 10 行原始数据
    distinct_groups = min(rows, group_keys)
    return distinct_groups * (ROW_FIXED_BYTES + row_width)


def plan_query(rows: int, group_keys: int, row_width: int,
               mem_limit_bytes: int) -> dict[str, object]:
    size = temp_table_size_bytes(rows, group_keys, row_width)
    spill = size > mem_limit_bytes
    return {
        "temp_size_mb": round(size / 1024 / 1024, 1),
        "in_memory": not spill,
        "disk_overflow_mb": round((size - mem_limit_bytes) / 1024 / 1024, 1) if spill else 0,
    }


def main() -> None:
    # 报表 SQL：按 user_id 聚合 3 个月订单，1 亿行、800 万个分组、行宽 120B
    r = plan_query(rows=100_000_000, group_keys=8_000_000,
                   row_width=120, mem_limit_bytes=64 * 1024 * 1024)
    print(r)
    assert not r["in_memory"], "应溢出到磁盘临时表"
    assert r["disk_overflow_mb"] > 800, "磁盘临时表应有 GB 级溢出"

    # 优化 1：把行宽砍到 24B（只选必要列）
    r2 = plan_query(100_000_000, 8_000_000, 24, 64 * 1024 * 1024)
    # 优化 2：预聚合表把分组数降到 50 万（配合 128MB 内存临时表限额）
    r3 = plan_query(100_000_000, 500_000, 120, 128 * 1024 * 1024)
    print("瘦列:", r2["disk_overflow_mb"], "MB 溢出; 预聚合:", r3["in_memory"])
    assert r2["disk_overflow_mb"] < r["disk_overflow_mb"]
    assert r3["in_memory"], "预聚合后应留在内存临时表"


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么 `ibtmp1` 涨上去不自动缩？临时文件不是该会话结束就删吗？——会话私有临时文件（8.0 的 session temp）会删，但共享 ibtmp 空间按历史峰值保留扩展后的大小，重启实例才收缩；所以磁盘告警恢复后盘面也不会自己回来。
- 追问 1.1：PG 有没有同类问题？——PG 用每个会话独立的临时文件（`temp_file_limit` 可限），不会共享膨胀，但会把 `temp_blks_written` 打爆 IO；排查口径换成 `log_temp_files`。
- 追问 2：`SQL_BIG_RESULT` 和 `SQL_SMALL_RESULT` 各自让优化器怎么选？——BIG_RESULT 倾向排序（sort）而非物化临时表，适合分组数多的情况；SMALL_RESULT 倾向先建临时表，适合分组数少能放进内存的场景。

**背诵要点**：

1. 内部临时表超过 tmp_table_size/temptable_max_ram 就落盘；8.0 共享 ibtmp1 只增不缩，重启才回收，磁盘满会拖垮全实例写入。
2. 判据：EXPLAIN 的 `Using temporary; Using filesort` + INNODB_SESSION_TEMP_TABLESPACES 体积；应急 kill + 重启。
3. 治理优先级：建索引避免物化 > 瘦列/预聚合降行数 > 报表隔离到专用实例；SQL 侧加 max_execution_time。

**复盘追问**：

1. 如果磁盘满当晚 ibtmp 正在涨，你的分钟级应急处置顺序是什么（先 kill 还是先清盘）？
2. 如何在上线前门禁里自动拦截"会落磁盘临时表"的报表 SQL？
