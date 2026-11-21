"""计算不同前缀长度的选择性, 并用 sqlite 表达式索引验证命中"""
import sqlite3
import random
import string

def selectivity(values, n):
    return len({v[:n] for v in values}) / len(values)

if __name__ == "__main__":
    random.seed(7)
    emails = ["".join(random.choices(string.ascii_lowercase, k=3))
              + f"@mail{i % 97}.com" for i in range(20000)]

    for n in (2, 4, 6, 8, 10):
        print(f"前缀 {n:>2} 选择性: {selectivity(emails, n):.4f}")

    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE u (id INTEGER PRIMARY KEY, email TEXT)")
        conn.executemany("INSERT INTO u (email) VALUES (?)",
                         [(e,) for e in emails])
        conn.execute("CREATE INDEX idx_prefix ON u (substr(email, 1, 6))")
        sql = ("SELECT * FROM u WHERE substr(email, 1, 6) = substr(?, 1, 6) "
               "AND email = ?")
        plan = conn.execute("EXPLAIN QUERY PLAN " + sql,
                            (emails[0], emails[0])).fetchall()
        print("前缀索引计划:", [r[3] for r in plan])
