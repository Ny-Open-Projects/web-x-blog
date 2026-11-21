---
title: [Q1661] NULL 三值逻辑陷阱: NOT IN 遇上 NULL
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1661 · NULL 三值逻辑陷阱: NOT IN 遇上 NULL

> 难度:★★☆☆ | 标签:SQL, NULL 语义

**问**:为什么说 NOT IN 配子查询是线上事故高发写法?NULL 在 SQL 里到底参与了几种"逻辑"?

**答**:SQL 是三值逻辑:TRUE、FALSE 之外还有 UNKNOWN,任何值与 NULL 的等值比较结果都是 UNKNOWN 而不是 FALSE。NOT IN 的语义是"对子查询结果逐个做不等于判断再取与",只要子查询里混进一个 NULL,整个表达式就永远无法判定为 TRUE,外层查询返回空集。同理,WHERE col != 1 会静默丢掉 col 为 NULL 的行,COUNT(*) 与 COUNT(col) 口径不同,NULL 与 NULL 互不相等、判等必须用 IS。防御办法是给可能为 NULL 的列显式加 WHERE col IS NOT NULL 过滤,或者直接改用 NOT EXISTS。

```python
# file: code/04_数据库与缓存/q1661_null_notin.py
"""NULL 三值逻辑陷阱: NOT IN 遇上 NULL 与比较的第三种结果"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE vip(user_id INTEGER PRIMARY KEY);
CREATE TABLE logs(id INTEGER PRIMARY KEY, user_id INTEGER);
INSERT INTO vip VALUES(1), (2), (3);
INSERT INTO logs VALUES(1, 1), (2, 2), (3, NULL);
""")

def rows(sql):
    return [r[0] for r in conn.execute(sql)]

# 陷阱一: NOT IN 的子查询含 NULL 时, 整个外层查询返回空集
bad = rows("SELECT user_id FROM vip WHERE user_id NOT IN (SELECT user_id FROM logs)")
good = rows("SELECT user_id FROM vip v WHERE NOT EXISTS "
            "(SELECT 1 FROM logs l WHERE l.user_id = v.user_id)")
print("NOT IN 含 NULL 的子查询 ->", bad, "(全空: x 不等于 NULL 结果是 UNKNOWN, 整体永假)")
print("NOT EXISTS 同语义查询  ->", good)

# 陷阱二: WHERE col != 1 不会返回 NULL 行, NULL 参与任何比较都是 UNKNOWN
print("COUNT(*) =", rows("SELECT COUNT(*) FROM logs")[0],
      "  COUNT(user_id) =", rows("SELECT COUNT(user_id) FROM logs")[0])
print("user_id != 1 的行 ->", rows("SELECT id FROM logs WHERE user_id != 1"),
      "NULL 行被静默过滤")

# 陷阱三: NULL 与 NULL 不相等, 判等必须用 IS
print("NULL = NULL  ->", rows("SELECT NULL = NULL")[0], " (NULL)")
print("NULL IS NULL ->", rows("SELECT NULL IS NULL")[0], " (1)")
print("结论: 外层否定查询一律用 NOT EXISTS; 统计口径区分 COUNT(*) 与 COUNT(col); 判等用 IS")
```

**追问**:
- CHECK 约束里写 col != 0 能拦住 NULL 吗?——不能,UNKNOWN 不是 FALSE,CHECK 对 UNKNOWN 放行,要挡住必须显式写 col IS NOT NULL 或加 NOT NULL 约束。
- JOIN 的 ON 条件里 NULL 行为一样吗?——一样,NULL 永远匹配不上等值 JOIN,所以 left join 找"无匹配"要用 IS NULL 判右侧键。

---
