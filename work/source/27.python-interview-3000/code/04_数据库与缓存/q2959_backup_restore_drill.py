"""备份恢复演练: 在线备份 指纹校验 灾难恢复 RPO 损失实测"""
import os
import shutil
import sqlite3
import tempfile
import time

work = tempfile.mkdtemp(prefix="drill_")
main_db, bak_db = os.path.join(work, "main.db"), os.path.join(work, "bak.db")

conn = sqlite3.connect(main_db)
conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v TEXT)")
conn.executemany("INSERT INTO t(v) VALUES(?)",
                 [("v%d" % i,) for i in range(1, 5001)])
conn.commit()

# 1) 在线备份: backup API 不阻断业务读写
t0 = time.perf_counter()
dst = sqlite3.connect(bak_db)
conn.backup(dst)
dst.close()
backup_ms = (time.perf_counter() - t0) * 1000


def fingerprint(path):
    c = sqlite3.connect(path)
    fp = c.execute("SELECT COUNT(*), SUM(id) FROM t").fetchone()
    c.close()
    return fp


base = fingerprint(bak_db)
print("备份 %d 行耗时 %.0f ms, 指纹(行数, id总和) = %s"
      % (base[0], backup_ms, base))
assert fingerprint(main_db) == base, "备份必须与源一致"

# 2) 备份点之后业务继续写入 10 行 —— 这就是潜在 RPO 损失
conn.executemany("INSERT INTO t(v) VALUES(?)",
                 [("late%d" % i,) for i in range(10)])
conn.commit()
print("备份后新增 10 行, 当前总行数:",
      conn.execute("SELECT COUNT(*) FROM t").fetchone()[0])

# 3) 灾难: 误操作清空全表
conn.execute("DELETE FROM t")
conn.commit()
print("灾难发生: 主库行数 =",
      conn.execute("SELECT COUNT(*) FROM t").fetchone()[0])

# 4) 恢复: 停写 -> 备份顶上 -> 核对指纹
t0 = time.perf_counter()
conn.close()
shutil.copyfile(bak_db, main_db)
conn = sqlite3.connect(main_db)
restored = fingerprint(main_db)
rto_ms = (time.perf_counter() - t0) * 1000
print("恢复完成, 指纹: %s, RTO 约 %.0f ms" % (restored, rto_ms))
assert restored == base
print("RPO 损失 = 备份点之后的 10 行 (生产要用 binlog 增量把这段补齐)")
conn.close()
shutil.rmtree(work)
print("演练通过: 备份可恢复, 恢复可校验, 损失可量化")
