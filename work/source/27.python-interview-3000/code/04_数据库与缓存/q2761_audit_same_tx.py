"""审计表与主表的事务同框: 回滚连审计一起回滚, 触发器保证不漏"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
c = conn.cursor()
c.execute("CREATE TABLE account (id INTEGER PRIMARY KEY, owner TEXT, bal INTEGER)")
c.execute("""CREATE TABLE audit (
    id INTEGER PRIMARY KEY AUTOINCREMENT, account_id INTEGER,
    delta INTEGER, note TEXT, at TEXT DEFAULT (datetime('now')))""")
c.execute("""CREATE TRIGGER account_audit AFTER UPDATE ON account
  WHEN OLD.bal <> NEW.bal
  BEGIN
    INSERT INTO audit(account_id, delta, note) VALUES(NEW.id, NEW.bal - OLD.bal, 'balance');
  END""")
c.execute("INSERT INTO account VALUES(1, 'alice', 100)")

c.execute("BEGIN")                          # 成功路径: 业务与审计同事务落盘
c.execute("UPDATE account SET bal = bal - 30 WHERE id=1")
c.execute("COMMIT")
print("扣款 30 后审计:", c.execute("SELECT account_id, delta, note FROM audit").fetchall())

c.execute("BEGIN")                          # 失败路径: 业务回滚, 审计必须一起消失
c.execute("UPDATE account SET bal = bal + 999 WHERE id=1")
c.execute("ROLLBACK")
n = c.execute("SELECT COUNT(*) FROM audit WHERE delta=999").fetchone()[0]
print("回滚后 delta=999 的审计条数: %d (0 才对, 审计与业务同生死)" % n)
print("最终账实:", c.execute("SELECT bal FROM account WHERE id=1").fetchone()[0])
conn.close()
