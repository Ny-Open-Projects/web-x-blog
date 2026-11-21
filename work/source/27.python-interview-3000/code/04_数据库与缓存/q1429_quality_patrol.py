"""定时对账任务: 数据质量巡检框架的最小实现"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
conn.executescript("""
CREATE TABLE orders(id INTEGER PRIMARY KEY, uid INTEGER, amount REAL, status TEXT);
INSERT INTO orders VALUES(1,1,100,'PAID'),(2,99,50,'PAID'),(3,1,-5,'PAID'),(4,2,80,'WEIRD');
CREATE TABLE users(id INTEGER PRIMARY KEY);
INSERT INTO users VALUES(1),(2);
""")

RULES = []
def rule(name, severity):
    def deco(fn):
        RULES.append((name, severity, fn))
        return fn
    return deco

@rule("负金额订单", "critical")
def negative_amount(c):
    return c.execute("SELECT COUNT(*) FROM orders WHERE amount < 0").fetchone()[0]

@rule("孤儿订单", "critical")
def orphan_orders(c):
    return c.execute("SELECT COUNT(*) FROM orders o LEFT JOIN users u ON o.uid=u.id "
                     "WHERE u.id IS NULL").fetchone()[0]

@rule("字典外状态", "warn")
def bad_status(c):
    return c.execute("SELECT COUNT(*) FROM orders WHERE status NOT IN "
                     "('PAID','PENDING','FAILED')").fetchone()[0]

def patrol(c):
    hits = []
    for name, severity, fn in RULES:
        n = fn(c)
        mark = "!!" if n and severity == "critical" else ("??" if n else "ok")
        print(f"[{mark}] {name}({severity}): {n} 条")
        if n:
            hits.append(name)
    return hits

bad = patrol(conn)
print("巡检结论:", ("需要治理: " + ",".join(bad)) if bad else "全部通过")
print("工程化: 轻规则高频重规则低峰, 结果入看板, critical 自动开工单")
