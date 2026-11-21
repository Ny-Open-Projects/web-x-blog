"""归档作业的进度断点: 分批迁移与断点续跑"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE events(id INTEGER PRIMARY KEY, kind TEXT, payload TEXT);
CREATE TABLE events_archive(id INTEGER PRIMARY KEY, kind TEXT, payload TEXT);
CREATE TABLE job_progress(job TEXT PRIMARY KEY, last_id INTEGER, done INTEGER, total INTEGER);
INSERT INTO job_progress VALUES('archive_events', 0, 0, 0);
""")
conn.executemany("INSERT INTO events(kind, payload) VALUES(?,?)",
                 [("click", "p" * 20) for _ in range(2000)])
conn.execute("UPDATE job_progress SET total = (SELECT COUNT(*) FROM events)")
conn.commit()

def archive_batch(batch=300):
    """从断点之后取一批 迁移与删源同事务 成功后推进断点"""
    last_id, done, total = conn.execute(
        "SELECT last_id, done, total FROM job_progress WHERE job = 'archive_events'").fetchone()
    rows = conn.execute(
        "SELECT id, kind, payload FROM events WHERE id > ? ORDER BY id LIMIT ?",
        (last_id, batch)).fetchall()
    if not rows:
        return False
    conn.executemany("INSERT INTO events_archive VALUES(?,?,?)", rows)
    conn.execute("DELETE FROM events WHERE id IN (%s)" % ",".join("?" * len(rows)),
                 [r[0] for r in rows])
    conn.execute("UPDATE job_progress SET last_id = ?, done = ? WHERE job = 'archive_events'",
                 (rows[-1][0], done + len(rows)))
    conn.commit()
    return True

for _ in range(3):
    archive_batch()
p = conn.execute("SELECT last_id, done FROM job_progress WHERE job = 'archive_events'").fetchone()
print("跑三批后断点 ->", p, " 源表剩", conn.execute("SELECT COUNT(*) FROM events").fetchone()[0], "行")

rounds = 0
while archive_batch():          # 断点续跑: 崩溃后重进 从 last_id 接着走
    rounds += 1
p = conn.execute("SELECT done, total FROM job_progress WHERE job = 'archive_events'").fetchone()
print(f"续跑 {rounds} 批完成 -> 源表 {conn.execute('SELECT COUNT(*) FROM events').fetchone()[0]} 行 "
      f"归档表 {conn.execute('SELECT COUNT(*) FROM events_archive').fetchone()[0]} 行 进度 {p}")
print("结论: 归档必须幂等可重入 断点记业务主键而非行号 迁移与删源同事务提交才能既不丢也不重")
