"""双写窗口读修复: 迁移期读新库 异步比对旧库 漂移即修复"""
import sqlite3

old = sqlite3.connect(":memory:")
new = sqlite3.connect(":memory:")
for db in (old, new):
    db.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, name TEXT, version INTEGER)")
old.executemany("INSERT INTO user VALUES(?,?,?)",
                [(1, "alice", 3), (2, "bob", 2), (3, "carol", 1)])
# 新库在双写窗口出现两处漂移: 2 是旧值, 3 整行漏写
new.executemany("INSERT INTO user VALUES(?,?,?)", [(1, "alice", 3), (2, "bob-old", 1)])
old.commit()
new.commit()

repair_queue = []

def read_new(user_id):
    """读路径: 读新库, 与旧库比对版本, 旧库更新则读旧值并登记修复"""
    row = new.execute("SELECT id, name, version FROM user WHERE id=?", (user_id,)).fetchone()
    old_row = old.execute(
        "SELECT id, name, version FROM user WHERE id=?", (user_id,)).fetchone()
    if row is None:
        if old_row:
            repair_queue.append(old_row)
        return old_row                      # 新库缺失, 回源旧库兜底
    if old_row and old_row[2] > row[2]:     # 版本更高者权威
        repair_queue.append(old_row)
        return old_row
    return row

def apply_repairs():
    """修复动作是 upsert, 重跑安全"""
    for uid, name, ver in repair_queue:
        new.execute("INSERT OR REPLACE INTO user VALUES(?,?,?)", (uid, name, ver))
    new.commit()
    n = len(repair_queue)
    repair_queue.clear()
    return n

print("读 2 (新库旧值):", read_new(2), "-> 触发读修复")
print("读 3 (新库缺失):", read_new(3), "-> 回源兜底")
print("修复队列:", repair_queue)
print("应用修复条数:", apply_repairs())
print("修复后新库:", new.execute("SELECT * FROM user ORDER BY id").fetchall())
print("要点: 读修复是兜底不是主路径; 权威以版本号或时间戳判定; 双写结束后下线该逻辑")
