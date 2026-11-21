"""sqlite 生成列 + 索引: 让 LOWER 条件命中索引"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("""CREATE TABLE u (
            id INTEGER PRIMARY KEY, email TEXT,
            email_lower TEXT GENERATED ALWAYS AS (lower(email)) STORED)""")
        conn.executemany("INSERT INTO u (email) VALUES (?)",
                         [(f"User{i}@Mail.com",) for i in range(10000)])
        conn.execute("CREATE INDEX idx_lower ON u (email_lower)")

        sql = "SELECT * FROM u WHERE email_lower = ?"
        plan = conn.execute("EXPLAIN QUERY PLAN " + sql, ("user8@mail.com",)).fetchall()
        print("计划:", [r[3] for r in plan])
        print("结果:", conn.execute(sql, ("user8@mail.com",)).fetchall())
