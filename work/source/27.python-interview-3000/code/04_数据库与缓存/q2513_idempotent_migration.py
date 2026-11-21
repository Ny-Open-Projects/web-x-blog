"""迁移脚本的幂等执行: 版本表 + 语句级双保险"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE schema_migrations (version TEXT PRIMARY KEY, applied_at TEXT DEFAULT CURRENT_TIMESTAMP)")
c.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, amount INTEGER)")

def col_exists(table, col):
    return any(r[1] == col for r in c.execute("PRAGMA table_info(%s)" % table))

MIGRATIONS = [
    ("0001_create_orders", lambda: c.execute(
        "CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, amount INTEGER)")),
    ("0002_add_status", lambda: None if col_exists("orders", "status")
        else c.execute("ALTER TABLE orders ADD COLUMN status TEXT DEFAULT 'new'")),
    ("0003_add_index", lambda: c.execute(
        "CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status)")),
]

def migrate():
    applied = {r[0] for r in c.execute("SELECT version FROM schema_migrations")}
    ran = []
    for version, fn in MIGRATIONS:
        if version in applied:
            continue
        fn()
        c.execute("INSERT INTO schema_migrations(version) VALUES(?)", (version,))
        ran.append(version)
    conn.commit()
    return ran

print("第一次执行:", migrate())
print("第二次执行:", migrate())
for v in [r[0] for r in c.execute("SELECT version FROM schema_migrations ORDER BY version")]:
    print("  已应用:", v)

# 对照: 没有版本表也没有 IF NOT EXISTS 的裸脚本, 第二次就炸
try:
    c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, amount INTEGER)")
except sqlite3.OperationalError as e:
    print("裸脚本重放: %s" % e)
print("结论: 幂等迁移是版本表(跳过已应用)与语句级保险(IF NOT EXISTS/条件加列)的双保险,")
print("      后者是前者的安全气囊——版本表丢失或人为补录时, 语句级守卫兜住重放")
