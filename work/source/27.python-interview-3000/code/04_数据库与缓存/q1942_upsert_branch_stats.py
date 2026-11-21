"""upsert 分支统计: 哪些行走了 insert 哪些走了 update"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE stock(sku TEXT PRIMARY KEY, qty INTEGER, updated INTEGER)")
conn.commit()

# 方案一: 逐行 INSERT OR IGNORE 加 UPDATE, 用 total_changes 差值精确归因
def upsert_with_stats(rows):
    ins, upd = [], []
    for sku, qty, ts in rows:
        before = conn.total_changes
        conn.execute("INSERT OR IGNORE INTO stock VALUES(?,?,?)", (sku, qty, ts))
        if conn.total_changes - before == 1:
            ins.append(sku)
        else:
            conn.execute("UPDATE stock SET qty = qty + ?, updated = ? WHERE sku = ?", (qty, ts, sku))
            upd.append(sku)
    return ins, upd

r1 = upsert_with_stats([("A1", 10, 1), ("A2", 5, 1)])
print("第一批 ->", "insert:", r1[0], "update:", r1[1])
r2 = upsert_with_stats([("A1", 3, 2), ("A3", 7, 2), ("A1", 1, 3)])
print("第二批 ->", "insert:", r2[0], "update:", r2[1])
print("表内容 ->", conn.execute("SELECT * FROM stock ORDER BY sku").fetchall())

# 方案二: 单条 ON CONFLICT 批量语句, EXCLUDED 引用本次候选值
# 分支归因: 先查已存在的键, 再用 total_changes 差值反推 update 行数
def upsert_bulk(rows):
    marks = ",".join("?" * len(rows))
    existing = {r[0] for r in conn.execute(
        "SELECT sku FROM stock WHERE sku IN (%s)" % marks, [r[0] for r in rows])}
    before = conn.total_changes
    conn.executemany("""
        INSERT INTO stock(sku, qty, updated) VALUES(?,?,?)
        ON CONFLICT(sku) DO UPDATE SET
            qty = qty + excluded.qty,
            updated = excluded.updated""", rows)
    changed = conn.total_changes - before
    n_ins = len([s for s, _, _ in rows if s not in existing])
    return n_ins, changed - n_ins

r3 = upsert_bulk([("A1", 2, 4), ("A4", 9, 4)])
print("批量 upsert ->", "insert:", r3[0], "update:", r3[1], " 与逐行法口径一致")
print("表终态 ->", conn.execute("SELECT * FROM stock ORDER BY sku").fetchall())
print("结论: changes 口径只给总行数 分支归因靠存在性预查或逐行计数 EXCLUDED 用于引用冲突候选行")
