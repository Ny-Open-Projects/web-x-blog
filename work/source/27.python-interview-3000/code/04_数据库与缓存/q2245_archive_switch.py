"""归档表切换的双写窗口: 双写 -> 读灰度 -> 反转写权威 -> 收尾"""
import random
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE orders_hot(id INTEGER PRIMARY KEY, amt REAL)")
c.execute("CREATE TABLE orders_archive(id INTEGER PRIMARY KEY, amt REAL)")
random.seed(2)

class Cutover:
    def __init__(self):
        self.dual_write = True
        self.read_archive_pct = 0

    def write_order(self, oid, amt):
        if self.dual_write:
            c.execute("INSERT OR REPLACE INTO orders_hot VALUES(?,?)", (oid, amt))
            c.execute("INSERT OR REPLACE INTO orders_archive VALUES(?,?)", (oid, amt))
        else:
            c.execute("INSERT OR REPLACE INTO orders_archive VALUES(?,?)", (oid, amt))

    def read_order(self, oid):
        if random.random() * 100 < self.read_archive_pct:
            return c.execute("SELECT amt FROM orders_archive WHERE id=?", (oid,)).fetchone()
        return c.execute("SELECT amt FROM orders_hot WHERE id=?", (oid,)).fetchone()

ct = Cutover()
for oid in range(1, 101):
    ct.write_order(oid, float(oid))

def recon():
    a = dict(c.execute("SELECT id, amt FROM orders_hot"))
    b = dict(c.execute("SELECT id, amt FROM orders_archive"))
    return len(a), len(b), sum(1 for k in a if a[k] != b.get(k))

print("双写后对账 hot=%d 行 archive=%d 行 差异=%d" % recon())
ct.read_archive_pct = 50
reads = [ct.read_order(1)[0] for _ in range(100)]
print("读灰度 50%% 两条路径结果一致:", all(r == 1.0 for r in reads))
ct.read_archive_pct = 100
ct.dual_write = False
for oid in range(101, 121):
    ct.write_order(oid, float(oid))
print("写权威反转后 hot 停在 %d 行, 新数据只进 archive=%d 行" % (
    c.execute("SELECT count(*) FROM orders_hot").fetchone()[0],
    c.execute("SELECT count(*) FROM orders_archive").fetchone()[0]))
print("窗口期纪律: 双写保一致 读灰度可回滚 对账归零才停写旧表, 旁路写入要提前收编")
