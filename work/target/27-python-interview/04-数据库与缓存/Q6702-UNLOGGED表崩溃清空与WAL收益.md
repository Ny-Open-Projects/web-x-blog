---
title: "[Q6702] UNLOGGED 表崩溃清空：临时数据的 WAL 收益与陷阱"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6702 · UNLOGGED 表崩溃清空：临时数据的 WAL 收益与陷阱

难度：P6 ｜ 标签：事故复盘、PostgreSQL、UNLOGGED、可重算数据

基线：Python 3.12；PostgreSQL 12+；sqlite3 标准库演示幂等重建逻辑。

**问**：ETL 流水线把中间结果表改成了 `UNLOGGED` 表，写入快了不少。一次主库意外重启后，这张表空了，但业务表都完好。为什么只有它没了？这种模式能用在哪、不能用在哪？

**答**：
- **结论**：`UNLOGGED` 表的数据变更不写 WAL，因此崩溃或非正常关闭后 PostgreSQL 会自动把它 `TRUNCATE`（数据全丢），但表结构仍在、重启后可继续用。它换来的是写入吞吐提升（省掉 WAL 记录与刷盘）和更少的 WAL 体积。另一个隐蔽陷阱：UNLOGGED 表的变更不通过 WAL 传播，备库上这张表**结构存在但数据始终为空**，一旦切主，依赖它的数据就消失。
- **取舍**：只放"可从源头重算、丢了能重建"的数据——ETL 暂存、会话级中间表、可重建的聚合缓存。绝不能放不可再生的业务事实、用户产生内容、唯一凭证。判断标准是"这张表清空后，能否用一个确定性作业原样重建"。
- **实战**：给 UNLOGGED 表命名加 `stage_`/`tmp_` 前缀并登记在案；重启/切主后的恢复流程必须包含"重建中间表"步骤且做成幂等（代码演示）；监控里把这类表标记为非持久资产，避免被误当权威数据源。

```python
import sqlite3


def ensure_intermediate(conn: sqlite3.Connection, watermark: int) -> int:
    """模拟 UNLOGGED 中间表崩溃后的幂等重建：水位不足则从源头重算。"""
    conn.execute(
        "CREATE TABLE IF NOT EXISTS stage (id INTEGER PRIMARY KEY, v INTEGER)"
    )
    have = conn.execute("SELECT COALESCE(MAX(id), 0) FROM stage").fetchone()[0]
    if have < watermark:
        conn.execute("DELETE FROM stage")
        conn.executemany(
            "INSERT INTO stage(id, v) VALUES (?, ?)",
            [(i, i * i) for i in range(1, watermark + 1)],
        )
        conn.commit()
        return watermark - have
    return 0


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    print("first build rows:", ensure_intermediate(conn, 5))
    print("stage count:", conn.execute("SELECT COUNT(*) FROM stage").fetchone()[0])
    conn.execute("DELETE FROM stage")  # 模拟崩溃重启后 UNLOGGED 表被清空
    conn.commit()
    print("rebuild rows:", ensure_intermediate(conn, 5))
    print("stage count:", conn.execute("SELECT COUNT(*) FROM stage").fetchone()[0])
```

**追问一**：为什么 UNLOGGED 表在备库上是空的？
→ 解析：物理复制依赖 WAL，UNLOGGED 表不产生 WAL 记录，备库拿不到数据变更，所以只有 DDL（结构）被复制。切主前必须先重建，否则读到空表。

**追问二**：UNLOGGED 表和临时表（`CREATE TEMP TABLE`）有什么区别？
→ 解析：临时表是会话级、会话结束即消失且对其他会话不可见；UNLOGGED 表是持久对象、跨会话共享，只是不写 WAL、崩溃后清空。
