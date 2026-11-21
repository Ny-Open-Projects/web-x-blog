"""复合主键与二级索引: 最左前缀与 rowid 附加规则实测"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE perms(user_id INTEGER, resource TEXT, action TEXT, granted INTEGER,
                   PRIMARY KEY(user_id, resource, action));
CREATE INDEX idx_perm_res ON perms(resource);
""")
conn.executemany("INSERT INTO perms VALUES(?,?,?,?)",
                 [(i % 500, "res%d" % (i // 5), "read", 1) for i in range(10000)])

def plan(sql):
    return " | ".join(r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql))

print("全前缀匹配   ->", plan(
    "SELECT granted FROM perms WHERE user_id = 1 AND resource = 'res5' AND action = 'read'"))
print("最左两列     ->", plan(
    "SELECT granted FROM perms WHERE user_id = 1 AND resource = 'res5'"))
print("只有最左一列 ->", plan("SELECT granted FROM perms WHERE user_id = 1"))
print("跳过最左列   ->", plan("SELECT granted FROM perms WHERE resource = 'res5'"))
print("二级索引加另一主键列 ->", plan(
    "SELECT granted FROM perms WHERE resource = 'res5' AND user_id = 3"))

# rowid 表的二级索引会自动附加 rowid: 直接查 rowid 可走二级索引避免回表
print("索引列与 rowid ->", plan("SELECT resource FROM perms WHERE resource = 'res5' LIMIT 5"))
print("结论: 复合主键是按声明顺序的联合唯一索引, 跳过最左列只能求救于二级索引或全表扫")
