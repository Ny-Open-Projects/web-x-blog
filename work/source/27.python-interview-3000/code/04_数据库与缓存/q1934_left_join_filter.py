"""LEFT JOIN 过滤位置: ON 保留行 WHERE 退化内连接"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER, amount INTEGER, status TEXT);
INSERT INTO users VALUES(1,'alice'),(2,'bob'),(3,'carol');
INSERT INTO orders VALUES(101,1,100,'paid'),(102,1,200,'void'),(103,2,300,'paid');
""")

def rows(sql):
    return conn.execute(sql).fetchall()

# 需求: 每个用户都要出现, 只统计 paid 订单
on_filter = rows("""
SELECT u.name, COUNT(o.id) AS cnt, COALESCE(SUM(o.amount), 0) AS total
FROM users u LEFT JOIN orders o ON o.user_id = u.id AND o.status = 'paid'
GROUP BY u.id ORDER BY u.id""")
print("过滤写在 ON   :", on_filter)

where_filter = rows("""
SELECT u.name, COUNT(o.id) AS cnt, COALESCE(SUM(o.amount), 0) AS total
FROM users u LEFT JOIN orders o ON o.user_id = u.id
WHERE o.status = 'paid'
GROUP BY u.id ORDER BY u.id""")
print("过滤写在 WHERE:", where_filter, "(carol 消失: NULL 状态判 UNKNOWN 被删行 退化成内连接)")

# WHERE 里显式放行 NULL 行能找回部分语义, 但有非 paid 订单的用户仍会整行被删
hybrid = rows("""
SELECT u.name, COUNT(o.id) AS cnt
FROM users u LEFT JOIN orders o ON o.user_id = u.id
WHERE o.status = 'paid' OR o.id IS NULL
GROUP BY u.id ORDER BY u.id""")
print("WHERE 放行 NULL:", hybrid, "(carol 回来了, alice 的 void 订单行仍被删 口径已经错)")

# 反向需求: 找没有 paid 订单的用户, 同样要靠 ON 过滤加 IS NULL
isnull = rows("""
SELECT u.name FROM users u
LEFT JOIN orders o ON o.user_id = u.id AND o.status = 'paid'
WHERE o.id IS NULL""")
print("无 paid 订单用户:", [r[0] for r in isnull])
print("结论: 右表过滤放 ON 才保住 LEFT JOIN 语义; 放 WHERE 会静默退化成 INNER JOIN")
