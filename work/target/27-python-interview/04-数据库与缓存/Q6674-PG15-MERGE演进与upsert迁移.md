---
title: [Q6674] PG15 MERGE 语句演进与 upsert 迁移
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6674 · PostgreSQL 15 MERGE 语句：与 ON CONFLICT 的分界

难度：P6 ｜ 标签：版本演进、PostgreSQL、upsert
基线：PostgreSQL 15+（MERGE 语法）；代码用 sqlite3 演示等价逻辑，任何环境可运行。

**问**：PG 15 引入标准 `MERGE` 语句。它和 9.5 就有的 `INSERT ... ON CONFLICT`（upsert）是什么关系？什么时候必须用 MERGE？迁移中要注意什么？

**答**：**结论**：两者解决不同层次的问题。`ON CONFLICT` 只做"冲突时 upsert 单表"，语义窄但优化好、并发安全；`MERGE` 是标准 SQL 的"源表到目标表的条件合并"，支持 WHEN MATCHED / NOT MATCHED / 源侧过滤、UPDATE/DELETE/INSERT 三分支，还能基于 join 条件（不只唯一约束）决定行为。**凡是有"不匹配时删除/更新旧数据"或"匹配条件不是唯一键"的同步场景，ON CONFLICT 表达不了，就得 MERGE**。

**取舍**：MERGE 的坑：① 并发下两个 MERGE 同时匹配同一行可能抛唯一约束错误（PG15 的 MERGE 不自动串行化），高并发 upsert 仍推荐 ON CONFLICT；② MERGE 需要 CTE 或 RETURNING 才能统计各分支行数，审计逻辑要自己写。ON CONFLICT 的坑：`DO NOTHING` 会跳过所有冲突（要 `ON CONFLICT (col) DO NOTHING` 指定目标），且没有 NOT-MATCHED-删除语义。

**实战**：同步类任务（每日全量对齐）用 MERGE；高并发计数/库存类单行 upsert 用 ON CONFLICT。PG 15 以下或 MySQL 环境降级方案：`DELETE + INSERT` 在一个事务里，或先 UPDATE 再 INSERT 的两段式（注意窗口期）。

```python
# 用 sqlite3 演示 MERGE 三分支语义（UPDATE/INSERT/DELETE 各算各的账）
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE target (sku TEXT PRIMARY KEY, price INT, active INT);
CREATE TABLE source (sku TEXT PRIMARY KEY, price INT, del INT);
INSERT INTO target VALUES ('a', 10, 1), ('b', 20, 1), ('c', 30, 1);
INSERT INTO source VALUES ('a', 11, 0),   -- 匹配 -> UPDATE
                          ('d', 40, 0),   -- 不匹配 -> INSERT
                          ('c', 30, 1);   -- 源标记删除 -> DELETE
""")

# MERGE 语义的手工等价实现：三分支分别计数（迁移到 PG15 后可用原生 MERGE 统计）
cur = conn.cursor()
cur.execute("ATTACH ':memory:' AS src") if False else None

matched_update = matched_delete = not_matched_insert = 0
for sku, price, deleted in cur.execute("SELECT sku, price, del FROM source"):
    row = cur.execute(
        "SELECT 1 FROM target WHERE sku = ?", (sku,)).fetchone()
    if row:                      # WHEN MATCHED
        if deleted:
            cur.execute("DELETE FROM target WHERE sku = ?", (sku,))
            matched_delete += 1
        else:
            cur.execute(
                "UPDATE target SET price = ? WHERE sku = ?", (price, sku))
            matched_update += 1
    else:                        # WHEN NOT MATCHED
        if not deleted:
            cur.execute(
                "INSERT INTO target VALUES (?, ?, 1)", (sku, price))
            not_matched_insert += 1

print("update:", matched_update, "insert:", not_matched_insert,
      "delete:", matched_delete)
# -> update: 1 insert: 1 delete: 1
print(list(cur.execute("SELECT * FROM target ORDER BY sku")))
# -> [('a', 11, 1), ('b', 20, 1), ('d', 40, 1)]

# 对照：ON CONFLICT 版本（只能覆盖 UPDATE+INSERT，表达不了 DELETE 分支）
cur.execute("""INSERT INTO target (sku, price, active) VALUES ('a', 99, 1)
               ON CONFLICT(sku) DO UPDATE SET price = excluded.price""")
print(cur.execute("SELECT price FROM target WHERE sku='a'").fetchone())
```

**追问 1**：并发两个 MERGE 合并同一行会发生什么？
提示：可能其中一个在写入时撞上唯一约束或行锁等待；MERGE 不提供 upsert 那样的"重试即成功"语义，高并发场景要加锁或退回 ON CONFLICT。

**追问 2**：MERGE 里 WHEN MATCHED AND source.price < target.price 这种条件分支有什么用？
提示：条件合并（只降价不涨价、只更新变化行），这是 ON CONFLICT 完全做不到的，也是同步任务里减少写放大的关键手段。

**追问 3**：把 MySQL 的 `INSERT ... ON DUPLICATE KEY UPDATE` 迁移到 PG 要注意什么？
提示：MySQL 的语义是 insert-or-update 二分，没有 delete 分支；且 MySQL 会对所有唯一键冲突生效，PG 必须显式指定冲突目标 `(col)`，迁移时漏指定会直接报错。

## 背诵要点
1. ON CONFLICT = 单行并发安全 upsert；MERGE = 源表条件合并，支持 UPDATE/INSERT/DELETE 三分支与非唯一键匹配。
2. 高并发计数用 ON CONFLICT，每日同步/对账用 MERGE；PG15 MERGE 并发不自动串行化。
3. ON CONFLICT 必须显式指定冲突目标，DO NOTHING 裸写会吞掉所有唯一键冲突。

## 复盘追问
1. 你的同步任务里有没有"源删除了目标也要删"的需求？现在是怎么实现的（硬删、软删标记还是对账修复）？
2. 如果 MERGE 执行到一半报错，目标表是什么状态？你如何保证同步任务的原子性？
