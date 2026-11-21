"""综合案例: 订单超时关闭的可靠实现, 延迟任务 + 条件状态机 + 对账兜底"""
import sqlite3

NOW = 1000.0          # 模拟时钟
TTL = 10.0            # 订单 10 秒未支付自动关闭

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE orders(no TEXT PRIMARY KEY, status TEXT, created_at REAL);
CREATE TABLE repay(no TEXT PRIMARY KEY, due REAL, done INTEGER DEFAULT 0);  -- 延迟任务表
""")

def create_order(no):
    """下单: 业务行与延迟任务同事务落库(本地消息表思想的定时版)"""
    conn.execute("INSERT INTO orders VALUES(?, 'created', ?)", (no, NOW))
    conn.execute("INSERT INTO repay VALUES(?, ?, 0)", (no, NOW + TTL))
    conn.commit()
    print(f"  下单 {no}, 关闭任务定在 {NOW + TTL:.0f}")

def pay(no, t):
    """支付: 条件状态机更新, 已关闭则走退款补偿"""
    cur = conn.execute(
        "UPDATE orders SET status='paid' WHERE no=? AND status='created'", (no,))
    conn.commit()
    if cur.rowcount:
        conn.execute("UPDATE repay SET done=1 WHERE no=?", (no,))
        conn.commit()
        print(f"  {no} 在 {t:.0f} 支付成功, 取消定时任务")
        return "paid"
    print(f"  {no} 已关闭, 支付转入退款流程")
    return "refund"

def closer(now):
    """定时扫描: 只处理到期任务, 关单动作是条件更新保证幂等"""
    rows = conn.execute(
        "SELECT no FROM repay WHERE done=0 AND due<=? ORDER BY due", (now,)).fetchall()
    closed = []
    for (no,) in rows:
        cur = conn.execute(
            "UPDATE orders SET status='closed' WHERE no=? AND status='created'", (no,))
        conn.execute("UPDATE repay SET done=1 WHERE no=?", (no,))
        conn.commit()
        if cur.rowcount:
            closed.append(no)
    return closed

def reconcile(now):
    """对账兜底: 扫 orders 里 created 且超过 TTL 的单, 修复漏关"""
    missed = [r[0] for r in conn.execute(
        "SELECT no FROM orders WHERE status='created' AND created_at+?<=?", (TTL, now))]
    for no in missed:
        conn.execute(
            "UPDATE orders SET status='closed' WHERE no=? AND status='created'", (no,))
        conn.commit()
    return missed

print("t=1000:")
create_order("SO-1")
create_order("SO-2")
print("t=1005: SO-1 支付")
pay("SO-1", 1005)
print("t=1011 定时器扫描, 关闭:", closer(1011))
print("t=1015: SO-2 迟到支付")
pay("SO-2", 1015)
print("对账巡检(应零差异):", reconcile(1015))
# 模拟任务行丢失: 定时器永远关不了它
conn.execute("INSERT INTO orders VALUES('SO-3', 'created', 1000)")
conn.execute("DELETE FROM repay WHERE no='SO-3'")
conn.commit()
print("SO-3 丢失定时任务, 到期后对账巡检修复:", reconcile(1020))
print("最终状态:", conn.execute("SELECT no, status FROM orders ORDER BY no").fetchall())
print("设计要点: 三层防线 = 延迟任务 条件状态机幂等 对账兜底, 任何一层失效都不丢关闭语义")
