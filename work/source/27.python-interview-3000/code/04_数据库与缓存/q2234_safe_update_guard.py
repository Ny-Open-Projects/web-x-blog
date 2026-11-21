"""忘加 WHERE 的危险 UPDATE: 客户端闸门加影响行数断言"""
import re
import sqlite3

conn = sqlite3.connect(":memory:")
conn.isolation_level = None    # 关闭隐式事务, BEGIN COMMIT ROLLBACK 全部显式控制
c = conn.cursor()
c.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, level INTEGER, banned INTEGER)")
c.executemany("INSERT INTO users VALUES(?,?,?)", [(1, 1, 0), (2, 2, 0), (3, 1, 0)])

DANGER = re.compile(r"^\s*(UPDATE|DELETE)\s+(?!.*\bWHERE\b)", re.I | re.S)

def guarded_execute(conn, sql, max_affected=1000):
    if DANGER.match(sql):
        raise ValueError("拒绝执行: UPDATE 或 DELETE 缺少 WHERE")
    cur = conn.cursor()
    cur.execute("BEGIN")
    cur.execute(sql)
    n = cur.rowcount
    if n > max_affected:
        cur.execute("ROLLBACK")
        raise ValueError("影响 %d 行超过阈值 %d, 已回滚" % (n, max_affected))
    conn.commit()
    return n

try:
    guarded_execute(conn, "UPDATE users SET level = 9")
except ValueError as e:
    print("闸门拦截:", e)

n = guarded_execute(conn, "UPDATE users SET banned = 1 WHERE id = 2")
print("正常执行影响 %d 行" % n)
try:
    guarded_execute(conn, "DELETE FROM users WHERE level = 1", max_affected=1)
except ValueError as e:
    print("阈值拦截:", e)
print("库内现状:", c.execute("SELECT id, level, banned FROM users").fetchall())
print("闸门最便宜, sql_safe_updates 与账号权限是服务端兜底, review 只是最后一层")
