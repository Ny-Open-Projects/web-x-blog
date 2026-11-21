"""事务边界三种划分: 语句级 请求级 业务级 的后果与耗时对比"""
import sqlite3
import time


def setup():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
    CREATE TABLE account(id INTEGER PRIMARY KEY, name TEXT, bal INTEGER);
    INSERT INTO account VALUES(1,'a',100),(2,'b',0);
    CREATE TABLE audit(id INTEGER PRIMARY KEY AUTOINCREMENT, txt TEXT);
    """)
    return conn


def transfer_stmt_level(conn, frm, to, amt):
    """语句级: 每条语句各自提交, 中途失败留下半截状态"""
    conn.execute("UPDATE account SET bal=bal-? WHERE id=?", (amt, frm))
    conn.commit()
    if amt > 50:
        raise ValueError("风控: 单笔超限")
    conn.execute("UPDATE account SET bal=bal+? WHERE id=?", (amt, to))
    conn.commit()


def transfer_request_level(conn, call_external):
    """请求级: 整个请求一个事务, 事务里夹外部调用就会被拉长"""
    conn.execute("BEGIN IMMEDIATE")
    conn.execute("UPDATE account SET bal=bal-10 WHERE id=1")
    t0 = time.perf_counter()
    call_external()                        # 事故点: 事务内调外部接口
    held_ms = (time.perf_counter() - t0) * 1000
    conn.execute("UPDATE account SET bal=bal+10 WHERE id=2")
    conn.commit()
    return held_ms


def transfer_business_level(conn, frm, to, amt):
    """业务级: 一个业务操作一个事务, 全成或全滚, 审计同框"""
    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute("UPDATE account SET bal=bal-? WHERE id=?", (amt, frm))
        if amt > 50:
            raise ValueError("风控: 单笔超限")
        conn.execute("UPDATE account SET bal=bal+? WHERE id=?", (amt, to))
        conn.execute("INSERT INTO audit(txt) VALUES(?)",
                     ("transfer %d->%d %d" % (frm, to, amt),))
        conn.commit()
        return True
    except ValueError:
        conn.rollback()
        return False


conn = setup()
try:
    transfer_stmt_level(conn, 1, 2, 60)
except ValueError as e:
    print("语句级失败:", e)
print("  余额:", conn.execute("SELECT bal FROM account ORDER BY id").fetchall(),
      "<- 扣款已提交 收款丢失")

held = transfer_request_level(conn, lambda: time.sleep(0.2))
print("请求级: 事务内夹外部调用, 行锁与连接被白占 %.0f ms" % held)

ok = transfer_business_level(conn, 1, 2, 60)
print("业务级失败返回:", ok, "余额:",
      conn.execute("SELECT bal FROM account ORDER BY id").fetchall(),
      "<- 原样未动")
ok = transfer_business_level(conn, 1, 2, 25)
print("业务级成功:", ok, "余额:",
      conn.execute("SELECT bal FROM account ORDER BY id").fetchall(),
      "审计:", conn.execute("SELECT COUNT(*) FROM audit").fetchone()[0], "条")
