"""批量 UPDATE 的分窗执行: 用主键窗口切片, 控锁控速可断点"""
import sqlite3
import time

DB = ":memory:"
conn = sqlite3.connect(DB)
c = conn.cursor()
c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, status TEXT, flag INTEGER NOT NULL DEFAULT 0)")
c.executemany("INSERT INTO orders(id, status) VALUES(?,?)",
              [(i, "done" if i % 3 == 0 else "pending") for i in range(1, 20001)])
c.execute("CREATE INDEX idx_status ON orders(status)")
conn.commit()

WINDOW = 2500
last_max_id = 0          # 断点: 上一个窗口的右边界
t0 = time.perf_counter()
total = 0
while True:
    # 每个窗口独立事务: 主键 > 上次右边界 AND 条件命中, 再限行数
    c.execute("BEGIN")
    c.execute(
        "UPDATE orders SET flag = 1 WHERE id > ? AND id <= ? AND status = 'done'",
        (last_max_id, last_max_id + WINDOW))
    n = c.rowcount
    hi = c.execute("SELECT MAX(id) FROM orders WHERE id > ? AND id <= ?",
                   (last_max_id, last_max_id + WINDOW)).fetchone()[0]
    c.execute("COMMIT")
    if hi is None:
        break
    last_max_id = hi
    total += n
    print("窗口 <=%-6d 本窗更新 %5d 行, 累计 %6d 行" % (hi, n, total))
    if last_max_id >= 20000:
        break

cost = (time.perf_counter() - t0) * 1000
done = c.execute("SELECT COUNT(*) FROM orders WHERE status='done' AND flag=1").fetchone()[0]
all_done = c.execute("SELECT COUNT(*) FROM orders WHERE status='done'").fetchone()[0]
print("分窗执行完成: 命中 %d/%d, 耗时 %.0f ms; 每窗独立提交, 中断后从 last_max_id=%d 续跑"
      % (done, all_done, cost, last_max_id))
print("与一条大 UPDATE 相比: 单条语句一把锁到底, 分窗把锁窗口切成 N 段, 主从延迟与锁等待都可控")
