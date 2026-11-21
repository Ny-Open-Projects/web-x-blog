"""大结果集流式处理: fetchall 一次载入 vs 分块 fetchmany 流式"""
import sqlite3
import tracemalloc

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE big(id INTEGER PRIMARY KEY, payload TEXT)")
conn.executemany("INSERT INTO big VALUES(?,?)",
                 [(i, "x" * 200) for i in range(200000)])
conn.commit()

tracemalloc.start()
rows = conn.execute("SELECT id, payload FROM big").fetchall()   # 一次性载入
total = sum(len(r[1]) for r in rows)
peak_all = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print(f"fetchall : 行数 {len(rows)}, 载荷 {total / 1e6:.0f} MB, 峰值内存 {peak_all / 1e6:.1f} MB")

def yield_per(conn, sql, chunk=5000):
    cur = conn.execute(sql)
    while True:
        batch = cur.fetchmany(chunk)
        if not batch:
            break
        for r in batch:
            yield r

tracemalloc.start()
total, n = 0, 0
for r in yield_per(conn, "SELECT id, payload FROM big"):
    total += len(r[1])
    n += 1
peak_stream = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print(f"流式分块 : 行数 {n}, 载荷 {total / 1e6:.0f} MB, 峰值内存 {peak_stream / 1e6:.1f} MB")
print("ORM 对应 yield_per 或按主键分段; MySQL/PG 需服务端游标才真正流式, 否则驱动仍会缓冲")
print("注意: 流式遍历期间游标与事务保持打开, 注意锁持有时间与连接占用")
