"""备份恢复演练: 清单与自动验证脚本"""
import os
import sqlite3
import tempfile
import time

src = os.path.join(tempfile.mkdtemp(), "prod.sqlite")
conn = sqlite3.connect(src)
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, amount INTEGER)")
conn.executemany("INSERT INTO orders(amount) VALUES(?)", [(i % 97,) for i in range(10000)])
conn.commit()

# 第 1 步: 用 backup API 拿一致性快照 而不是拷贝热文件
bak = os.path.join(tempfile.mkdtemp(), "bak.sqlite")
with sqlite3.connect(bak) as dst:
    conn.backup(dst)
print("1 备份完成 文件大小:", os.path.getsize(bak), "字节")

# 第 2-5 步: 隔离环境恢复并做四层验证
r = sqlite3.connect(bak)
print("2 integrity_check:", r.execute("PRAGMA integrity_check").fetchone()[0])
n_src = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
n_bak = r.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
print(f"3 行数比对: 源 {n_src} 备 {n_bak}", "一致" if n_src == n_bak else "不一致!")

fp_src = conn.execute("SELECT COUNT(*), SUM(amount), MIN(id), MAX(id) FROM orders").fetchone()
fp_bak = r.execute("SELECT COUNT(*), SUM(amount), MIN(id), MAX(id) FROM orders").fetchone()
print("4 聚合指纹比对:", fp_src == fp_bak, fp_bak)

smp_src = conn.execute("SELECT * FROM orders WHERE id % 997 = 0 ORDER BY id").fetchall()
smp_bak = r.execute("SELECT * FROM orders WHERE id % 997 = 0 ORDER BY id").fetchall()
print("5 抽样逐行比对:", smp_src == smp_bak, f" 共 {len(smp_bak)} 行")

# 第 6-9 步: 冒烟测可用性 记录 RTO 归档结论 排期下次演练 挂告警
t0 = time.perf_counter()
_ = r.execute("SELECT SUM(amount) FROM orders").fetchone()
print(f"6 冒烟查询可用 恢复验证耗时 {1000 * (time.perf_counter() - t0):.1f} ms")
print("7 演练结论归档  8 下次演练排期  9 备份任务失败挂告警")
print("结论: 备份的价值等于最近一次恢复演练 没验证过可恢复的备份等于没有备份")
