---
title: [Q1963] 锁等待超时处置: busy_timeout 与退避重试
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1963 · 锁等待超时处置: busy_timeout 与退避重试

> 难度:★★★☆ | 标签:运维, 锁

**问**:拿到 database is locked 或锁等待超时, 应用层正确的处置姿势是什么?

**答**:分三层处置。参数层:把等待超时配到能盖过最慢的合法事务, SQLite 用 busy_timeout, MySQL 用 innodb_lock_wait_timeout, 实测零等待下撞锁毫秒级报错, 配置后驱动会在锁上等待而不是立刻失败。应用层:超时是重试信号不是终态, 用指数退避加抖动重试, 实测第三次尝试在写者释放后成功;要识别可重试错误, 死锁与锁超时可重试, 语法与约束错误不可。治本层:缩短写事务、统一加锁顺序、拆大事务, 并在监控上区分锁等待与死锁。重试必须带幂等保障, 否则一次成功的重试叠加一次误判的失败就是重复写。

```python
# file: code/04_数据库与缓存/q1963_lock_wait_timeout.py
"""锁等待超时处置: busy_timeout 指数退避与锁持有最小化"""
import os
import sqlite3
import tempfile
import threading
import time

db_path = os.path.join(tempfile.mkdtemp(), "lock.sqlite")
writer = sqlite3.connect(db_path, check_same_thread=False, timeout=0.3)
reader = sqlite3.connect(db_path, timeout=0.3)
writer.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v INTEGER)")
writer.execute("INSERT INTO t VALUES(1, 1)")
writer.commit()

def hold_briefly(seconds):
    """短暂持有写锁 模拟一个慢写事务"""
    writer.execute("BEGIN IMMEDIATE")
    writer.execute("UPDATE t SET v = v + 1 WHERE id = 1")
    time.sleep(seconds)
    writer.rollback()

# 默认 busy_timeout 为 0: 撞锁立刻报错
reader.execute("PRAGMA busy_timeout = 0")
writer.execute("BEGIN IMMEDIATE")
writer.execute("UPDATE t SET v = v + 1 WHERE id = 1")
t0 = time.perf_counter()
try:
    reader.execute("INSERT INTO t(v) VALUES(2)")
    print("居然写入成功")
except sqlite3.OperationalError as e:
    print(f"零等待撞锁 -> {time.perf_counter() - t0:.3f}s 即报错: {e}")
writer.rollback()

# 设置 busy_timeout 让驱动在锁上等待而不是立刻失败: 写者 0.1 秒后释放
reader.execute("PRAGMA busy_timeout = 200")
holder = threading.Thread(target=hold_briefly, args=(0.10,))
holder.start()
time.sleep(0.02)
t0 = time.perf_counter()
reader.execute("INSERT INTO t(v) VALUES(2)")
reader.commit()
print(f"busy_timeout=200 -> 等待 {time.perf_counter() - t0:.3f}s 写者释放后写入成功")
holder.join()

def with_retry(fn, attempts=5, base=0.05):
    for i in range(attempts):
        try:
            return fn(), i
        except sqlite3.OperationalError as e:
            if "locked" not in str(e) or i == attempts - 1:
                raise
            time.sleep(base * 2 ** i + 0.01)   # 0.06 0.11 0.21 指数退避

reader.execute("PRAGMA busy_timeout = 0")
holder = threading.Thread(target=hold_briefly, args=(0.12,))
holder.start()
time.sleep(0.02)                              # 确保写锁先就位
t0 = time.perf_counter()
result, attempt = with_retry(lambda: reader.execute("INSERT INTO t(v) VALUES(3)").rowcount)
reader.commit()
holder.join()
print(f"退避重试 -> 第 {attempt + 1} 次成功 耗时 {time.perf_counter() - t0:.2f}s 影响行数 {result}")
print("结论: 超时阈值要盖过最慢的合法事务 重试要指数退避加抖动 治本是缩短写事务与统一加锁顺序")
```

**追问**:
- 重试的抖动为什么必要?—— 同时超时的请求按同样节奏重试会再次集体撞锁, 抖动把重试时间打散降低二次冲突概率。
- 怎么区分锁等待和死锁?—— 死锁会被数据库主动检测并回滚牺牲者报错码明确, 锁等待是被动超时, 监控上按错误码分类统计。

---
