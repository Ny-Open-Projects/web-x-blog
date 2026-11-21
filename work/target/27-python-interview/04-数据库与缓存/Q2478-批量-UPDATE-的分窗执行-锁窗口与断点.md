---
title: [Q2478] 批量 UPDATE 的分窗执行: 锁窗口与断点
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2478 · 批量 UPDATE 的分窗执行: 锁窗口与断点

> 难度:★★★☆ | 标签:批量, 运维

**问**:要把 2 万行订单打上标记,一条大 UPDATE 和分批执行怎么选?

**答**:一条大 UPDATE 的问题是"一把锁到底":行锁(或间隙锁)从头持到尾,主从延迟拉长,失败则全部回滚重来。分窗执行用主键窗口切片,每窗一个独立小事务,锁窗口变成 N 段,每段提交后进度可观测、可断点续跑——记住上一个窗口的右边界,中断后从它继续。窗口大小按"单窗执行时间 × 主从延迟预算"定,通常几千行。代价是总耗时略增(多次事务开销)与窗口间数据变动需要条件里带好过滤,工程上绝大多数批量 UPDATE 都值得分窗。

```python
# file: code/04_数据库与缓存/q2478_batched_update_windows.py
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
```

**追问**:
- 窗口怎么选不会漏行?—— 以主键为序推进,条件里带主键区间与业务过滤;业务条件随时间变化的要先落成快照表再更新。
- 和"LIMIT 2000 循环"的区别?—— LIMIT 循环每次都要重新找命中行,主键窗口走范围扫描,推进边界明确且天然可断点。

---
