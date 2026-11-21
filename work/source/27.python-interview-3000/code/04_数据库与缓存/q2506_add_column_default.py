"""加列默认值的 online 差异: 元数据秒加与数据回填是两件事"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, amt INTEGER)")
c.executemany("INSERT INTO orders(amt) VALUES(?)", [(i,) for i in range(1, 50001)])
conn.commit()

# SQLite / MySQL 8 INSTANT / PG 11+ 这一类: 常量默认值只记元数据, 不改历史行
t0 = time.perf_counter()
c.execute("ALTER TABLE orders ADD COLUMN flag INTEGER NOT NULL DEFAULT 0")
ms_alter = (time.perf_counter() - t0) * 1000
t0 = time.perf_counter()
n = c.execute("SELECT COUNT(*) FROM orders WHERE flag = 0").fetchone()[0]
ms_read = (time.perf_counter() - t0) * 1000
print("5 万行表加列带默认值: ALTER 耗时 %.1f ms, 查询默认值命中 %d 行 耗时 %.1f ms"
      % (ms_alter, n, ms_read))
dflt = [r[4] for r in c.execute("PRAGMA table_info(orders)") if r[1] == "flag"][0]
print("table_info 里 flag 的 dflt_value=%r  <- 默认值存在元数据里, 历史行没被重写" % dflt)

# 表达式默认值在 ALTER ADD COLUMN 里不被允许 (常量才行)
try:
    c.execute("ALTER TABLE orders ADD COLUMN ts INTEGER DEFAULT (strftime('%s','now'))")
except sqlite3.OperationalError as e:
    print("表达式默认值被拒: %s" % e)

# 版本不支持 instant 的库/场景: 加可空列 + 分批回填 + 再收约束
t0 = time.perf_counter()
conn.execute("ALTER TABLE orders ADD COLUMN tag TEXT")
WINDOW, last = 10000, 0
batches = 0
while True:
    cur = conn.execute("SELECT id FROM orders WHERE id > ? AND tag IS NULL LIMIT ?",
                       (last, WINDOW))
    ids = [r[0] for r in cur.fetchall()]
    if not ids:
        break
    conn.execute("UPDATE orders SET tag='legacy' WHERE id IN (%s)"
                 % ",".join("?" * len(ids)), ids)
    conn.commit()
    last = ids[-1]
    batches += 1
ms_backfill = (time.perf_counter() - t0) * 1000
print("回填路线: 加可空列 + %d 个窗口分批 UPDATE, 总耗时 %.1f ms (每批独立提交可断点)"
      % (batches, ms_backfill))
print("结论: '加列'的代价取决于默认值是元数据还是数据; instant DDL 秒级完成,")
print("      回填是另一笔账, 任何库上大表都该走'可空列 -> 分批回填 -> 收紧约束'三步")
