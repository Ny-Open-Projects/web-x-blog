"""外键开关下的批量导入: 即时拦截 vs 事后巡检的权衡"""
import sqlite3
import time

N = 20000
BAD = [(30000 + i, 99999) for i in range(10)]          # 10 条悬空引用
rows = [(i, (i % 10000) + 1) for i in range(1, N + 1)] + BAD

def build(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, "
              "user_id INTEGER NOT NULL REFERENCES users(id))")   # 外键必须显式声明
    c.executemany("INSERT INTO users VALUES(?,?)",
                  [(i, "u%d" % i) for i in range(1, 10001)])
    return c

# 方式一: 开外键, 坏行当场拦截
conn_on = sqlite3.connect(":memory:")
conn_on.execute("PRAGMA foreign_keys = ON")
c = build(conn_on)
try:
    c.executemany("INSERT INTO orders VALUES(?,?)", rows)
except sqlite3.IntegrityError as e:
    ok = c.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
    print("外键开启: %s -> 悬空引用零入库, 合法行已入库 %d 条" % (e, ok))

# 方式二: 关外键, 全部进库后巡检
conn_off = sqlite3.connect(":memory:")
conn_off.execute("PRAGMA foreign_keys = OFF")
c = build(conn_off)
t0 = time.perf_counter()
c.executemany("INSERT INTO orders VALUES(?,?)", rows)
ms = (time.perf_counter() - t0) * 1000
violations = c.execute("PRAGMA foreign_key_check(orders)").fetchall()
print("外键关闭: %d 条全部入库 耗时 %.0f ms, 巡检发现 %d 条孤儿行"
      % (N + 10, ms, len(violations)))
orphans = c.execute("""SELECT COUNT(*) FROM orders o
    WHERE o.user_id NOT IN (SELECT id FROM users)""").fetchone()[0]
print("补一刀确认: user_id 不在 users 的行 = %d 条, 需补数据或删除" % orphans)
assert len(violations) == orphans == 10

# 性能面: 同一批合法数据, 开关外键各导一次 (先清表)
c.execute("DELETE FROM orders")
t0 = time.perf_counter()
c.executemany("INSERT INTO orders VALUES(?,?)", rows[:N])
ms_off = (time.perf_counter() - t0) * 1000
conn_on2 = sqlite3.connect(":memory:")
conn_on2.execute("PRAGMA foreign_keys = ON")
c2 = build(conn_on2)
t0 = time.perf_counter()
c2.executemany("INSERT INTO orders VALUES(?,?)", rows[:N])
ms_on = (time.perf_counter() - t0) * 1000
print("合法数据 %d 行导入: 外键开 %.0f ms vs 外键关 %.0f ms (内存库差距小, 磁盘库放大)"
      % (N, ms_on, ms_off))
print("结论: 即时拦截换来的是'坏行进不了门', 事后巡检换来的是'吞吐', 二者必须二选一地自觉")
