---
title: [Q1682] 批量 upsert 冲突分支: DO NOTHING 与 DO UPDATE
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1682 · 批量 upsert 冲突分支: DO NOTHING 与 DO UPDATE

> 难度:★★★☆ | 标签:SQL, upsert

**问**:一批价格数据导入,已存在的不覆盖、降价才覆盖,一条语句能做到吗?

**答**:做不到"一条语句两种动作",一条 INSERT 只能挂一个 ON CONFLICT 动作,正确做法是拆成两条:新套装 DO NOTHING,更新套 DO UPDATE 加 WHERE 条件,让冲突更新只在满足业务条件(如降价)时生效,excluded 引用待插入的新值与表内旧值比较。SQLite 有个语法陷阱:INSERT 的数据源是 SELECT 时必须在 SELECT 里写 WHERE true,否则解析器会把 ON 当成 JOIN 条件报语法错。rowcount 只统计实际变更行,幂等重跑时它自然归零,可以直接当"本次生效行数"用。

```python
# file: code/04_数据库与缓存/q1682_bulk_upsert_branch.py
"""批量 upsert 冲突分支: DO NOTHING 与 DO UPDATE 的拆分与条件"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE sku_price(sku TEXT PRIMARY KEY, price REAL, source TEXT)")
conn.executemany("INSERT INTO sku_price VALUES(?,?,?)",
                 [("A", 10.0, "erp"), ("B", 20.0, "erp"), ("C", 30.0, "erp")])
conn.commit()

feed = [("A", 11.0, "feed"), ("B", 19.0, "feed"), ("D", 5.0, "feed")]
conn.execute("CREATE TEMP TABLE feed(sku TEXT PRIMARY KEY, price REAL, source TEXT)")
conn.executemany("INSERT INTO feed VALUES(?,?,?)", feed)

# 分支一: 只新增不覆盖 -> DO NOTHING
n_ins = conn.execute("""
  INSERT INTO sku_price(sku, price, source)
  SELECT sku, price, source FROM feed WHERE true
  ON CONFLICT(sku) DO NOTHING""").rowcount
print("DO NOTHING 实际插入:", n_ins, "行 (只有 D; 注意 INSERT 源是 SELECT 时必须写 WHERE true)")

# 分支二: 只覆盖降价 -> DO UPDATE 带条件
n_upd = conn.execute("""
  INSERT INTO sku_price(sku, price, source)
  SELECT sku, price, source FROM feed WHERE true
  ON CONFLICT(sku) DO UPDATE SET price = excluded.price, source = excluded.source
  WHERE excluded.price < sku_price.price""").rowcount
print("条件 DO UPDATE 生效:", n_upd, "行 (B 降价被更新, A 涨价被 WHERE 挡住)")
print("最终:", conn.execute("SELECT * FROM sku_price ORDER BY sku").fetchall())
print("要点: 一条 INSERT 只能挂一个冲突动作, 新增与更新分支要拆成两条语句;")
print("      rowcount 只统计实际变更行, 幂等重跑时天然为 0")
```

**追问**:
- MySQL 的等价写法?——INSERT ... ON DUPLICATE KEY UPDATE price=VALUES(price) 配合应用层判断,或 INSERT IGNORE 做分支一;MySQL 8.0.20 起 VALUES() 建议改用别名行。
- 两条语句之间有原子性问题吗?——同事务里先后执行就是原子的;分两个事务则要接受中间态或先落 staging 表。

---
