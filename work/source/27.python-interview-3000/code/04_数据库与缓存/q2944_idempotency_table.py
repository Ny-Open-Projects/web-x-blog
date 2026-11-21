"""幂等表完整写入流程: 同事务占位 业务与结果落库 重放零副作用"""
import json
import sqlite3

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
conn.executescript("""
CREATE TABLE idem(msg_id TEXT PRIMARY KEY, status TEXT, result TEXT);
CREATE TABLE balance(uid INTEGER PRIMARY KEY, bal INTEGER);
INSERT INTO balance VALUES(7, 100);
""")


def handle(msg_id, uid, amt):
    # 第 1 步: 事务内占位, 抢不到说明处理过或正在处理
    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute("INSERT INTO idem VALUES(?,?,NULL)", (msg_id, "processing"))
    except sqlite3.IntegrityError:
        conn.rollback()
        row = conn.execute("SELECT status, result FROM idem WHERE msg_id=?",
                           (msg_id,)).fetchone()
        if row["status"] == "done":
            return "replay", json.loads(row["result"])
        return "in_progress", None
    # 第 2 步: 业务写入 + 结果回填 + 状态翻转, 与占位同一个事务
    conn.execute("UPDATE balance SET bal=bal+? WHERE uid=?", (amt, uid))
    result = {"bal": conn.execute(
        "SELECT bal FROM balance WHERE uid=?", (uid,)).fetchone()[0]}
    conn.execute("UPDATE idem SET status='done', result=? WHERE msg_id=?",
                 (json.dumps(result), msg_id))
    conn.commit()
    return "done", result


print("首次:", handle("m1", 7, 30))
print("重放:", handle("m1", 7, 30))
bal = conn.execute("SELECT bal FROM balance WHERE uid=7").fetchone()[0]
print("余额:", bal, "(只加了一次)")
conn.execute("INSERT INTO idem VALUES('m2','processing',NULL)")  # 模拟他人在途
conn.commit()
print("处理中再来:", handle("m2", 7, 50))
print("最终余额:", conn.execute("SELECT bal FROM balance WHERE uid=7").fetchone()[0])
assert bal == 130
