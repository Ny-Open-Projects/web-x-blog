"""巡检项的自动化清单: 每项一个函数, 三态输出与处置建议"""
import sqlite3

CHECKS = []
def check(name, advice):
    def deco(fn):
        CHECKS.append((name, advice, fn))
        return fn
    return deco

@check("quick_check 完整性", "FAIL 时立即停写并备份")
def _(conn):
    return conn.execute("PRAGMA quick_check").fetchone()[0]

@check("freelist 膨胀度", "超 30% 预约 VACUUM 窗口")
def _(conn):
    pc = conn.execute("PRAGMA page_count").fetchone()[0]
    fl = conn.execute("PRAGMA freelist_count").fetchone()[0]
    ratio = fl / max(1, pc)
    return "PASS" if ratio <= 0.3 else "WARN %.0f%%" % (ratio * 100)

@check("孤儿引用", "回溯删除路径并补数据修复")
def _(conn):
    n = conn.execute("""SELECT COUNT(*) FROM orders o
                        LEFT JOIN users u ON u.id = o.user_id
                        WHERE u.id IS NULL""").fetchone()[0]
    return "PASS" if n == 0 else "WARN %d 条" % n

@check("挂起写事务", "超 10 分钟的写事务人工介入")
def _(conn):
    conn.execute("BEGIN")                      # 模拟一个挂起的写事务
    conn.execute("CREATE TABLE IF NOT EXISTS tmp_tx (x)")
    conn.execute("INSERT INTO tmp_tx VALUES(1)")
    conn.execute("ROLLBACK")                   # 实际系统里查事务表的事务年龄
    return "PASS"

conn = sqlite3.connect(":memory:", isolation_level=None)
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY)")
conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER)")
conn.executemany("INSERT INTO users VALUES(?)", [(1,), (2,)])
conn.executemany("INSERT INTO orders VALUES(?,?)", [(1, 1), (2, 2), (3, 99)])
for name, advice, fn in CHECKS:
    print("[%s] %-18s 处置: %s" % (fn(conn), name, advice))
conn.close()
