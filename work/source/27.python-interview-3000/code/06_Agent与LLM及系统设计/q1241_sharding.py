"""分库分表:hash 路由 + 跨片查询 fan-out + 翻倍扩容迁移量分析。"""
from collections import defaultdict


class ShardedDB:
    def __init__(self, n_dbs, n_tables):
        self.n_dbs, self.n_tables = n_dbs, n_tables
        self.shards = defaultdict(list)            # (db, table) -> rows

    def route(self, user_id):
        db = user_id % self.n_dbs
        table = (user_id // self.n_dbs) % self.n_tables
        return db, table

    def insert(self, user_id, row):
        self.shards[self.route(user_id)].append({"user_id": user_id, **row})

    def query_by_user(self, user_id):
        """分片内按 user_id 过滤:同一分片存多个用户。"""
        return [r for r in self.shards[self.route(user_id)] if r["user_id"] == user_id]

    def query_all_users(self):
        """跨片查询:广播聚合,演示其代价。"""
        scanned = sum(len(v) for v in self.shards.values())
        rows = [r for v in self.shards.values() for r in v]
        return rows, scanned

    def migration_ratio_on_double(self, user_ids):
        """翻倍扩容:仅 user_id%old_db 落在新半区的数据移动。"""
        moved = sum(1 for uid in user_ids if (uid % (self.n_dbs * 2)) >= self.n_dbs)
        return moved / len(user_ids)


if __name__ == "__main__":
    db = ShardedDB(n_dbs=4, n_tables=4)
    for uid in range(1000, 1032):
        db.insert(uid, {"amount": uid})
    rows = db.query_by_user(1003)
    print("user 1003 路由到:", db.route(1003), "->", rows)
    assert rows and all(r["user_id"] == 1003 for r in rows), "分片内按 user_id 精确过滤"

    rows_all, scanned = db.query_all_users()
    print(f"跨片聚合需扫描 {scanned} 行 across {len(db.shards)} 分片(代价高,应走宽表)")
    assert scanned == 32

    ratio = db.migration_ratio_on_double(list(range(1000, 2000)))
    print(f"4 库翻倍到 8 库迁移比例: {ratio:.0%}")
    assert 0.3 < ratio < 0.7, "翻倍扩容约一半数据迁移"
    print("路由确定性: 同一 user 永远命中同一分片")
