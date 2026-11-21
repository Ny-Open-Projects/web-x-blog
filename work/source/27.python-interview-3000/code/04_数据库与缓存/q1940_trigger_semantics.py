"""触发器执行语义: 时机 粒度与应用层替代方案对比"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE account(id INTEGER PRIMARY KEY, balance INTEGER)")
conn.execute("CREATE TABLE audit(id INTEGER PRIMARY KEY, account_id INTEGER, old INTEGER, new INTEGER, src TEXT)")
conn.execute("INSERT INTO account VALUES(1, 100)")

# AFTER UPDATE + FOR EACH ROW: 每受影响行触发一次 WHEN 充当行级守卫
conn.execute("""
CREATE TRIGGER trg_balance_audit AFTER UPDATE ON account
FOR EACH ROW
WHEN OLD.balance <> NEW.balance
BEGIN
    INSERT INTO audit(account_id, old, new, src)
    VALUES(OLD.id, OLD.balance, NEW.balance, 'trigger');
END""")

conn.execute("UPDATE account SET balance = 120 WHERE id = 1")   # 变动 触发
conn.execute("UPDATE account SET balance = 120 WHERE id = 1")   # 值没变 WHEN 拦下
conn.execute("UPDATE account SET balance = 90 WHERE id = 1")    # 再触发
print("触发器审计记录 ->", conn.execute("SELECT account_id, old, new, src FROM audit").fetchall())
print("三次 UPDATE 两次落审计: FOR EACH ROW 按行触发 WHEN 过滤无效变更")

# 应用层等价实现: 逻辑显式 可评审可测试 但要防直连写库绕过
def change_balance(cur, account_id, new_balance):
    old = cur.execute("SELECT balance FROM account WHERE id = ?", (account_id,)).fetchone()[0]
    if old != new_balance:
        cur.execute("UPDATE account SET balance = ? WHERE id = ?", (new_balance, account_id))
        cur.execute("INSERT INTO audit(account_id, old, new, src) VALUES(?,?,?,?)",
                    (account_id, old, new_balance, "app"))

change_balance(conn.cursor(), 1, 70)
print("应用层审计累计 ->", conn.execute("SELECT COUNT(*) FROM audit").fetchone()[0], "条")
print("结论: 触发器保证任何入口都受控但逻辑隐身于库 应用层可见可测但存在绕过路径 二选一要全团队一致")
