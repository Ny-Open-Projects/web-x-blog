"""版本号乐观锁: 模拟并发更新冲突与重试成功"""
import sqlite3

def fetch(conn, oid):
    row = conn.execute(
        "SELECT id, qty, version FROM stock WHERE id = ?", (oid,)).fetchone()
    return {"id": row[0], "qty": row[1], "version": row[2]}

def update_with_version(conn, item, delta):
    cur = conn.execute(
        "UPDATE stock SET qty = qty + ?, version = version + 1 "
        "WHERE id = ? AND version = ?", (delta, item["id"], item["version"]))
    conn.commit()
    return cur.rowcount == 1

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE stock (id INTEGER PRIMARY KEY, qty INT, version INT)")
    conn.execute("INSERT INTO stock VALUES (1, 10, 0)")

    item = fetch(conn, 1)
    stale = dict(item)                       # 模拟另一个会话的旧快照
    ok = update_with_version(conn, item, 5)  # 会话A成功
    print("A 更新:", ok)
    ok2 = update_with_version(conn, stale, -3)  # B 拿旧版本提交
    print("B 旧版本提交:", ok2, "<- 版本不匹配被拒绝")
    fresh = fetch(conn, 1)
    print("B 重读后重试:", update_with_version(conn, fresh, -3),
          "当前:", fetch(conn, 1))
