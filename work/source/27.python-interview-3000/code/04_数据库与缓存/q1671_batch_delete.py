"""批量 DELETE 分批: 大表清理的分批提交与节奏控制"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE logs(id INTEGER PRIMARY KEY, created INTEGER, expired INTEGER)")
conn.execute("CREATE INDEX idx_exp ON logs(expired)")
conn.executemany("INSERT INTO logs VALUES(?,?,?)",
                 [(i, i, 1 if i % 2 == 0 else 0) for i in range(120000)])
conn.commit()

BATCH = 5000
total = conn.execute("SELECT COUNT(*) FROM logs WHERE expired=1").fetchone()[0]
print(f"待删除 {total} 行, 每批 {BATCH} 行")

batch_no, total_ms = 0, 0.0
while True:
    t0 = time.perf_counter()
    cur = conn.execute(
        "DELETE FROM logs WHERE id IN "
        "(SELECT id FROM logs WHERE expired = 1 LIMIT ?)", (BATCH,))
    conn.commit()                      # 每批提交, 释放空间与锁
    ms = (time.perf_counter() - t0) * 1000
    total_ms += ms
    batch_no += 1
    if batch_no <= 3 or cur.rowcount == 0:
        print(f"  第 {batch_no} 批删 {cur.rowcount} 行, 耗时 {ms:.1f} ms")
    if cur.rowcount < BATCH:
        break

print(f"共 {batch_no} 批, 总耗时 {total_ms:.0f} ms")
print("剩余未过期行:", conn.execute("SELECT COUNT(*) FROM logs WHERE expired=0").fetchone()[0])
print("要点: 一条巨型 DELETE 的 undo 与锁持有时间不可控, 分批提交把影响切片;")
print("      生产再加批间 sleep 限速, 过滤列必须有索引否则每批都是全表扫")
