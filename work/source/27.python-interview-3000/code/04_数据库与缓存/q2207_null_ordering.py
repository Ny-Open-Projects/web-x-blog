"""NULL 排序位置控制: NULLS FIRST/LAST 与 IS NULL 技巧"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE tasks(id INTEGER PRIMARY KEY, due TEXT)")
c.executemany("INSERT INTO tasks(due) VALUES(?)",
              [("2026-03-01",), (None,), ("2026-01-15",), (None,), ("2026-02-01",)])

def show(label, sql):
    rows = [r[0] if r[0] is not None else "NULL" for r in c.execute(sql)]
    print("%-24s -> %s" % (label, rows))

show("ORDER BY due ASC 默认", "SELECT due FROM tasks ORDER BY due ASC")
show("ORDER BY due DESC 默认", "SELECT due FROM tasks ORDER BY due DESC")
show("ASC NULLS LAST", "SELECT due FROM tasks ORDER BY due ASC NULLS LAST")
show("DESC NULLS FIRST", "SELECT due FROM tasks ORDER BY due DESC NULLS FIRST")
show("技巧 IS NULL 升序", "SELECT due FROM tasks ORDER BY (due IS NULL), due ASC")
show("技巧 IS NULL 降序", "SELECT due FROM tasks ORDER BY (due IS NULL), due DESC")
print("SQLite 视 NULL 为最小值, 老版本没有 NULLS LAST 时用 IS NULL 技巧, 行为跨库一致")
