"""修复动作自身的幂等: 对账修复任务重跑不产生二次伤害"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE acct(id INTEGER PRIMARY KEY, balance INTEGER);
CREATE TABLE repair_log(repair_id TEXT PRIMARY KEY, applied_at INTEGER);
""")
conn.executemany("INSERT INTO acct VALUES(?,?)", [(1, 0), (2, 0)])
conn.commit()

def apply_repair(repair_id, target_id, set_balance):
    """幂等修复: repair_id 唯一键防重入, 动作用绝对值 SET 而非相对值 INCREMENT"""
    cur = conn.execute(
        "INSERT OR IGNORE INTO repair_log(repair_id, applied_at) "
        "VALUES(?, strftime('%s','now'))", (repair_id,))
    conn.commit()
    if cur.rowcount == 0:
        return f"{repair_id} 已应用过, 跳过"
    conn.execute("UPDATE acct SET balance=? WHERE id=?", (set_balance, target_id))
    conn.commit()
    return f"{repair_id} 应用: acct {target_id} balance -> {set_balance}"

print(apply_repair("fix-2026-1105-001", 1, 100))
print(apply_repair("fix-2026-1105-001", 1, 100), "<- 同一修复单重跑")

# 反面教材: 相对值修复重跑会翻倍伤害
def bad_repair(target_id, delta):
    conn.execute("UPDATE acct SET balance=balance+? WHERE id=?", (delta, target_id))
    conn.commit()

bad_repair(2, 50)
bad_repair(2, 50)
print("相对值 INCREMENT 跑两次:", conn.execute(
    "SELECT balance FROM acct WHERE id=2").fetchone()[0], "(伤害翻倍)")
print("要点: 修复单要登记落库并以唯一键防重入; 动作语义用目标态 SET;")
print("      半途崩溃后重跑必须收敛到同一终态, 这是修复与普通任务的分界线")
