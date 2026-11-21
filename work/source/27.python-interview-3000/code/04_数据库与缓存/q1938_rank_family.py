"""RANK DENSE_RANK ROW_NUMBER: 并列名次的三种口径"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE scores(name TEXT, score INTEGER)")
conn.executemany("INSERT INTO scores VALUES(?,?)", [
    ("alice", 95), ("bob", 92), ("carol", 92), ("dave", 88), ("eve", 88), ("frank", 80)])

q = """
SELECT name, score,
       ROW_NUMBER() OVER (ORDER BY score DESC) AS rn,
       RANK()       OVER (ORDER BY score DESC) AS rk,
       DENSE_RANK() OVER (ORDER BY score DESC) AS dr
FROM scores"""
print("name     score  rn  rk  dr")
for r in conn.execute(q):
    print("%-8s %5d  %2d  %2d  %2d" % r)

# 三种口径各取前 3: 语义与结果集大小都不同
def top_by(fn):
    return [r[0] for r in conn.execute(
        "SELECT name FROM (SELECT name, " + fn +
        "() OVER (ORDER BY score DESC) AS x FROM scores) WHERE x <= 3")]

limit3 = [r[0] for r in conn.execute("SELECT name FROM scores ORDER BY score DESC LIMIT 3")]
print("LIMIT 3    ->", limit3, "纯行数截断 并列被硬拆")
print("ROW_NUMBER ->", top_by("ROW_NUMBER"), "每行唯一序号 并列被任意先后拆开")
print("RANK       ->", top_by("RANK"), "并列同名次 92 分两人都算第 2 会多取一行")
print("DENSE_RANK ->", top_by("DENSE_RANK"), "不跳号 前 3 个名次等级把 88 分也带进来")
print("结论: 取 N 条用 ROW_NUMBER 并补 tie-breaker; 取前 N 个名次等级用 DENSE_RANK; RANK 跳号会让按名次分页出现空洞")
