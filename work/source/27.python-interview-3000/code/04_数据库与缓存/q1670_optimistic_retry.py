"""乐观锁重试实战: 版本号条件更新 加 指数退避重试"""
import random
import sqlite3
import time

random.seed(42)
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE stock(sku TEXT PRIMARY KEY, qty INTEGER, version INTEGER)")
conn.execute("INSERT INTO stock VALUES('sku-1', 100, 0)")
conn.commit()

def load():
    return conn.execute("SELECT qty, version FROM stock WHERE sku='sku-1'").fetchone()

class Rival:
    """并发对手: 每次被调用就抢先扣减一次库存并推进版本"""
    def __init__(self, times):
        self.times, self.called = times, 0
    def strike(self):
        if self.called >= self.times:
            return
        self.called += 1
        conn.execute("UPDATE stock SET qty=qty-1, version=version+1 WHERE sku='sku-1'")
        conn.commit()

def deduct(want, rival, max_retry=5):
    for attempt in range(1, max_retry + 1):
        qty, ver = load()
        if qty < want:
            return False, "库存不足"
        rival.strike()                      # 对手在我们读之后抢先写入
        cur = conn.execute(
            "UPDATE stock SET qty=qty-?, version=version+1 WHERE sku='sku-1' AND version=?",
            (want, ver))
        conn.commit()
        if cur.rowcount == 1:
            return True, f"第 {attempt} 次尝试成功"
        print(f"  第 {attempt} 次提交冲突: 本地 version={ver} 已过期, 退避后重试")
        time.sleep(0.01 * (2 ** (attempt - 1)) + random.random() * 0.005)
    return False, f"重试 {max_retry} 次仍冲突"

ok, msg = deduct(5, Rival(times=1))
print(ok, msg, "当前库存与版本:", load())
ok, msg = deduct(5, Rival(times=0))
print(ok, msg, "当前库存与版本:", load())
print("要点: WHERE version=? 是冲突检测, rowcount=0 即冲突; ")
print("      重试要有上限, 退避要加抖动, 否则高并发下会活锁; 冲突率高就改悲观锁或队列串行")
