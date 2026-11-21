"""SQLite 模拟 skip_locked 抢任务: 立即事务 + 行级条件更新"""
import sqlite3
import threading

def claim(db, worker):
    conn = sqlite3.connect(db, isolation_level=None)
    conn.execute("PRAGMA busy_timeout=3000")
    try:
        conn.execute("BEGIN IMMEDIATE")          # 单写临界区(等价跳过忙行)
        row = conn.execute(
            "SELECT id, payload FROM tasks WHERE status='pending' "
            "ORDER BY id LIMIT 1").fetchone()
        if not row:
            conn.execute("COMMIT")
            return None
        conn.execute("UPDATE tasks SET status='processing', worker=? WHERE id=?",
                     (worker, row[0]))
        conn.execute("COMMIT")
        return row
    except sqlite3.OperationalError:
        conn.execute("ROLLBACK")
        return "busy"

if __name__ == "__main__":
    db = "q938.db"
    s = sqlite3.connect(db, isolation_level=None)
    s.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, "
              "payload TEXT, status TEXT, worker TEXT)")
    s.execute("DELETE FROM tasks")
    s.executemany("INSERT INTO tasks (payload, status) VALUES (?, 'pending')",
                  [(f"t{i}",) for i in range(6)])
    s.close()

    out = {}
    def work(w):
        out[w] = claim(db, w)
    ts = [threading.Thread(target=work, args=(f"w{i}",)) for i in range(3)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print("领取结果:", out)
    print("剩余 pending:", sqlite3.connect(db).execute(
        "SELECT count(*) FROM tasks WHERE status='pending'").fetchone()[0])
