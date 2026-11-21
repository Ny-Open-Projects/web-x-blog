"""version 字段并发写演示: 两个会话同一版本的提交只有一方成功"""
import sqlite3

class ConcurrentUpdate(Exception):
    pass

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE doc(id INTEGER PRIMARY KEY, title TEXT, version INTEGER)")
conn.execute("INSERT INTO doc VALUES(1, 'v0', 1)")
conn.commit()

class FakeSession:
    """模拟一个 ORM 会话: 读入时记版本快照, flush 时按版本条件更新"""

    def __init__(self, conn, label):
        self.conn, self.label = conn, label
        self.obj = None

    def load(self):
        row = self.conn.execute(
            "SELECT id, title, version FROM doc WHERE id=1").fetchone()
        self.obj = {"id": row[0], "title": row[1], "version": row[2]}
        return self

    def rename(self, title):
        self.obj["title"] = title

    def flush(self):
        o = self.obj
        cur = self.conn.execute(
            "UPDATE doc SET title=?, version=version+1 WHERE id=? AND version=?",
            (o["title"], o["id"], o["version"]))
        self.conn.commit()
        if cur.rowcount == 0:
            raise ConcurrentUpdate(
                f"版本过期: 期望 version={o['version']}, 数据库已是更高版本")
        print(f"[{self.label}] 提交成功, version 升到 {o['version'] + 1}")

a = FakeSession(conn, "会话A").load()
b = FakeSession(conn, "会话B").load()
a.rename("A 改的标题")
b.rename("B 改的标题")
a.flush()
try:
    b.flush()
except ConcurrentUpdate as e:
    print("[会话B] 冲突:", e, "-> 重读合并后重试")
b = FakeSession(conn, "会话B").load()
b.rename("B 基于最新版合并的结果")
b.flush()
print("最终:", conn.execute("SELECT title, version FROM doc WHERE id=1").fetchone())
print("要点: UPDATE 的 WHERE version=? 让丢失更新变成显式冲突;")
print("      冲突处理要么重试要么提示用户, 静默覆盖是最差选择")
