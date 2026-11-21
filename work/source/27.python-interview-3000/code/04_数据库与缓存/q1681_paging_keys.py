"""分页键稳定性: 排序列不唯一时 keyset 分页丢行的实测与修复"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE item(id INTEGER PRIMARY KEY, score INTEGER)")
conn.executemany("INSERT INTO item VALUES(?,?)",
                 [(i, i // 10) for i in range(1, 101)])   # 每 10 行同分
conn.commit()

def page_by_score(last_score, limit=5):
    return conn.execute(
        "SELECT id, score FROM item WHERE score > ? ORDER BY score LIMIT ?",
        (last_score, limit)).fetchall()

page1 = page_by_score(-1)
print("仅按 score 翻页 第一页:", page1)
page2 = page_by_score(page1[-1][1])
print("第二页:", page2)
print("与 last 同分段的其余行被 WHERE score > last 整段跳过 -> 丢行")

# 修复: 加唯一 tie-breaker, 排序键变成 (score, id)
def page_tiebreak(last_score, last_id, limit=5):
    return conn.execute(
        "SELECT id, score FROM item WHERE score > ? OR (score = ? AND id > ?) "
        "ORDER BY score, id LIMIT ?", (last_score, last_score, last_id, limit)).fetchall()

rows_all = []
pid, pscore = 0, -1
while True:
    chunk = page_tiebreak(pscore, pid)
    if not chunk:
        break
    rows_all.extend(chunk)
    pid, pscore = chunk[-1]

print("带 tie-breaker 的 keyset 翻页取回行数:", len(rows_all),
      "完整覆盖 1..100:", sorted(r[0] for r in rows_all) == list(range(1, 101)))

conn.execute("CREATE INDEX idx_score_id ON item(score, id)")
print("复合索引计划:", [r[3] for r in conn.execute(
    "EXPLAIN QUERY PLAN SELECT id, score FROM item WHERE score > ? "
    "ORDER BY score, id LIMIT ?", (5, 5))])
print("要点: keyset 分页的排序键必须以唯一列收尾; OFFSET 分页在并发插入下也会漂移, 生产优先 keyset")
