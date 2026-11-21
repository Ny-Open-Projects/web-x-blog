"""库存扣减的写锁实测: 写事务持锁窗口近似等于下一个写者的等待时长"""
import os
import sqlite3
import tempfile
import threading
import time

dbpath = os.path.join(tempfile.mkdtemp(), "stock.db")
conn0 = sqlite3.connect(dbpath, isolation_level=None)
conn0.execute("PRAGMA journal_mode=WAL")
conn0.execute("CREATE TABLE stock (sku TEXT PRIMARY KEY, qty INTEGER)")
conn0.execute("INSERT INTO stock VALUES('A', 100)")

held = {}
def writer(idx, hold_s):
    conn = sqlite3.connect(dbpath, isolation_level=None)
    conn.execute("PRAGMA busy_timeout=5000")
    t0 = time.perf_counter()
    conn.execute("BEGIN IMMEDIATE")                  # 拿写锁, 拿不到就在这里等
    conn.execute("UPDATE stock SET qty = qty - 1 WHERE sku='A'")
    time.sleep(hold_s)                               # 模拟持锁期间的业务处理
    conn.execute("COMMIT")
    held[idx] = (time.perf_counter() - t0) * 1000

t1 = threading.Thread(target=writer, args=(1, 0.2))
t1.start()
time.sleep(0.05)
t2 = threading.Thread(target=writer, args=(2, 0.0))
t2.start()
t1.join()
t2.join()
print("写者1 持锁窗口 %.0f ms | 写者2 等锁+执行 %.0f ms (两者近似相等)" % (held[1], held[2]))

# 条件更新守卫: 库存不足时影响行数为 0, 业务据此拒绝
cur = conn0.execute("UPDATE stock SET qty = qty - 999 WHERE sku='A' AND qty >= 999")
print("超量扣减尝试: 影响行数 %d (0 即拒绝), 当前库存 %d" %
      (cur.rowcount, conn0.execute("SELECT qty FROM stock WHERE sku='A'").fetchone()[0]))
conn0.close()
