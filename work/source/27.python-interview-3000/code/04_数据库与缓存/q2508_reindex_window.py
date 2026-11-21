"""索引重建的时机与窗口: 膨胀信号 REINDEX 与 VACUUM 的分工"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE events (id INTEGER PRIMARY KEY, cat TEXT, payload TEXT)")
c.execute("CREATE INDEX idx_cat ON events(cat, payload)")
c.executemany("INSERT INTO events VALUES(?,?,?)",
              [(i, "cat%d" % (i % 50), "p%d" % i) for i in range(1, 30001)])
conn.commit()

# 制造膨胀: 删掉 8 成数据, 索引页并不立即归还
c.execute("DELETE FROM events WHERE id % 5 != 0")
conn.commit()
freelist = c.execute("PRAGMA freelist_count").fetchone()[0]
pages_before = c.execute("PRAGMA page_count").fetchone()[0]
n = c.execute("SELECT COUNT(*) FROM events").fetchone()[0]
print("删除后剩 %d 行: page_count=%d freelist=%d (空闲页占 %.0f%%)"
      % (n, pages_before, freelist, freelist * 100.0 / pages_before))

# REINDEX: 重建索引的逻辑结构, 整理碎片, 不归还空间
t0 = time.perf_counter()
c.execute("REINDEX idx_cat")
ms_reindex = (time.perf_counter() - t0) * 1000
ok = c.execute("PRAGMA integrity_check").fetchone()[0]
print("REINDEX 耗时 %.1f ms, integrity_check=%s (结构重建 但空间在 freelist 里)" % (ms_reindex, ok))

# VACUUM: 归还空间, 需要近似整库复制的窗口
pages_mid = c.execute("PRAGMA page_count").fetchone()[0]
t0 = time.perf_counter()
c.execute("VACUUM")
ms_vacuum = (time.perf_counter() - t0) * 1000
pages_after = c.execute("PRAGMA page_count").fetchone()[0]
print("VACUUM 耗时 %.1f ms: page_count %d -> %d (空间真正归还)" % (ms_vacuum, pages_mid, pages_after))
print("结论: 索引膨胀的信号是'行数跌 索引体积不跌', REINDEX 治结构 VACUUM 治空间;")
print("      生产库的 REINDEX/VACUUM 都要低峰窗口+主从拆解: 它们等价于一次全量读+全量写")
