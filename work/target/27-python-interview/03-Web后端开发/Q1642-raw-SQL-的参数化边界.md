---
title: [Q1642] raw SQL 的参数化边界
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1642 · raw SQL 的参数化边界

> 难度:★★★★ | 标签:SQL 安全, Django ORM

**问**:什么时候允许写 raw SQL?写的时候安全边界在哪几条线上?

**答**:合理边界:ORM 表达不了的查询——窗口函数、递归 CTE、跨表批量 UPDATE、优化器提示——这些用 raw 是工程正解;能用 ORM 表达却图省事写 raw 是负债,丢了参数绑定、类型转换与防注入的框架层。安全底线三条:一是参数永远走占位符绑定,把输入当数据,拼接字符串在代码评审就该打回,IN 子句动态展开也是生成占位符而不是拼值;二是无法参数化的子句(ORDER BY 方向、表名)走白名单,输入不在名单就用安全默认值;三是 raw 查询集中放置并注释说明为什么绕过 ORM,便于审计。演示里拼接让 WHERE 条件整个失效,参数化后同样的输入只是普通字符串。

```python
# file: code/03_Web后端开发/q1642_raw_sql.py
"""raw SQL 的边界: 参数化是底线, IN 动态展开用占位符, 排序键走白名单(标准库 sqlite3)。"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, org TEXT);
INSERT INTO users VALUES (1, 'alice', 'A'), (2, 'bob', 'B'), (3, 'carol', 'A');
""")

# 1) 注入演示: 拼接把过滤条件整个吃掉(仅计数演示, 生产严禁)
attacker = "x' OR '1'='1"
bad_count = conn.execute("SELECT COUNT(*) FROM users WHERE name = '%s'" % attacker).fetchone()[0]
print("拼接的行数(被注入):", bad_count)

# 2) 参数化: 输入永远是数据, 不是代码
safe_count = conn.execute("SELECT COUNT(*) FROM users WHERE name = ?", (attacker,)).fetchone()[0]
print("参数化的行数:", safe_count)

# 3) 动态 IN: 占位符数量与参数一一对应, 而不是把列表拼进 SQL
ids = [1, 3]
marks = ",".join("?" * len(ids))
rows = conn.execute(f"SELECT name FROM users WHERE id IN ({marks})", ids).fetchall()
print("IN 展开:", [r[0] for r in rows])

# 4) ORDER BY 无法参数化: 排序方向必须走白名单
malicious = "name; DROP TABLE users"
allowed = {"name", "created_at"}
safe_order = malicious if malicious in allowed else "id"
print("白名单后的排序键:", safe_order)
print("raw SQL 的合理边界: 窗口函数、递归 CTE、批量 UPDATE JOIN 等 ORM 表达不了的查询")
```

**追问**:
- ORM 的 extra 和 raw 怎么选?——尽量 raw 方法加参数绑定,extra 已被视为遗留接口,新代码别用。
- 动态表名怎么处理?——表名走代码内白名单映射,永远不接用户输入。
