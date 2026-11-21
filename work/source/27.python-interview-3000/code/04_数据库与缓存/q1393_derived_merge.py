"""派生表的合并与物化: 哪些子查询可以被优化器展开"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL)")
conn.executemany("INSERT INTO orders VALUES(?,?,?)",
                 [(i, i % 1000, 9.9) for i in range(20000)])

def plan(sql, label):
    print(label)
    for r in conn.execute("EXPLAIN QUERY PLAN " + sql):
        print("   ", r[3])

plan("SELECT * FROM (SELECT id, user_id, amount FROM orders WHERE amount > 5) t "
     "WHERE t.user_id = 7", "[简单投影] 可合并 条件可下推:")
plan("SELECT * FROM (SELECT id, user_id FROM orders ORDER BY id LIMIT 100) t "
     "WHERE t.user_id = 7", "[带 LIMIT] 不可合并 需物化:")
plan("SELECT * FROM (SELECT user_id, COUNT(*) c FROM orders GROUP BY user_id) t "
     "WHERE t.user_id = 7", "[聚合派生表] 物化后过滤:")
