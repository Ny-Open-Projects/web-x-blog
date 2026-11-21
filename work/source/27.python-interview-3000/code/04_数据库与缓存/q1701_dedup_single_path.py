"""防重表 + 唯一支路: 所有写入收敛到单一入口, 唯一约束做最后防线"""
import os
import sqlite3
import tempfile
import threading

DB = os.path.join(tempfile.gettempdir(), "q1701_dedup.db")
if os.path.exists(DB):
    os.remove(DB)

def new_conn():
    c = sqlite3.connect(DB, timeout=10)
    c.executescript("""
    CREATE TABLE IF NOT EXISTS dedup(biz_key TEXT PRIMARY KEY, result TEXT);
    CREATE TABLE IF NOT EXISTS payment(id INTEGER PRIMARY KEY AUTOINCREMENT,
        biz_key TEXT UNIQUE, amount REAL);
    """)
    return c

def pay_once(biz_key, amount):
    """唯一支路: 不做先查后插, 直接靠唯一约束在同事务里裁决"""
    c = new_conn()
    try:
        with c:
            c.execute("INSERT INTO dedup(biz_key, result) VALUES(?, 'init')", (biz_key,))
            c.execute("INSERT INTO payment(biz_key, amount) VALUES(?,?)", (biz_key, amount))
            c.execute("UPDATE dedup SET result='paid' WHERE biz_key=?", (biz_key,))
        return True, "支付成功"
    except sqlite3.IntegrityError:
        return False, "重复请求, 返回原结果"
    except sqlite3.OperationalError as e:
        return False, f"数据库忙, 由上层重试: {e}"
    finally:
        c.close()

print(pay_once("PO-1", 100.0))
print(pay_once("PO-1", 100.0), "<- 同 biz_key 第二次")
print(pay_once("PO-1", 200.0), "<- 同键不同金额同样被拦截")
print("payment 行数:", new_conn().execute("SELECT COUNT(*) FROM payment").fetchone()[0])

results, lock = [], threading.Lock()

def worker():
    ok, _ = pay_once("PO-X", 1.0)
    with lock:
        results.append(ok)

threads = [threading.Thread(target=worker) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("10 线程并发同键: 成功笔数 =", sum(results), "/", len(results))
os.remove(DB)
print("要点: 先查后插存在竞态窗口; 唯一支路加唯一约束在并发下仍只放行一笔;")
print("      幂等的对外表现是返回原结果而不是报错")
