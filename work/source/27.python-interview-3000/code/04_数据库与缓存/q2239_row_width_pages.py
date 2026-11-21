"""行宽与内存页: 窄行一页多行, 超宽行进溢出页"""
import os
import sqlite3

def build(path, wide):
    if os.path.exists(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("PRAGMA page_size=4096")
    c.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, payload TEXT)")
    if wide:
        c.executemany("INSERT INTO t VALUES(?,?)", [(i, "x" * 20000) for i in range(1, 1001)])
    else:
        c.executemany("INSERT INTO t VALUES(?,?)", [(i, str(i % 2)) for i in range(1, 1001)])
    conn.commit()
    pages = c.execute("PRAGMA page_count").fetchone()[0]
    conn.close()
    return pages * 4096

b1 = build("/tmp/q2239_narrow.db", wide=False)
b2 = build("/tmp/q2239_wide.db", wide=True)
n = 1000
print("窄行表: 1000 行 共 %7.1f KB, 每行摊 %4.0f B" % (b1 / 1024.0, b1 / n))
print("宽行表: 1000 行 20KB 字段, 共 %7.1f KB, 每行摊 %4.0f B" % (b2 / 1024.0, b2 / n))
print("宽行一行占 5-6 个 4KB 页: 主页放行头与前缀, 其余在溢出页, 读一行变成读多页")
os.remove("/tmp/q2239_narrow.db")
os.remove("/tmp/q2239_wide.db")
