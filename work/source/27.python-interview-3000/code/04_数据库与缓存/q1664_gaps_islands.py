"""gaps-and-islands: 连续登录检测, 日期偏移与自关联的两种实现"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE login(user_id INTEGER, day TEXT)")
conn.executemany("INSERT INTO login VALUES(?,?)",
                 [(1, "2026-10-01"), (1, "2026-10-02"), (1, "2026-10-03"),
                  (1, "2026-10-05"), (1, "2026-10-06"),
                  (2, "2026-10-01"), (2, "2026-10-03"), (2, "2026-10-04")])
conn.commit()

# 实现一: 日期减去行号在同一段连续日期内是常数, 以此分岛
sql_win = """
WITH d AS (
  SELECT user_id, day,
         ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY day) AS rn
  FROM (SELECT DISTINCT user_id, day FROM login)
)
SELECT user_id, MIN(day) AS run_start, MAX(day) AS run_end, COUNT(*) AS days
FROM d
GROUP BY user_id, julianday(day) - rn
ORDER BY user_id, run_start
"""
print("窗口函数版连续段:")
for uid, s, e, n in conn.execute(sql_win):
    print(f"  用户{uid}: {s} ~ {e} 连续 {n} 天")

# 实现二: 无窗口函数的老库解法, 用自关联找"岛起点"与"岛终点"
sql_join = """
WITH d AS (SELECT DISTINCT user_id, day FROM login)
SELECT s.user_id, s.day AS seg_start,
       (SELECT MIN(e.day) FROM d e
         WHERE e.user_id = s.user_id AND e.day >= s.day
           AND NOT EXISTS (SELECT 1 FROM d f WHERE f.user_id = e.user_id
                 AND julianday(f.day) - julianday(e.day) = 1)) AS seg_end
FROM d s
WHERE NOT EXISTS (SELECT 1 FROM d p WHERE p.user_id = s.user_id
        AND julianday(s.day) - julianday(p.day) = 1)
ORDER BY s.user_id, seg_start
"""
print("自关联版岛起点与终点:", conn.execute(sql_join).fetchall())
print("要点: 岛起点 = 没有前一天的行; 岛终点 = 没有后一天的行; 方向写反会得到错误的岛边界")
