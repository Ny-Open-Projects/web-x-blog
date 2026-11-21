"""sqlite JSON 列 + 生成列索引: 按内部字段高效查询"""
import json
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("""CREATE TABLE profile (
        id INTEGER PRIMARY KEY,
        info TEXT,
        city TEXT GENERATED ALWAYS AS (json_extract(info, '$.city')) VIRTUAL)""")
    conn.executemany("INSERT INTO profile (info) VALUES (?)",
                     [(json.dumps({"name": n, "city": c}),) for n, c in
                      [("alice", "BJ"), ("bob", "SH"), ("carol", "BJ")]])
    conn.execute("CREATE INDEX idx_city ON profile (city)")

    plan = conn.execute(
        "EXPLAIN QUERY PLAN SELECT * FROM profile WHERE city = 'BJ'").fetchall()
    print("计划:", [r[3] for r in plan])
    print("命中:", conn.execute(
        "SELECT json_extract(info, '$.name') FROM profile WHERE city = ?",
        ("BJ",)).fetchall())
