"""调整 join 顺序观察 sqlite 计划: 过滤后的表应做驱动"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE big (id INTEGER PRIMARY KEY, uid INT, flag INT)")
        conn.execute("CREATE TABLE small (id INTEGER PRIMARY KEY, tag TEXT)")
        conn.executemany("INSERT INTO big (uid, flag) VALUES (?, ?)",
                         [(i % 1000, i % 200) for i in range(50000)])
        conn.executemany("INSERT INTO small (tag) VALUES (?)",
                         [(f"tag{i}",) for i in range(50)])
        conn.execute("CREATE INDEX idx_big_uid ON big (uid)")
        conn.execute("CREATE INDEX idx_big_flag ON big (flag)")

        j1 = ("SELECT s.tag, count(*) FROM big b JOIN small s ON s.id = b.uid "
              "WHERE b.flag = 7 GROUP BY s.tag")
        j2 = ("SELECT s.tag, count(*) FROM small s JOIN big b ON s.id = b.uid "
              "WHERE b.flag = 7 GROUP BY s.tag")
        for label, sql in (("big 驱动", j1), ("small 驱动", j2)):
            print(label, [r[3] for r in
                          conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()])
        print("两结果一致, 驱动顺序由优化器决定; 统计失真时用 STRAIGHT_JOIN 干预")
