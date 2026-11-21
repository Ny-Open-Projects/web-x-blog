"""按 user_id 取模路由到 16 张分表, 含跨片查询兜底"""
import sqlite3

N_SHARDS = 16

def shard_table(user_id):
    return f"orders_{user_id % N_SHARDS:02d}"

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    for i in range(N_SHARDS):
        conn.execute(f"""CREATE TABLE orders_{i:02d}
                         (id INTEGER PRIMARY KEY, user_id INT, amt REAL)""")
    rows = [(uid, amt) for uid in range(100) for amt in (10.0, 20.0)]
    for uid, amt in rows:
        conn.execute(f"INSERT INTO {shard_table(uid)} (user_id, amt) VALUES (?, ?)",
                     (uid, amt))

    uid = 77
    print(f"user {uid} 路由到 {shard_table(uid)}:",
          conn.execute(f"SELECT * FROM {shard_table(uid)} WHERE user_id = ?",
                       (uid,)).fetchall())

    # 跨片兜底: UNION ALL 视图思路(仅限低频管理查询)
    union_sql = " UNION ALL ".join(
        f"SELECT user_id, amt FROM orders_{i:02d}" for i in range(N_SHARDS))
    total = conn.execute(
        f"SELECT count(*) FROM ({union_sql}) WHERE user_id = ?", (uid,)).fetchone()[0]
    print("广播查询结果:", total, "<- 应避免, 业务设计保证带路由键")
