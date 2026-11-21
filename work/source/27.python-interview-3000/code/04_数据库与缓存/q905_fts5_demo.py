"""sqlite FTS5 全文索引: 建虚拟表 插入检索 与 LIKE 性能对比"""
import sqlite3
import time

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        docs = [(f"第{i}篇 python 数据库与缓存 调优 文章内容{i % 7}",)
                for i in range(20000)]
        conn.execute("CREATE TABLE docs (content TEXT)")
        conn.executemany("INSERT INTO docs VALUES (?)", docs)

        try:
            conn.execute("CREATE VIRTUAL TABLE fts USING fts5(content)")
            conn.executemany("INSERT INTO fts VALUES (?)", docs)

            t0 = time.perf_counter()
            r1 = conn.execute("SELECT count(*) FROM docs WHERE content LIKE '%文章内容3%'").fetchone()
            t1 = time.perf_counter()
            r2 = conn.execute("SELECT count(*) FROM fts WHERE fts MATCH '文章内容3'").fetchone()
            t2 = time.perf_counter()
            print(f"LIKE: {r1[0]} 行 {(t1-t0)*1000:.1f} ms")
            print(f"FTS5 MATCH: {r2[0]} 行 {(t2-t1)*1000:.1f} ms")
        except sqlite3.OperationalError as e:
            print("当前 sqlite 编译未含 FTS5:", e)
