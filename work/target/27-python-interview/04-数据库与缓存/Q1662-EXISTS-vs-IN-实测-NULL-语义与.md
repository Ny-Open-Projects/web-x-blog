---
title: [Q1662] EXISTS vs IN 实测: NULL 语义与代价双维度
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1662 · EXISTS vs IN 实测: NULL 语义与代价双维度

> 难度:★★★★ | 标签:SQL 调优, EXISTS

**问**:EXISTS 和 IN 到底该用哪个?有没有标准答案?

**答**:没有标准答案,要分语义与代价两个维度看。语义维度上,否定查询 NOT IN 会被子查询里的 NULL 全灭,NOT EXISTS 则完全免疫,所以否定场景 EXISTS 是硬要求;肯定场景里 IN 与 EXISTS 数学上等价。代价维度上,老教材说"外表小用 IN、外表大用 EXISTS",但现代优化器普遍能把两者改写成同一个半连接,实测才有意义;SQLite 这类以嵌套循环为主的引擎差异会真实存在,MySQL 8 与 PG 通常能拉平。本机 sqlite 实测里相关 EXISTS 比缓存的 IN 慢一个量级,说明"优化器是否做了改写"比"写法本身"更关键,结论要靠 EXPLAIN 加计时落地。

```python
# file: code/04_数据库与缓存/q1662_exists_vs_in.py
"""EXISTS vs IN 实测: NULL 语义差异与四种写法的代价"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, vip INTEGER)")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER)")
conn.executemany("INSERT INTO users VALUES(?,?)",
                 [(i, 1 if i % 10 == 0 else 0) for i in range(1, 100001)])
conn.executemany("INSERT INTO orders VALUES(?,?)",
                 [(i, (i * 7) % 50000 + 1) for i in range(1, 150001)])
conn.execute("CREATE INDEX idx_o_user ON orders(user_id)")
conn.commit()

def timed(sql, n=3):
    t0 = time.perf_counter()
    for _ in range(n):
        conn.execute(sql).fetchall()
    return (time.perf_counter() - t0) / n * 1000

q_in = ("SELECT COUNT(*) FROM users WHERE id IN "
        "(SELECT user_id FROM orders WHERE user_id <= 5000)")
q_exists = ("SELECT COUNT(*) FROM users u WHERE EXISTS "
            "(SELECT 1 FROM orders o WHERE o.user_id = u.id AND o.user_id <= 5000)")
q_not_in = "SELECT COUNT(*) FROM users WHERE id NOT IN (SELECT user_id FROM orders)"
q_not_exists = ("SELECT COUNT(*) FROM users u WHERE NOT EXISTS "
                "(SELECT 1 FROM orders o WHERE o.user_id = u.id)")
print(f"IN       半连接  : {timed(q_in):8.2f} ms")
print(f"EXISTS   半连接  : {timed(q_exists):8.2f} ms")
print(f"NOT IN   反连接  : {timed(q_not_in):8.2f} ms")
print(f"NOT EXISTS 反连接: {timed(q_not_exists):8.2f} ms")

# NULL 语义差异: 子查询含 NULL 时 NOT IN 全空, NOT EXISTS 不受影响
conn.execute("INSERT INTO orders VALUES(999999, NULL)")
conn.commit()
print("子查询混入一个 NULL 后: NOT IN =", conn.execute(q_not_in).fetchone()[0],
      "  NOT EXISTS =", conn.execute(q_not_exists).fetchone()[0])
print("结论: 否定语义一律用 NOT EXISTS 免疫 NULL; 肯定语义 IN 与 EXISTS 现代优化器多可等价改写, 实测为准")
```

**追问**:
- 为什么本机实测 EXISTS 慢很多?——SQLite 没有做半连接改写,相关子查询按嵌套循环逐行执行;MySQL 8 与 PG 会改写为 semi-join,差距通常消失。
- 大列表 IN (1,2,3...) 与子查询 IN 怎么选?——几百以内常量列表代价可忽略;上千个值会有解析与临时表成本,改成临时表 JOIN 或分批。

---
