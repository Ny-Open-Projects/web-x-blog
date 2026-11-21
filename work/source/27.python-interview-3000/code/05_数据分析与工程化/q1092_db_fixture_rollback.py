import sqlite3

def make_conn():
    conn = sqlite3.connect(":memory:", isolation_level=None)  # 手动控制事务
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("BEGIN")
    return conn

class DBFixture:
    """每个测试一个事务,结束回滚,数据零残留"""

    def __init__(self):
        self.conn = make_conn()

    def add(self, name):
        self.conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
        return self.conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    def count(self):
        return self.conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]

    def rollback(self):
        self.conn.execute("ROLLBACK")

if __name__ == "__main__":
    db = DBFixture()
    db.add("alice")
    db.add("bob")
    assert db.count() == 2
    db.rollback()
    assert db.count() == 0, "回滚后应零残留,测试间天然隔离"
    print("事务回滚隔离验证通过")
