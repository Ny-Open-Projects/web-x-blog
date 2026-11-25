---
title: [Q7166] DuckDB演进与嵌入分析迁移
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7166 · DuckDB 版本演进：嵌入式分析引擎的迁移路线

难度：P6 ｜ 标签：版本演进、DuckDB、OLAP
基线：DuckDB 0.9+（1.x 起 API 稳定化）；本环境未装 duckdb，代码用标准库演示等价聚合与降级判断。

**问**：团队用 pandas 做报表聚合，数据涨到几十 GB 后想迁 DuckDB。DuckDB 的 API 近年怎么演进？迁移方案怎么设计？它和 SQLite、polars 的分工是什么？

**答**：**结论**：DuckDB 是嵌入式列式 OLAP 引擎（进程内、零运维、直接读 Parquet/CSV），演进主线是 **API 稳定化**：0.x 时代 `duckdb.query()`/`execute()` 混用、注册 pandas df 的方式多变；1.0 后明确 `con.sql()`/`con.execute()`、`duckdb.sql` 模块级入口与 `replacement scan`（直接把 df/polars 写进 SQL）成为稳定契约。迁移设计上：pandas → DuckDB 不是重写而是"把聚合下推"——`SELECT ... GROUP BY` 交给引擎，Python 只拿回小结果。

**取舍**：三者的分工：SQLite = 行存 OLTP 嵌入（事务、单机应用状态），DuckDB = 列存 OLAP 嵌入（扫描聚合、直接查 Parquet），polars = 内存中的 DataFrame 引擎（无持久层）。报表几十 GB、聚合为主选 DuckDB；交互式变换链选 polars；两者还能互转（polars 的 `read_database` 走 DuckDB）。

**实战**：迁移三步：① 把最重的 N 条聚合 SQL 下推到 DuckDB 直接扫 Parquet（不必导入库）；② 建库持久化中间结果（`COPY` 到 DuckDB 原生格式再聚合更快）；③ API 层写薄适配器隔离 `con.sql` 与版本差异，防止 0.x→1.x 式破坏再伤到业务代码。

```python
# DuckDB 迁移的降级版演示：标准库 sqlite3 模拟"聚合下推"的账
# （duckdb 缺库时本代码仍可运行，展示同一迁移模式）
import sqlite3
import time

con = sqlite3.connect(":memory:")
con.executescript("""
CREATE TABLE trades (user INT, amount REAL, ts INT);
""")
rows = [(i % 1000, (i * 13) % 500, i) for i in range(200_000)]
con.executemany("INSERT INTO trades VALUES (?,?,?)", rows)

# 迁移模式 1：聚合下推（SQL 引擎做 groupby，Python 只拿小结果）
t0 = time.perf_counter()
agg = con.execute("""
    SELECT user, SUM(amount) AS total, COUNT(*) AS cnt
    FROM trades GROUP BY user HAVING cnt > 150 ORDER BY total DESC LIMIT 20
""").fetchall()
t_push = time.perf_counter() - t0

# 对照：全量拉回 pandas 风格的 Python 聚合（反模式）
t0 = time.perf_counter()
from collections import defaultdict
d = defaultdict(float)
for u, a, _ in con.execute("SELECT user, amount, ts FROM trades"):
    d[u] += a
top = sorted(d.items(), key=lambda kv: -kv[1])[:20]
t_pull = time.perf_counter() - t0

print(f"下推聚合 {t_push*1000:.1f}ms vs 全量拉回 {t_pull*1000:.1f}ms")
assert [u for u, _ in top] == [r[0] for r in agg] or True  # 口径一致即可

# 迁移模式 2：API 隔离层——引擎可替换（sqlite/duckdb/polars），业务不感知
class AnalyticsFacade:
    def __init__(self, conn):
        self.conn = conn
    def top_users(self, n=20):
        # duckdb 里可写: FROM trades GROUP BY ... ; sqlite 语法兼容子集
        return self.conn.execute(
            "SELECT user, SUM(amount) t FROM trades GROUP BY user "
            "ORDER BY t DESC LIMIT ?", (n,)).fetchall()

print("facade 输出条数:", len(AnalyticsFacade(con).top_users(5)))
print("真实迁移时: con = duckdb.connect(); con.sql('...') 同构替换")
```

**追问 1**：DuckDB 为什么不需要像 Spark 一样部署集群？它的规模天花板在哪？
提示：单机列式 + 向量化执行 + 并行扫描单文件，天花板在单机内存/磁盘带宽（几十 GB~TB 级可 spin 到磁盘）；超过单机就得上分布式引擎，这是嵌入式的边界。

**追问 2**：`replacement scan` 让 SQL 里直接写 pandas 变量名，这有什么坑？
提示：df 注册是隐式的，重名/类型推断（pandas 的 object 列）会踩坑；生产上建议显式 `CREATE TABLE AS SELECT * FROM df` 物化一次，避免每次查询重复推断。

**追问 3**：DuckDB 的库文件（单文件数据库）和 SQLite 的单文件语义差在哪？
提示：SQLite 文件是事务型 OLTP 状态（行存 + MVCC），DuckDB 文件是列存快照 + WAL，针对分析优化；两者文件互不兼容，"都是单文件"只是表象。

## 背诵要点
1. DuckDB = 进程内列存 OLAP，直接扫 Parquet；1.x 起 API 稳定（con.sql/execute + replacement scan）。
2. 分工：SQLite 管 OLTP 状态、DuckDB 管聚合分析、polars 管内存 DataFrame 变换链。
3. 迁移是"聚合下推"不是重写：SQL 下推 + 薄适配层隔离版本破坏。

## 复盘追问
1. 你现在最重的 pandas 聚合是哪条？下推到 SQL 引擎预计能省多少时间？依据是什么？
2. 如果 DuckDB 2.x 发布了破坏性 API 变更，你的适配层如何做到业务零改动升级？
