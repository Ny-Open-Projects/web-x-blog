"""原子交换: 唯一约束下直接换位撞约束, 借道中转值三步完成"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
c = conn.cursor()
c.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, pos INTEGER UNIQUE, title TEXT)")
c.executemany("INSERT INTO todo VALUES(?,?,?)", [(1, 1, "买牛奶"), (2, 2, "写周报")])

try:
    c.execute("BEGIN")
    c.execute("UPDATE todo SET pos=2 WHERE id=1")   # 第一步就撞上 id=2 现有的 pos=2
    c.execute("UPDATE todo SET pos=1 WHERE id=2")
    c.execute("COMMIT")
    print("直接交换竟然成功, 不应到这里")
except sqlite3.IntegrityError as e:
    c.execute("ROLLBACK")
    print("直接交换撞约束: %s (事务已整体回滚)" % e)

c.execute("BEGIN")
c.execute("UPDATE todo SET pos=-1 WHERE id=1")      # 借道负数域, 挪出冲突
c.execute("UPDATE todo SET pos=1 WHERE id=2")
c.execute("UPDATE todo SET pos=2 WHERE id=1")
c.execute("COMMIT")
print("借道换位后:", c.execute("SELECT id, pos, title FROM todo ORDER BY pos").fetchall())
print("要点: 中间态非法是约束的错也是设计的题, 中转值把非法中间态藏进事务内部")
