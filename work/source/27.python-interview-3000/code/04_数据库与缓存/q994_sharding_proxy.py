"""最小分片中间件: SQL 路由 -> 改写 -> 结果归并"""
import sqlite3

class MiniShardingProxy:
    def __init__(self, shards=4):
        self.shards = shards
        self.conns = [sqlite3.connect(":memory:") for _ in range(shards)]
        for c in self.conns:
            c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INT, amt REAL)")

    def route(self, user_id):
        return hash(user_id) % self.shards

    def insert(self, user_id, amt):
        idx = self.route(user_id)
        self.conns[idx].execute(
            "INSERT INTO orders (user_id, amt) VALUES (?, ?)", (user_id, amt))
        self.conns[idx].commit()
        return idx

    def query_by_user(self, user_id):              # 带分片键: 单片路由
        idx = self.route(user_id)
        return self.conns[idx].execute(
            "SELECT * FROM orders WHERE user_id = ?", (user_id,)).fetchall()

    def query_all(self):                            # 无分片键: 广播归并
        rows = []
        for c in self.conns:
            rows.extend(c.execute("SELECT * FROM orders").fetchall())
        return sorted(rows)                          # 归并排序

if __name__ == "__main__":
    proxy = MiniShardingProxy()
    for uid, amt in [(1, 10), (5, 20), (9, 30), (1, 40)]:
        print(f"user {uid} 路由到分片 {proxy.insert(uid, amt)}")
    print("带分片键查询:", proxy.query_by_user(1))
    print("广播归并:", proxy.query_all())
