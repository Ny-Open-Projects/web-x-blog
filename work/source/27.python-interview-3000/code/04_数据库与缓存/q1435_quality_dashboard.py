"""综合案例: 为订单库建一套数据质量看板"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
conn.executescript("""
CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT);
CREATE TABLE orders(id INTEGER PRIMARY KEY, uid INTEGER, amount REAL, status TEXT, city TEXT);
INSERT INTO users VALUES(1,'a@x'),(2,'a@x'),(3,NULL);
INSERT INTO orders VALUES
 (1,1,100,'PAID','BJ'),(2,1,-20,'PAID','BJ'),(3,99,50,'paid','SH'),
 (4,2,80,NULL,'SZ'),(5,2,60,'FAILED',NULL);
""")

def check(name, sql):
    return name, conn.execute(sql).fetchone()[0]

checks = [
    check("用户重复邮箱",
          "SELECT COUNT(*) FROM (SELECT email FROM users GROUP BY email HAVING COUNT(*) > 1)"),
    check("用户缺邮箱", "SELECT COUNT(*) FROM users WHERE email IS NULL OR email=''"),
    check("孤儿订单",
          "SELECT COUNT(*) FROM orders o LEFT JOIN users u ON o.uid=u.id WHERE u.id IS NULL"),
    check("负金额", "SELECT COUNT(*) FROM orders WHERE amount < 0"),
    check("字典外状态",
          "SELECT COUNT(*) FROM orders WHERE status IS NULL OR status NOT IN "
          "('PAID','PENDING','FAILED')"),
    check("缺城市", "SELECT COUNT(*) FROM orders WHERE city IS NULL OR city=''"),
]
total_orders = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
print("订单库质量看板")
print("-" * 40)
worst = None
for name, n in checks:
    print(f"{name}: {n} 条")
    if n and (worst is None or n > worst[1]):
        worst = (name, n)
print("-" * 40)
print(f"订单总数 {total_orders}, 最突出问题: {worst[0]}({worst[1]} 条)")
print("闭环: 每条规则挂 owner 与 SLA, 修复后复检归零, 规则库持续沉淀")
