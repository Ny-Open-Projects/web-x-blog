---
title: [Q1070] Polars lazy 与 DuckDB 组合
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1070 · Polars lazy 与 DuckDB 组合

> 难度:★★★★ | 标签:Polars, DuckDB, 性能

**问**:pandas 之外,现在的"大表轻分析"黄金组合是什么?lazy 到底省在哪?

**答**:两条路线:Polars 的 lazy API 先构建查询计划,执行时做谓词/投影下推与并行化,只物理读取需要的列和行,内存与 CPU 都省;DuckDB 用 SQL 直接查询 CSV/Parquet,零拷贝列读取,交互分析几乎零成本。工程组合:DuckDB 负责"SQL 快查与聚合下推",结果转 pandas/Polars 做精细加工;定时大批量转换用 Polars lazy 跑批。选型口诀:交互问数用 DuckDB,批量 ETL 用 Polars,pandas 留给生态依赖和最终展示。

```python
# file: code/05_数据分析与工程化/q1070_lazy_engines.py
import csv
import os
import tempfile

path = os.path.join(tempfile.gettempdir(), "q1070_events.csv")
if not os.path.exists(path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["city", "amount"])
        for i in range(20000):
            w.writerow([f"c{i % 4}", i % 100])

used = "stdlib"
try:
    import polars as pl
    used = "polars"
    res = (
        pl.scan_csv(path)
        .group_by("city")
        .agg(pl.col("amount").sum().alias("total"))
        .sort("city")
        .collect()
    )
    print(res)
except ImportError:
    try:
        import duckdb
        used = "duckdb"
        print(duckdb.sql(f"SELECT city, sum(amount) AS total FROM read_csv_auto('{path}') GROUP BY city ORDER BY city"))
    except ImportError:
        from collections import defaultdict
        agg = defaultdict(int)
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                agg[row["city"]] += int(row["amount"])
        for k in sorted(agg):
            print(k, agg[k])
print("引擎:", used, "- lazy 计划把过滤与投影下推到数据源,避免全量进内存")
```

**追问**:
- 追问 1:lazy 计划什么时候真正执行?—— 调用 `collect()` 时;之前只是构建计划,可先 `explain()` 查看下推效果。
- 追问 2:DuckDB 查 Parquet 为什么快?—— 列存按需读列,行组统计让谓词直接剪枝,无反序列化开销。
