"""TCC 最小模型: 冻结-确认-取消 + 空回滚与幂等防护"""
import sqlite3

def setup():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE acct (id INTEGER PRIMARY KEY, bal INT, frozen INT DEFAULT 0);
        CREATE TABLE tx_log (txid TEXT, action TEXT, PRIMARY KEY (txid, action));
        INSERT INTO acct VALUES (1, 100, 0), (2, 0, 0);
    """)
    return conn

def once(conn, txid, action):
    try:
        conn.execute("INSERT INTO tx_log VALUES (?, ?)", (txid, action))
        return True
    except sqlite3.IntegrityError:
        return False                                # 幂等: 已执行过

def try_(conn, txid, amount):
    if not once(conn, txid, "try"):
        return "幂等跳过"
    conn.execute("UPDATE acct SET bal = bal - ?, frozen = frozen + ? WHERE id = 1",
                 (amount, amount))
    return "try 冻结完成"

def cancel(conn, txid, amount):
    done = once(conn, txid, "cancel")
    tried = conn.execute("SELECT 1 FROM tx_log WHERE txid=? AND action='try'",
                         (txid,)).fetchone()
    if not tried:
        conn.execute("INSERT INTO tx_log VALUES (?, 'try_null')", (txid,))
        return "空回滚: 未 try 过, 直接记取消成功"
    if not done:
        conn.execute("UPDATE acct SET bal = bal + ?, frozen = frozen - ? WHERE id = 1",
                     (amount, amount))
        return "cancel 释放冻结"
    return "cancel 幂等跳过"

def confirm(conn, txid, amount):
    if not once(conn, txid, "confirm"):
        return "confirm 幂等跳过"
    conn.execute("UPDATE acct SET frozen = frozen - ? WHERE id = 1", (amount,))
    conn.execute("UPDATE acct SET bal = bal + ? WHERE id = 2", (amount,))
    return "confirm 转账完成"

if __name__ == "__main__":
    conn = setup()
    print(try_(conn, "tx1", 30))
    print(confirm(conn, "tx1", 30))
    print(cancel(conn, "tx2", 50), "<- 空回滚演示")
    print("余额:", conn.execute("SELECT id, bal, frozen FROM acct").fetchall())
