"""清洗键分组: 归一化表达式聚合与物化列替代"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE lead (id INTEGER PRIMARY KEY, phone TEXT)")
pats = ["138-0000-%04d", "138 0000 %04d", "+861380000%04d", "1380000%04d"]
rows = []
i = 0
for k in range(1000):
    for pat in pats:
        i += 1
        rows.append((i, pat % (k % 300)))
c.executemany("INSERT INTO lead VALUES(?,?,?)".replace("?,?,?", "?,?"), rows) if False else \
    c.executemany("INSERT INTO lead VALUES(?,?)", rows)

NORM = "REPLACE(REPLACE(REPLACE(phone, '-', ''), ' ', ''), '+86', '')"

t0 = time.perf_counter()
dup = c.execute("""SELECT COUNT(*) FROM (
  SELECT %s AS p, COUNT(*) AS n FROM lead GROUP BY p HAVING n > 1)""" % NORM).fetchone()[0]
expr_ms = (time.perf_counter() - t0) * 1000
print("表达式分组: %d 个号码存在多格式重复, 耗时 %.1f ms" % (dup, expr_ms))

c.execute("ALTER TABLE lead ADD COLUMN clean TEXT")
c.execute("UPDATE lead SET clean = " + NORM)
c.execute("CREATE INDEX idx_clean ON lead(clean)")
t0 = time.perf_counter()
dup2 = c.execute("""SELECT COUNT(*) FROM (
  SELECT clean, COUNT(*) AS n FROM lead GROUP BY clean HAVING n > 1)""").fetchone()[0]
col_ms = (time.perf_counter() - t0) * 1000
print("物化列分组: 同样 %d 个, 耗时 %.1f ms (索引在手, 大表上差距放大)" % (dup2, col_ms))
