"""用 sqlite 模拟 ICP 收益: 联合索引前缀模糊 + 残留条件, 观察扫描与回表差"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT, age INT)")
        conn.executemany("INSERT INTO user (name, age) VALUES (?, ?)",
                         [(("张" if i % 2 else "李") + f"{i:05d}", i % 80)
                          for i in range(20000)])
        conn.execute("CREATE INDEX idx_name_age ON user (name, age)")

        sql = "SELECT * FROM user WHERE name LIKE '张%' AND age = 20"
        plan = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()
        rows = conn.execute(sql).fetchall()
        print("计划:", [r[3] for r in plan])
        print(f"命中 {len(rows)} 行")
        print("MySQL 对照: 无 ICP 时全部张姓回表后过滤; 有 ICP 时在索引内先滤 age")
