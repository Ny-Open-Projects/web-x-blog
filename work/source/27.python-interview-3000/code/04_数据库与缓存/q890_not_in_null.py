"""复现 NOT IN 遇 NULL 结果为空, 对照 NOT EXISTS 的正确语义"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("CREATE TABLE banned (user_id INT)")
        conn.executemany("INSERT INTO users (name) VALUES (?)",
                         [("a",), ("b",), ("c",)])
        conn.executemany("INSERT INTO banned (user_id) VALUES (?)",
                         [(2,), (None,)])         # 含 NULL

        not_in = "SELECT name FROM users WHERE id NOT IN (SELECT user_id FROM banned)"
        not_exists = ("SELECT u.name FROM users u WHERE NOT EXISTS "
                      "(SELECT 1 FROM banned x WHERE x.user_id = u.id)")
        print("NOT IN 结果:", [r[0] for r in conn.execute(not_in)], "<- 因 NULL 全空")
        print("NOT EXISTS:", [r[0] for r in conn.execute(not_exists)], "<- 正常排除 id=2")
        print("计划对照:")
        for sql in (not_in, not_exists):
            print(" ", [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()])
