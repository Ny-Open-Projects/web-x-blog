"""订正的快照留痕: 旧值入档, 一键回滚"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, status TEXT, balance INTEGER)")
c.execute("""CREATE TABLE fix_log (
    batch_id TEXT, tbl TEXT, pk INTEGER, col TEXT, old TEXT, new TEXT, at INTEGER)""")
c.executemany("INSERT INTO accounts VALUES(?,?,?)",
              [(1, "active", 100), (2, "active", 200), (3, "frozen", 300)])
conn.commit()

def apply_fix(batch, where_sql, set_sql, args):
    rows = c.execute("SELECT id, status, balance FROM accounts WHERE " + where_sql,
                     args).fetchall()
    now = int(time.time())
    c.execute("BEGIN")
    for rid, st, bal in rows:                      # 先留痕: 记录会被改的每一列旧值
        c.execute("INSERT INTO fix_log VALUES(?,?,?,?,?,?,?)",
                  (batch, "accounts", rid, "status", st, None, now))
        c.execute("INSERT INTO fix_log VALUES(?,?,?,?,?,?,?)",
                  (batch, "accounts", rid, "balance", str(bal), None, now))
    c.execute("UPDATE accounts SET " + set_sql + " WHERE " + where_sql, args)
    c.execute("UPDATE fix_log SET new = 'written' WHERE batch_id = ? AND new IS NULL", (batch,))
    c.execute("COMMIT")
    return len(rows)

batch = "fix-20261105-01"
n = apply_fix(batch, "status = 'active'", "status = 'frozen', balance = 0", ())
print("订正 %s: 冻结 %d 个账户, 每列旧值已入档" % (batch, n))

def rollback(batch):
    c.execute("BEGIN")
    for pk, col, old in c.execute(
            "SELECT pk, col, old FROM fix_log WHERE batch_id = ?", (batch,)).fetchall():
        c.execute("UPDATE accounts SET %s = ? WHERE id = ?" % col, (old, pk))
    c.execute("DELETE FROM fix_log WHERE batch_id = ?", (batch,))
    c.execute("COMMIT")

rollback(batch)
print("回滚后账户:", c.execute("SELECT id, status, balance FROM accounts ORDER BY id").fetchall())
assert c.execute("SELECT COUNT(*) FROM accounts WHERE status='active'").fetchone()[0] == 2
print("结论: 订正留痕的本质是'应用级 undo log', 按批次组织, 回滚是重放旧值;")
print("      它救不了删除行的恢复 (那要靠备份), 但覆盖了绝大多数 UPDATE 类订正事故")
