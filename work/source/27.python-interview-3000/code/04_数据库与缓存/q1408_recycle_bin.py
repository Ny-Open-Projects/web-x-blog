"""回收站表: 删除先进回收站, 可恢复, 定期清理过期"""
import json
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, amount REAL)")
conn.execute("""CREATE TABLE recycle_bin(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    src_table TEXT, src_id INTEGER, payload TEXT, deleted_at REAL)""")
conn.executemany("INSERT INTO orders VALUES(?,?)", [(1, 100.0), (2, 200.0)])

def delete_order(oid):
    row = conn.execute("SELECT * FROM orders WHERE id=?", (oid,)).fetchone()
    conn.execute("INSERT INTO recycle_bin(src_table, src_id, payload, deleted_at) "
                 "VALUES('orders',?,?,?)",
                 (oid, json.dumps({"id": row[0], "amount": row[1]}), time.time()))
    conn.execute("DELETE FROM orders WHERE id=?", (oid,))

def restore(bin_id):
    row = conn.execute("SELECT src_id, payload FROM recycle_bin WHERE id=?",
                       (bin_id,)).fetchone()
    data = json.loads(row[1])
    if conn.execute("SELECT 1 FROM orders WHERE id=?", (data["id"],)).fetchone():
        return False, "id 已被占用 转人工"
    conn.execute("INSERT INTO orders VALUES(?,?)", (data["id"], data["amount"]))
    conn.execute("DELETE FROM recycle_bin WHERE id=?", (bin_id,))
    return True, "已恢复"

delete_order(1)
print("删除后 orders 行数:", conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0])
print("恢复结果:", restore(1))
print("恢复后 orders 行数:", conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0])
