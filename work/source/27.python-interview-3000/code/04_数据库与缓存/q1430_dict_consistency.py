"""字典表一致性: 状态值白名单校验与脏值归一"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
conn.execute("CREATE TABLE dict_status(code TEXT PRIMARY KEY)")
conn.executescript("INSERT INTO dict_status VALUES('PAID'),('PENDING'),('FAILED')")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, status TEXT)")
conn.executemany("INSERT INTO orders VALUES(?,?)",
                 [(1, 'PAID'), (2, 'paid'), (3, 'ok'), (4, 'PENDING')])

bad = conn.execute("SELECT id, status FROM orders WHERE status NOT IN "
                   "(SELECT code FROM dict_status)").fetchall()
print("字典外状态:", bad)
mapping = {"paid": "PAID", "ok": "FAILED"}    # 归一规则, 新值需先评审入字典
for oid, s in bad:
    conn.execute("UPDATE orders SET status=? WHERE id=?",
                 (mapping.get(s, "FAILED"), oid))
left = conn.execute("SELECT COUNT(*) FROM orders WHERE status NOT IN "
                    "(SELECT code FROM dict_status)").fetchone()[0]
print(f"归一后残留 {left} 条; 防复发: 写入层枚举校验 + 巡检常态监控")
