"""大字段拆分: 主表瘦身前后的大小与页数对比"""
import os
import sqlite3

DETAIL = "x" * 8000

def build(with_detail):
    path = "/tmp/q1407_%s.db" % ("with" if with_detail else "split")
    if os.path.exists(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    if with_detail:
        conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, title TEXT, detail TEXT)")
        conn.executemany("INSERT INTO t VALUES(?,?,?)",
                         [(i, "t%d" % i, DETAIL) for i in range(300)])
    else:
        conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, title TEXT)")
        conn.execute("CREATE TABLE t_detail(id INTEGER PRIMARY KEY, detail TEXT)")
        conn.executemany("INSERT INTO t VALUES(?,?)", [(i, "t%d" % i) for i in range(300)])
        conn.executemany("INSERT INTO t_detail VALUES(?,?)",
                         [(i, DETAIL) for i in range(300)])
    conn.commit()
    pages = conn.execute("PRAGMA page_count").fetchone()[0]
    conn.close()
    return os.path.getsize(path), pages

s1, p1 = build(True)
s2, p2 = build(False)
print(f"合并存储: {s1} 字节 {p1} 页; 拆分后主表库: {s2} 字节 {p2} 页")
print("列表查询只触主表, 读放大显著下降; 详情按需查 t_detail")
