"""排名口径分页实测: RANK 跳号空洞 DENSE_RANK 稳定 ROW_NUMBER 去重"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE scores(id INTEGER PRIMARY KEY, name TEXT, score INTEGER)")
conn.executemany("INSERT INTO scores(name, score) VALUES(?,?)", [
    ("alice", 95), ("bob", 92), ("bobby", 92), ("carol", 92),
    ("dave", 88), ("dan", 88), ("frank", 80)])

base = ("SELECT name, score, ROW_NUMBER() OVER (ORDER BY score DESC, id) AS rn, "
        "RANK() OVER (ORDER BY score DESC) AS rk, "
        "DENSE_RANK() OVER (ORDER BY score DESC) AS dr FROM scores")
print("全量口径:")
for r in conn.execute(base):
    print("  %-6s %3d  rn=%d rk=%d dr=%d" % r)

def page(fn, lo, hi):
    sql = ("SELECT name, score FROM (SELECT name, score, " + fn +
           "() OVER (ORDER BY score DESC) AS x FROM scores) WHERE x BETWEEN %d AND %d" % (lo, hi))
    return [(r[0], r[1]) for r in conn.execute(sql)]

print("第 2 页 每页 2 个名次 即名次 2 到 3:")
print("  ROW_NUMBER ->", page("ROW_NUMBER", 2, 3), "恰好两人 并列由 id 决出先后 确定性分页")
print("  RANK       ->", page("RANK", 2, 3), "rk 跳过了 3 下一段名次被整页吞掉")
print("  DENSE_RANK ->", page("DENSE_RANK", 2, 3), "名次等级连续 92 与 88 两档都进来 页面变大")

# 去重效果: 同分只保留一行 用 ROW_NUMBER 按值分区取第一
dedup = conn.execute("""
SELECT name, score FROM (
    SELECT name, score, ROW_NUMBER() OVER (PARTITION BY score ORDER BY id) AS rn
    FROM scores) WHERE rn = 1 ORDER BY score DESC""").fetchall()
print("按 score 去重保留首个 ->", dedup)

# DENSE_RANK 的去重口径: 名次等级数就是去重后的档数
levels = conn.execute(
    "SELECT COUNT(DISTINCT score), MAX(dr) FROM "
    "(SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS dr FROM scores)").fetchone()
print("分数档数与 DENSE_RANK 最大值 ->", levels, " 两者相等")
print("结论: 分页要确定性就 ROW_NUMBER 加 tie-breaker 要名次语义就 DENSE_RANK RANK 的跳号会让按名次翻页丢段")
