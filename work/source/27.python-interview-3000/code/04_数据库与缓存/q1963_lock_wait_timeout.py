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
