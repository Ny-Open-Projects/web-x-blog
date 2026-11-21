"""脏检查与 flush 时机: 属性快照如何只发变更列"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, city TEXT)")
conn.execute("INSERT INTO users VALUES(1, 'alice', 30, 'hz')")
conn.commit()

COLS = ("id", "name", "age", "city")

class Tracked:
    def __init__(self, row):
        self.current = dict(zip(COLS, row))
        self.snapshot = dict(self.current)       # 载入时的属性快照

obj = Tracked(conn.execute(
    "SELECT id, name, age, city FROM users WHERE id=1").fetchone())

def flush(tracked, conn):
    changed = {k: v for k, v in tracked.current.items()
               if k != "id" and tracked.snapshot.get(k) != v}
    if not changed:
        print("flush: 无脏属性, 不发 SQL")
        return
    sets = ", ".join(f"{k} = ?" for k in changed)
    sql = f"UPDATE users SET {sets} WHERE id = ?"
    print("flush 发出:", sql, "参数:", list(changed.values()) + [tracked.current["id"]])
    conn.execute(sql, list(changed.values()) + [tracked.current["id"]])
    conn.commit()
    tracked.snapshot = dict(tracked.current)

obj.current["age"] = 31
obj.current["city"] = "sh"
flush(obj, conn)          # 只更新 age 与 city 两列, name 未变不进 UPDATE
flush(obj, conn)          # 快照已刷新, 二次 flush 零 SQL
print("要点: 快照在查询时建立; commit 前触发 flush; expire 后下次访问重发 SELECT 重建快照;")
print("      大批量修改绕过逐对象脏检查, 用批量 UPDATE 语句更划算")
