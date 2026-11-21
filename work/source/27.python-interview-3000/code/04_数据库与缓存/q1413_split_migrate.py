"""综合案例: 用户大表分表的迁移剧本(小规模演示)"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users_old(id INTEGER PRIMARY KEY, name TEXT)")
conn.execute("CREATE TABLE users_0(id INTEGER PRIMARY KEY, name TEXT)")
conn.execute("CREATE TABLE users_1(id INTEGER PRIMARY KEY, name TEXT)")
conn.executemany("INSERT INTO users_old VALUES(?,?)",
                 [(i, "user%d" % i) for i in range(1, 201)])

def shard_of(uid):
    return uid % 2                      # 真实场景用一致性哈希; 表名来自内部白名单

def migrate_all():                      # 阶段 2: 回填, OR IGNORE 保证幂等
    rows = conn.execute("SELECT id, name FROM users_old").fetchall()
    for uid, name in rows:
        conn.execute("INSERT OR IGNORE INTO users_%d VALUES(?,?)" % shard_of(uid),
                     (uid, name))
migrate_all()

n_old = conn.execute("SELECT COUNT(*) FROM users_old").fetchone()[0]
n_new = sum(conn.execute("SELECT COUNT(*) FROM users_%d" % i).fetchone()[0]
            for i in (0, 1))
sample_ok = all(
    conn.execute("SELECT name FROM users_%d WHERE id=?" % shard_of(u),
                 (u,)).fetchone()[0] == n
    for u, n in conn.execute("SELECT id, name FROM users_old LIMIT 20"))
print(f"阶段 3 校验: 行数 {n_old} vs {n_new} 一致={n_old == n_new}, 抽样一致={sample_ok}")
print("剧本: 建表双写 -> 回填 -> 对账 -> 灰度切读 -> 全量 -> 旧表只读 -> 归档下线")
