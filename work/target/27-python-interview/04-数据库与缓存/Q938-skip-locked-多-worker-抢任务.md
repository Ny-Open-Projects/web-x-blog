---
title: [Q938] skip_locked: 多 worker 抢任务
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q938 · skip_locked: 多 worker 抢任务

> 难度:★★★★ | 标签:并发, 任务队列

**问**:用数据库实现任务队列,多个 worker 怎么不重复、不互相等待地取任务?

**答**:标准配方:`SELECT ... WHERE status='pending' ORDER BY id LIMIT n FOR UPDATE SKIP LOCKED`,再接 UPDATE 置为 processing 并 commit——skip_locked 让被其他 worker 锁住的行直接跳过,各取各的,天然互斥且不阻塞。收尾路径:成功置 done,失败按重试次数置 pending(延迟)或 dead;处理崩溃靠租约字段(lease_until),过期任务被清扫线程回收。MySQL 8+ 与 PG 支持 SKIP LOCKED,SQLite 单写者场景用 BEGIN IMMEDIATE 近似。相比 list 队列,数据库队列的优势是事务一致与可视性,劣势是吞吐,量大换 Redis Stream/MQ。

```python
# file: code/04_数据库与缓存/q938_skip_locked_queue.py
"""SQLite 模拟 skip_locked 抢任务: 立即事务 + 行级条件更新"""
import sqlite3
import threading

def claim(db, worker):
    conn = sqlite3.connect(db, isolation_level=None)
    conn.execute("PRAGMA busy_timeout=3000")
    try:
        conn.execute("BEGIN IMMEDIATE")          # 单写临界区(等价跳过忙行)
        row = conn.execute(
            "SELECT id, payload FROM tasks WHERE status='pending' "
            "ORDER BY id LIMIT 1").fetchone()
        if not row:
            conn.execute("COMMIT")
            return None
        conn.execute("UPDATE tasks SET status='processing', worker=? WHERE id=?",
                     (worker, row[0]))
        conn.execute("COMMIT")
        return row
    except sqlite3.OperationalError:
        conn.execute("ROLLBACK")
        return "busy"

if __name__ == "__main__":
    db = "q938.db"
    s = sqlite3.connect(db, isolation_level=None)
    s.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, "
              "payload TEXT, status TEXT, worker TEXT)")
    s.execute("DELETE FROM tasks")
    s.executemany("INSERT INTO tasks (payload, status) VALUES (?, 'pending')",
                  [(f"t{i}",) for i in range(6)])
    s.close()

    out = {}
    def work(w):
        out[w] = claim(db, w)
    ts = [threading.Thread(target=work, args=(f"w{i}",)) for i in range(3)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print("领取结果:", out)
    print("剩余 pending:", sqlite3.connect(db).execute(
        "SELECT count(*) FROM tasks WHERE status='pending'").fetchone()[0])
```

**追问**:
- 为什么不能只 SELECT 再 UPDATE?——两个 worker 会读到同一 pending 行然后都改,必须借行锁/立即事务把"读+标记"做成原子。
- 任务失败后怎么回队?——按 retry_count 递增退避置回 pending(或延迟时间戳),超过上限进 dead 状态等待人工处理。

---
