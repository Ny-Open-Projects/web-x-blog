"""回滚脚本必备要素: 幂等 备份与验证断言"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, email TEXT, dept TEXT);
INSERT INTO users VALUES(1,'alice','a@x.com','eng'),(2,'bob','b@x.com','ops');
""")
FORWARD = """
ALTER TABLE users ADD COLUMN dept_code TEXT;
UPDATE users SET dept_code = lower(dept);
"""

def column_exists(cur, table, col):
    return any(r[1] == col for r in cur.execute("PRAGMA table_info(%s)" % table))

def drop_column(cur, table, col):
    """sqlite 旧版没有 DROP COLUMN 用改名 重建 拷回 三步删除
    正式脚本要按原始 DDL 重建以保留约束 这里从简"""
    cols = [r[1] for r in cur.execute("PRAGMA table_info(%s)" % table) if r[1] != col]
    cur.execute("ALTER TABLE %s RENAME TO %s_old" % (table, table))
    cur.execute("CREATE TABLE %s AS SELECT %s FROM %s_old" % (table, ",".join(cols), table))
    cur.execute("DROP TABLE %s_old" % table)

def rollback(c):
    cur = c.cursor()
    log = []
    if column_exists(cur, "users", "dept_code"):
        # 要素一: 幂等 先检查现状 重复执行直接跳过
        # 要素二: 销毁数据前先备份成 _rbk 表 可追溯
        cur.execute("CREATE TABLE IF NOT EXISTS users_rbk AS SELECT id, dept_code FROM users")
        drop_column(cur, "users", "dept_code")
        log.append("已删除 dept_code 且快照在 users_rbk")
    # 要素三: 回滚后验证断言 不通过要报警而不是静默成功
    if column_exists(cur, "users", "dept_code"):
        log.append("验证失败: 列仍存在")
    else:
        log.append("验证通过: 结构已还原")
    n = cur.execute("SELECT COUNT(*) FROM users WHERE dept IS NULL").fetchone()[0]
    log.append("业务字段完整性: %d 行 dept 为空" % n)
    c.commit()
    return log

conn.executescript(FORWARD)
print("正向迁移后 ->", conn.execute("SELECT id, dept_code FROM users").fetchall())
print("第一次回滚 ->", rollback(conn))
print("第二次回滚 ->", rollback(conn), " 幂等 重复执行无副作用")
print("结论: 回滚脚本四要素 幂等可重入 数据先备份 验证断言 顺序与正向严格相反 且必须在预发演练过")
