"""sqlite 演示 ISO 文本与 epoch 两种存储的时区行为与范围查询"""
import sqlite3
import time as t

if __name__ == "__main__":
    now = int(t.time())
    with sqlite3.connect(":memory:") as conn:
        conn.execute("""CREATE TABLE ev (id INTEGER PRIMARY KEY,
                        iso TEXT, epoch INT)""")
        conn.executemany("INSERT INTO ev (iso, epoch) VALUES (?, ?)",
                         [("2026-11-01 10:00:00", now - 3600),
                          ("2026-11-01 11:00:00", now),
                          ("1970-01-01 00:00:01", 1)])
        print("epoch 范围查(近两小时):",
              conn.execute("SELECT count(*) FROM ev WHERE epoch >= ?",
                           (now - 7200,)).fetchone()[0])
        print("ISO 范围查:",
              conn.execute("SELECT count(*) FROM ev WHERE iso >= '2026-11-01'").fetchone()[0])
        print("epoch 可读化:", conn.execute(
            "SELECT datetime(epoch, 'unixepoch', '+8 hours') FROM ev WHERE epoch = 1").fetchone())
        print("MySQL 对照: timestamp 2038 上限与自动时区转换是选型分水岭")
