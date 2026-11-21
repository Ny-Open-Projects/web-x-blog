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
