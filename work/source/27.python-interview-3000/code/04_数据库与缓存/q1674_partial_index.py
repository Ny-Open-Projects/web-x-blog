"""partial index: 部分索引的概念与 sqlite 演示"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE jobs(id INTEGER PRIMARY KEY, status TEXT, priority INTEGER)")
conn.executemany("INSERT INTO jobs VALUES(?,?,?)",
                 [(i, "done" if i % 50 else "pending", i % 7) for i in range(1, 50001)])
conn.commit()
# 普通索引覆盖全部 5 万行, 其中 98% 是 done
conn.execute("CREATE INDEX idx_full ON jobs(status)")
# 部分索引只索引 pending 子集
conn.execute("CREATE INDEX idx_pending ON jobs(status, priority) WHERE status='pending'")
conn.commit()

def plan(sql):
    return [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql)]

print("查询 pending 的计划:", plan("SELECT * FROM jobs WHERE status='pending'"))
print("查询 done 的计划:   ", plan("SELECT * FROM jobs WHERE status='done'"))
print("普通索引行数:", conn.execute("SELECT COUNT(*) FROM jobs INDEXED BY idx_full").fetchone()[0])
print("部分索引行数:", conn.execute(
    "SELECT COUNT(*) FROM jobs INDEXED BY idx_pending WHERE status='pending'").fetchone()[0])
print("要点: 部分索引把热子集建成小而准的索引, 体积与维护成本按选择度比例缩小;")
print("      查询条件必须蕴含建索引的谓词, 优化器才会选用它")
