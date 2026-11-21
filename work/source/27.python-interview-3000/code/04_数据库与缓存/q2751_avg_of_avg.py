"""均值的均值不是均值: 分组 AVG 直接再 AVG 的偏差与两种修法"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE session (id INTEGER PRIMARY KEY, grp TEXT, dur REAL)")
rows = []
i = 0
for g, ds in [("a", [1, 2, 3]), ("b", [10.0] * 10)]:
    for d in ds:
        i += 1
        rows.append((i, g, d))
c.executemany("INSERT INTO session VALUES(?,?,?)", rows)

wrong = c.execute("""SELECT AVG(avg_dur) FROM
    (SELECT grp, AVG(dur) AS avg_dur FROM session GROUP BY grp)""").fetchone()[0]
right = c.execute("SELECT AVG(dur) FROM session").fetchone()[0]
weighted = c.execute("""SELECT SUM(cnt * avg_dur) / SUM(cnt) FROM
    (SELECT grp, AVG(dur) AS avg_dur, COUNT(*) AS cnt FROM session GROUP BY grp)""").fetchone()[0]
print("均值的均值 %.2f | 全局均值 %.2f | 按行数加权 %.2f" % (wrong, right, weighted))
print("a 组 3 行 b 组 10 行, 简单平均把 a 的权重抬到了一半, 偏差 %.0f%%"
      % (abs(wrong - right) / right * 100))
