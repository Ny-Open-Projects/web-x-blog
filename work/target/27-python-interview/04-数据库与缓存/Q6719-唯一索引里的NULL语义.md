---
title: "[Q6719] 唯一索引里的 NULL：唯一约束并不总是唯一"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6719 · 唯一索引里的 NULL：唯一约束并不总是唯一

难度：P6 ｜ 标签：唯一索引、NULL 语义、数据质量、幂等

基线：Python 3.12 + sqlite3（3.40+）；MySQL 8.0 / PostgreSQL 15 语义对照。

**问**：用户表给 `phone` 加了唯一索引，上线后发现同一批"手机号为空"的导入数据进了 300 条重复记录，唯一索引完全没拦住。唯一约束不是应该保证不重复吗？为什么 NULL 能绕过？

**答**：
- **结论**：SQL 标准里 `NULL` 表示"未知"，两个 NULL 不相等，所以唯一索引允许**多行 NULL**（MySQL、PostgreSQL 默认、SQLite 都是这个语义）。唯一约束保证的是"非 NULL 值不重复"，不是"每一行都唯一"。业务上"手机号为空"往往代表"尚未填写"，多行空值是合法的；但如果业务要求"空也只能有一条"，唯一索引本身给不了。
- **取舍**：三种治理方式：① 应用层把"空"归一成一个**非空哨兵值**（如 `__missing__:{uuid}`）再写入，唯一索引才生效；② PostgreSQL 15+ 用 `UNIQUE NULLS NOT DISTINCT`，让 NULL 之间也互斥；③ 用部分唯一索引/触发器只约束"需要唯一的子集"。哨兵值简单但污染数据语义；`NULLS NOT DISTINCT` 最干净但版本受限；触发器在并发下不可靠。
- **实战**：① 建唯一索引前先问"这一列的空值业务含义是什么"，别假设唯一约束等于业务唯一；② 用 `SELECT col, COUNT(*) ... GROUP BY col HAVING COUNT(*)>1` 做数据质量巡检，NULL 要单独统计；③ 幂等表的主键/唯一键避免可空列；④ 迁移到 PG 15+ 时评估 `NULLS NOT DISTINCT` 对现有数据的影响（可能立刻暴露重复 NULL）。

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, phone TEXT UNIQUE)")
conn.executemany("INSERT INTO users(phone) VALUES (?)", [(None,), (None,), ("13800000000",)])
print("NULL 行数:", conn.execute(
    "SELECT COUNT(*) FROM users WHERE phone IS NULL").fetchone()[0])

try:
    conn.execute("INSERT INTO users(phone) VALUES ('13800000000')")
except sqlite3.IntegrityError as exc:
    print("非 NULL 重复被拦:", exc)

# 方案：用生成列把 NULL 归一为非空哨兵，再对它建唯一索引
conn.execute("""CREATE TABLE users2 (
    id INTEGER PRIMARY KEY,
    phone TEXT,
    phone_key TEXT GENERATED ALWAYS AS (COALESCE(phone, '__NULL__')) STORED,
    UNIQUE(phone_key))""")
conn.execute("INSERT INTO users2(phone) VALUES (NULL)")
try:
    conn.execute("INSERT INTO users2(phone) VALUES (NULL)")
except sqlite3.IntegrityError:
    print("哨兵方案：第二条 NULL 被唯一索引拦住")
```

**追问一**：为什么 `WHERE phone <> '13800000000'` 查不到 phone 为 NULL 的行？
→ 解析：任何与 NULL 的比较结果都是 UNKNOWN，不是 TRUE，所以该行不满足过滤条件。要包含 NULL 必须写 `phone IS NULL OR phone <> ...`，或 `COALESCE(phone,'') <> ...`。NULL 的"未知"语义会同时影响唯一约束、聚合（`COUNT(phone)` 不计 NULL）和索引选择。

**追问二**：MySQL 里复合唯一索引 `(tenant_id, phone)`，phone 为 NULL 时能插入多少条同租户记录？
→ 解析：只要复合键里有 NULL，整个键就被视为"含未知"，唯一性检查不生效，可以插入任意多条。若业务要求"同租户下空手机号只能一条"，必须把 phone 归一为非空值，或改用可空列上的函数索引/生成列。
