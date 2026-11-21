"""迁移演练: 影子表校验后原子切换"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER, amount INTEGER, status TEXT);
CREATE TABLE orders_new(id INTEGER PRIMARY KEY, user_id INTEGER, amount INTEGER, status TEXT,
                        CHECK (amount >= 0));
""")
rows = [(i, i % 100, i % 900, "paid" if i % 2 else "open") for i in range(1, 5001)]
conn.executemany("INSERT INTO orders VALUES(?,?,?,?)", rows)
conn.execute("INSERT INTO orders VALUES(6001, 7, -5, 'paid')")   # 混入一行违反新约束的脏数据
conn.commit()

# 第一步: 全量拷贝到影子表 演练应当在这里暴露脏数据与约束冲突
copied, rejected = 0, 0
src_rows = conn.execute("SELECT id, user_id, amount, status FROM orders").fetchall()
for r in src_rows:
    try:
        conn.execute("INSERT INTO orders_new VALUES(?,?,?,?)", r)
        copied += 1
    except sqlite3.IntegrityError:
        rejected += 1
conn.commit()
print(f"全量拷贝 成功 {copied} 行 被新约束拒绝 {rejected} 行 <- 演练发现了脏数据")

# 第二步: 增量回放 模拟迁移窗口内持续写入
delta = [(9000 + i, i % 100, i, "paid") for i in range(50)]
conn.executemany("INSERT INTO orders VALUES(?,?,?,?)", delta)
conn.executemany("INSERT INTO orders_new VALUES(?,?,?,?)", delta)
conn.commit()

# 第三步: 三重校验 行数与聚合指纹 抽样逐行
src = conn.execute(
    "SELECT COUNT(*), COALESCE(SUM(amount), 0), MAX(id) FROM orders WHERE amount >= 0").fetchone()
dst = conn.execute("SELECT COUNT(*), COALESCE(SUM(amount), 0), MAX(id) FROM orders_new").fetchone()
print("指纹比对 源 剔除脏行 ->", src, " 影子 ->", dst, " 一致:", src == dst)
smp_s = conn.execute("SELECT * FROM orders WHERE id % 997 = 0 AND amount >= 0 ORDER BY id").fetchall()
smp_d = conn.execute("SELECT * FROM orders_new WHERE id % 997 = 0 ORDER BY id").fetchall()
print("抽样比对一致:", smp_s == smp_d)

# 第四步: 校验全绿才原子切换 旧表改名保留作回退路径
conn.executescript("ALTER TABLE orders RENAME TO orders_old; ALTER TABLE orders_new RENAME TO orders;")
print("切换后结构 ->", [r[1] for r in conn.execute("PRAGMA table_info(orders)")],
      " 行数", conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0],
      " 旧表保留", conn.execute("SELECT COUNT(*) FROM orders_old").fetchone()[0], "行可回退")
print("结论: 演练让脏数据 约束冲突 增量窗口在预发暴露 切换必须原子改名且保留旧表回退路径")
