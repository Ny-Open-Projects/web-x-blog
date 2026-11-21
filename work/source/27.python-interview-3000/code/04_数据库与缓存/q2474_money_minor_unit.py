"""金额的最小单位存储: 用'分'的整数, 把浮点误差挡在库外"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE payments (id INTEGER PRIMARY KEY, cents INTEGER NOT NULL)")
# 若用 REAL 存 0.1+0.2 之类, 聚合后出现 0.30000000000000004
c.execute("CREATE TABLE payments_real (amount REAL)")
c.executemany("INSERT INTO payments_real VALUES(?)", [(0.1,), (0.2,)])
print("浮点存储聚合: %r  <- 经典误差" % c.execute(
    "SELECT SUM(amount) FROM payments_real").fetchone()[0])

# 分单位整数: 聚合永远精确
c.executemany("INSERT INTO payments(cents) VALUES(?)", [(10,), (20,), (70,)])
total = c.execute("SELECT SUM(cents) FROM payments").fetchone()[0]
print("分单位聚合: %d 分 = %.2f 元, 无任何误差" % (total, total / 100.0))

# 分摊: 100 元分给 3 人, 余数处理是分单位存储的真正考点
def split_cents(total_cents, n):
    base, rem = divmod(total_cents, n)
    return [base + (1 if i < rem else 0) for i in range(n)]

parts = split_cents(10000, 3)
print("10000 分分 3 份 -> %s, 合计 %d 分, 一分不丢" % (parts, sum(parts)))
assert sum(parts) == 10000

# 边界: 千万别把'元'的小数与'分'的整数混存
c.execute("CREATE TABLE bad (amount REAL)")
c.execute("INSERT INTO bad VALUES(19.99)")
stored = c.execute("SELECT amount * 100 FROM bad").fetchone()[0]
print("浮点元 * 100 转分: %r  <- 转换本身引入误差, 必须 round 或从一开始就存分" % stored)
print("纪律: 金额列一律整数分(或 DECIMAL), 运算在整数域完成, 展示层才除 100 格式化")
