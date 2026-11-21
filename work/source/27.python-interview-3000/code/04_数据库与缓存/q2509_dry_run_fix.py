"""数据订正的 dry-run: 先预览影响集, 后执行并断言行数"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, currency TEXT, amount INTEGER)")
rows = []
for i in range(1, 201):
    cur = "USD" if i % 10 == 0 else "CNY"      # 20 条错误标成 USD 的脏数据
    rows.append((i, cur, 100 + i))
c.executemany("INSERT INTO orders VALUES(?,?,?)", rows)
conn.commit()

WHERE = "currency = 'USD'"                      # 订正条件只写一处, 预览与执行共用
def run_fix(dry_run):
    preview = c.execute(
        "SELECT id, amount FROM orders WHERE " + WHERE + " ORDER BY id").fetchall()
    if dry_run:
        print("  [dry-run] 将影响 %d 行, 样例: %s ... %s"
              % (len(preview), preview[:2], preview[-1:]))
        return len(preview), 0
    c.execute("BEGIN")
    c.execute("UPDATE orders SET currency='CNY', amount = amount * 7 WHERE " + WHERE)
    affected = c.rowcount
    c.execute("COMMIT")
    return len(preview), affected

n_preview, _ = run_fix(dry_run=True)
_, n_affected = run_fix(dry_run=False)
assert n_preview == n_affected, "影响行数与预览不一致, 立即停止"
print("执行后核对: 预览 %d 行 == 实际 %d 行, 断言通过" % (n_preview, n_affected))
left = c.execute("SELECT COUNT(*) FROM orders WHERE currency='USD'").fetchone()[0]
print("残留 USD 行数: %d" % left)

# 再跑一遍 dry-run: 影响集必须为空, 证明订正是幂等收口的
n2, _ = run_fix(dry_run=True)
print("二次 dry-run 影响行数: %d   <- 为 0 才算订正干净" % n2)
print("结论: 订正脚本必须 dry-run 与执行共用同一个 WHERE, 执行后拿 rowcount 对预览断言,")
print("      条件每次都要重新预览——数据是活的, 昨天的 WHERE 今天可能咬人")
