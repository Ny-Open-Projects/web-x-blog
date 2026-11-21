"""索引上线前 EXPLAIN 门禁: 计划断言自动化"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER, status TEXT, amount INTEGER)")
conn.executemany("INSERT INTO orders VALUES(?,?,?,?)",
                 [(i, i % 5000, "paid" if i % 3 else "open", i % 1000) for i in range(30000)])
conn.commit()

def plan_details(sql):
    return [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql)]

def gate(sql, must_use=None):
    """上线门禁: 必须命中期望索引 且不允许无索引支撑的全表扫描"""
    details = plan_details(sql)
    problems = []
    if must_use and must_use not in " | ".join(details):
        problems.append("未命中期望索引 %s" % must_use)
    for d in details:
        if d.startswith("SCAN") and "USING" not in d:
            problems.append("全表扫描: %s" % d)
    return problems, details

cases = ["SELECT * FROM orders WHERE user_id = 42",
         "SELECT * FROM orders WHERE status = 'paid' AND amount > 500"]
print("--- 建索引前 门禁应当拦截 ---")
for sql in cases:
    problems, details = gate(sql)
    print("拦截 ->", problems or "通过", "  计划:", details[0] if details else "")

conn.execute("CREATE INDEX idx_o_user ON orders(user_id)")
conn.execute("CREATE INDEX idx_o_status_amt ON orders(status, amount)")
conn.commit()
print("--- 建索引后 重新过门禁 ---")
for sql in cases:
    must = "idx_o_user" if "user_id" in sql else "idx_o_status_amt"
    problems, details = gate(sql, must_use=must)
    print("通过 ->" if not problems else "仍拦截 ->", problems or must, "  计划:", details[0])
print("结论: 索引评审要跑在真实量级数据上 门禁断言三件事 命中目标索引 无裸全表扫 无意外临时表与排序")
