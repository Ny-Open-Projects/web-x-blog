"""统计信息与分析器: ANALYZE 采集分布, 陈旧统计误导优化器"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, status TEXT)")
conn.executemany("INSERT INTO orders VALUES(?,?)",
                 [(i, "pending" if i % 100 == 0 else "done") for i in range(1, 50001)])
conn.execute("CREATE INDEX idx_status ON orders(status)")
conn.commit()

def plan(sql):
    return [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql)]

q = "SELECT * FROM orders WHERE status='pending'"
print("未收集统计:", plan(q))
conn.execute("ANALYZE")
print("ANALYZE 后:", plan(q))
print("sqlite_stat1 内容 (表行数, 索引列不同值数):",
      conn.execute("SELECT tbl, idx, stat FROM sqlite_stat1").fetchall())

# 场景: 大规模删除后统计信息过期
conn.execute("DELETE FROM orders WHERE status='done'")
conn.commit()
print("现在表只剩", conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0], "行, 全是 pending")
print("陈旧统计下的计划(仍按 5 万行估算):", plan(q))
conn.execute("ANALYZE")
print("重新 ANALYZE:", plan(q), "-> 表只剩目标行, 全表扫比索引跳转更便宜")
print("要点: 计划质量取决于统计新鲜度; 大批量变更后手动 ANALYZE, 生产库对倾斜列考虑直方图")
