---
title: [Q334] DuckDB 嵌入式分析
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q334 · DuckDB 嵌入式分析

> 难度:★★★ | 标签:DuckDB, SQL

**问**:DuckDB 是什么?相比 pandas 和传统 OLAP 库的优势在哪?

**答**:DuckDB 是嵌入式 OLAP 数据库,像 SQLite 一样进程内运行、零部署,却支持完整 SQL、列式执行、直接查询 parquet/CSV/pandas DataFrame,还能与 pandas 互转。定位:介于 pandas(单机内存、Python API)与 Spark(分布式、重运维)之间,适合单机 GB~百 GB 级分析、本地数仓探查、给数据管道加 SQL 层。优势是"不把数据拉进内存也能算"——可以流式扫描大 parquet 并只物化结果,内存占用远低于 pandas 全量加载。

```python
# file: code/05_数据分析与工程化/q334_duckdb_sql.py
import csv
import os

def write_csv(path):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["city", "amt"])
        for city, amt in [("BJ", 10), ("SH", 20), ("BJ", 30)]:
            w.writerow([city, amt])

if __name__ == "__main__":
    path = "demo_duck.csv"
    write_csv(path)
    try:
        import duckdb
        con = duckdb.connect()                 # 进程内,零部署
        out = con.execute(
            "SELECT city, sum(amt) AS total "
            "FROM read_csv_auto(?) GROUP BY city ORDER BY total DESC",
            [path],
        ).fetchall()
        print(out)
        con.close()
    except ImportError:
        # 降级:纯标准库实现同样语义
        groups = {}
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                groups[row["city"]] = groups.get(row["city"], 0) + float(row["amt"])
        print(sorted(groups.items(), key=lambda kv: -kv[1]))
    os.remove(path)
```

**追问**:
- DuckDB 能直接查 pandas 对象吗?可以,`duckdb.query("SELECT * FROM df")` 会用 Arrow 桥接零拷贝扫描 DataFrame,常用于给 pandas 管道补 SQL 能力。
- DuckDB 为什么「不把数据拉进内存也能算」?——列式 + 向量化执行,扫描 parquet 流式聚合,只物化最终结果;pandas 必须先全量进内存。
- 什么时候 DuckDB 替代 pandas?——GB 级数据、SQL 逻辑复杂、内存吃紧;单表小清洗继续 pandas 更顺手。
- 它和 Spark 怎么分工?——单机到百 GB 内 DuckDB(零运维);跨机、TB 级、需要分布式调度才上 Spark。
