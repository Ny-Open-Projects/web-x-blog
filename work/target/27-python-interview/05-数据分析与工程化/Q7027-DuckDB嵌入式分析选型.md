---
title: [Q7027] DuckDB 嵌入式分析选型
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7027 · DuckDB 嵌入式分析：什么时候用 DuckDB 而不是 pandas/Polars？

> 难度:★★★ | 标签:DuckDB, SQL, 数据分析

**问**：一个单机数据分析任务：几个 GB 的 CSV/Parquet 要做 join、窗口函数、聚合。用 pandas 内存吃紧、写 SQL 手工优化累。DuckDB 解决了什么问题？边界在哪？

**答**：结论：DuckDB 是**进程内 OLAP 引擎**——把列式向量化执行 + 完整 SQL（含窗口函数、join、 spill-to-disk）嵌进 Python。它取三者之长：比 pandas 省内存（向量化 + 磁盘溢写，几十 GB 数据单机可算）、比手写 SQL 轻松（标准 SQL 而不是 pandas API 拼积木）、比起一个数据库服务省事（`import duckdb` 即用，零部署）。选型信号：**分析型（全表扫描聚合）+ 单机数据量（GB 级）+ 需要复杂 SQL**；高并发写入、事务语义、多服务共享数据是它的边界——那是 PostgreSQL 的事。

机理与实战：
- 读取路径是其核心优势：`duckdb.sql("SELECT ... FROM 'data/*.parquet'")` 直接查文件，不加载进 Python；配合 `register()` 把 pandas/Arrow 表零拷贝喂给 SQL。pandas 组合拳：pandas 做小结果集的后处理，DuckDB 做重计算。
- 内存行为：DuckDB 有 `memory_limit` 与临时目录配置，超限自动 spill 到磁盘——这是 pandas 做不到的（pandas 只能 OOM 或靠你手动分块）。但"溢写"不是免费的，join 大表仍建议先过滤裁剪列（`SELECT` 只取需要的列，DuckDB 列存裁剪天然友好）。
- 与 Polars 的分工：Polars 强在 DataFrame API 的多核向量化、惰性优化，适合"管道式"处理；DuckDB 强在 SQL 表达复杂关系逻辑（窗口、多表 join）。两者可混用（Arrow 为桥），团队以 SQL 文化为主选 DuckDB，以链式转换为主选 Polars。

```python
# 基线:Python 3.9+ / duckdb 0.9+ ;缺库降级:纯标准库演示查询下推思想
try:
    import duckdb
    HAS_DUCK = True
except ImportError:
    HAS_DUCK = False


def demo_duck() -> None:
    import os, tempfile
    tmp = tempfile.mkdtemp()
    duckdb.sql("CREATE TABLE events (uid INT, ts TIMESTAMP, amount DOUBLE)")
    duckdb.sql("""INSERT INTO events SELECT i % 100, now(), i * 1.5
                  FROM range(100000) t(i)""")
    # 重计算全在 DuckDB 内完成,Python 只接结果(内存=结果集大小)
    top = duckdb.sql("""
        SELECT uid, sum(amount) AS total,
               row_number() OVER (ORDER BY sum(amount) DESC) AS rk
        FROM events GROUP BY uid LIMIT 5
    """).fetchall()
    print("窗口函数 Top5:", top)
    # 直接查文件:零加载分析
    path = f"{tmp}/events.parquet"
    duckdb.sql(f"COPY events TO '{path}'")
    cnt = duckdb.sql(f"SELECT count(*) FROM '{path}' WHERE amount > 100000").fetchone()
    print("文件直查行数:", cnt[0])


def demo_stdlib() -> None:
    """缺库降级:演示"下推过滤/裁剪列"的内存思想。"""
    rows = ({"uid": i % 100, "amount": i * 1.5} for i in range(100000))
    # 全量物化 vs 下推聚合:下推把 10 万行压成 100 行再回 Python
    agg: dict[int, float] = {}
    for r in rows:
        if r["amount"] > 100000:            # 过滤下推
            agg[r["uid"]] = agg.get(r["uid"], 0) + r["amount"]
    print("下推后回传行数:", len(agg))


if __name__ == "__main__":
    demo_duck() if HAS_DUCK else demo_stdlib()
```

**追问一**：DuckDB 单写者限制对"边写边查"的报表应用意味着什么？
答：DuckDB 文件是单进程独占写，多进程并发写会锁冲突；它的定位是"分析时计算"而不是"在线服务的数据库"。需要多进程读写就上 PostgreSQL/ClickHouse，DuckDB 适合 job/notebook/嵌入式分析场景。

**追问二**：几个 GB 的 join 在 DuckDB 里怎么调优？
答：先裁剪（只 select 需要的列、尽早 WHERE 过滤），必要时 `PRAGMA memory_limit='4GB'` + `temp_directory` 明确溢写路径；join 顺序交给优化器但可以用 `PRAGMA enable_profiling` 看 hash join 是否磁盘溢出，溢出严重就先物化小表做 semi-join 预过滤。

**背诵要点**：
- DuckDB = 进程内 OLAP：列存向量化 + 完整 SQL + 磁盘溢写，GB 级单机分析首选。
- 文件直查（parquet/csv glob）+ register 零拷贝桥接 pandas/Arrow 是核心优势。
- 边界：单写者、无事务语义多服务共享；在线高并发库用 PG/ClickHouse。

**复盘追问**：
- "pandas 后处理 + DuckDB 重计算"的分工边界怎么定才不出现两边都做一半？
- 与 Polars 混用时 Arrow 作为交换层的成本与陷阱？

## 背诵要点
- 选型信号：分析型负载、GB 级单机、SQL 复杂逻辑 → DuckDB。
- memory_limit + spill 使其能算超内存数据，pandas 无此能力。
- 查询调优三步：裁列、早过滤、看 profiler 定位 join 溢写。

## 复盘追问
- DuckDB 的持久化文件（.duckdb）在版本升级时的兼容性策略？
- 报表服务的"每次启动新连接 vs 常驻单连接"怎么选？
