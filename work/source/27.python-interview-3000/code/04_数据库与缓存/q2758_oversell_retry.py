"""防超卖双保险实测: 条件更新守门 + 版本号乐观重试"""
import os
import random
import sqlite3
import tempfile
import threading
import time

dbpath = os.path.join(tempfile.mkdtemp(), "seckill.db")
init = sqlite3.connect(dbpath, isolation_level=None)
init.execute("PRAGMA journal_mode=WAL")
init.execute("CREATE TABLE goods (id INTEGER PRIMARY KEY, stock INTEGER, ver INTEGER)")
init.execute("INSERT INTO goods VALUES(1, 5, 0)")

sold = []
attempts = {"n": 0}
lock = threading.Lock()

def buyer(bid):
    conn = sqlite3.connect(dbpath, isolation_level=None)
    conn.execute("PRAGMA busy_timeout=3000")
    for _ in range(50):                              # 重试上限, 防风暴
        with lock:
            attempts["n"] += 1
        try:
            stock, ver = conn.execute(
                "SELECT stock, ver FROM goods WHERE id=1").fetchone()
            if stock <= 0:
                return False
            cur = conn.execute(
                "UPDATE goods SET stock=stock-1, ver=ver+1 "
                "WHERE id=1 AND stock=? AND ver=?", (stock, ver))
            if cur.rowcount == 1:
                with lock:
                    sold.append(bid)
                return True
        except sqlite3.OperationalError:
            pass                                     # 忙等也算一次失败重试
        time.sleep(random.uniform(0, 0.002))         # 随机退避
    return False

threads = [threading.Thread(target=buyer, args=(i,)) for i in range(20)]
for t in threads:
    t.start()
for t in threads:
    t.join()
stock = init.execute("SELECT stock FROM goods WHERE id=1").fetchone()[0]
assert stock >= 0 and len(sold) == 5 - stock
print("20 人抢 5 件: 成交 %d, 最终库存 %d, 总尝试 %d 次其中重试 %d 次"
      % (len(sold), stock, attempts["n"], attempts["n"] - len(sold)))
print("不变量: 成交数 + 剩余库存 = 初始库存, 超卖在条件更新下无路径发生")
init.close()
