"""表膨胀的估算与增量清理: freelist 算账, auto_vacuum 增量还页"""
import os
import sqlite3
import tempfile

dbpath = os.path.join(tempfile.mkdtemp(), "bloat.db")
conn = sqlite3.connect(dbpath, isolation_level=None)
conn.execute("PRAGMA page_size=4096")
conn.execute("PRAGMA auto_vacuum=INCREMENTAL")     # 必须在建表前设置
conn.execute("CREATE TABLE log (id INTEGER PRIMARY KEY, msg TEXT)")
conn.execute("BEGIN IMMEDIATE")
conn.executemany("INSERT INTO log VALUES(?,?)",
                 [(i, "m" * 100) for i in range(1, 20001)])
conn.execute("COMMIT")
before = conn.execute("PRAGMA page_count").fetchone()[0]
conn.execute("DELETE FROM log WHERE id % 2 = 0")   # 删一半: 空页留在 freelist, 文件不变小

pc = conn.execute("PRAGMA page_count").fetchone()[0]
fl = conn.execute("PRAGMA freelist_count").fetchone()[0]
print("删除一半后: page_count=%d, freelist=%d (%.0f%%), 可回收约 %.1f MB"
      % (pc, fl, fl * 100.0 / pc, fl * 4096 / 1048576.0))

conn.execute("PRAGMA incremental_vacuum(200)")     # 每次最多还 200 页, 控 IO 节奏
fl2 = conn.execute("PRAGMA freelist_count").fetchone()[0]
print("增量回收一批后 freelist=%d (还剩 %d 页待回收)" % (fl2, fl2))
conn.execute("PRAGMA incremental_vacuum")          # 不带参数 = 全部还清
fl3 = conn.execute("PRAGMA freelist_count").fetchone()[0]
pc3 = conn.execute("PRAGMA page_count").fetchone()[0]
print("全部还清: freelist=%d, page_count=%d, 文件缩小 %.1f MB"
      % (fl3, pc3, (before - pc3) * 4096 / 1048576.0))
conn.close()
