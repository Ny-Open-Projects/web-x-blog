"""外键延迟约束: 事务内先破坏后修复 DEFERRABLE 的用法"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)   # 手动管理事务
conn.execute("PRAGMA foreign_keys = ON")
conn.executescript("""
CREATE TABLE node(id INTEGER PRIMARY KEY, parent_id INTEGER,
    FOREIGN KEY(parent_id) REFERENCES node(id));
CREATE TABLE edge(id INTEGER PRIMARY KEY, src INTEGER, dst INTEGER,
    FOREIGN KEY(src) REFERENCES node(id) DEFERRABLE INITIALLY DEFERRED,
    FOREIGN KEY(dst) REFERENCES node(id) DEFERRABLE INITIALLY DEFERRED);
INSERT INTO node VALUES(1, NULL);
""")

# 立即约束: 语句执行完立刻检查
try:
    conn.execute("INSERT INTO node VALUES(2, 999)")
    print("立即外键写坏引用 -> 居然成功")
except sqlite3.IntegrityError as e:
    print("立即外键写坏引用 -> 语句即时报错:", e)

# 延迟约束: 事务内允许暂时悬空 COMMIT 时统一复检
conn.execute("BEGIN")
conn.execute("INSERT INTO edge VALUES(2, 999, 1)")
print("延迟外键事务内写坏引用 -> 语句放行")
conn.execute("INSERT INTO node VALUES(999, 1)")
conn.execute("COMMIT")
print("补齐引用后 COMMIT -> 成功 提交时复检通过")

# 反例: 提交时仍悬空 事务被整体拒绝
conn.execute("BEGIN")
conn.execute("INSERT INTO edge VALUES(3, 888, 1)")
try:
    conn.execute("COMMIT")
    print("坏数据居然提交成功")
except sqlite3.IntegrityError as e:
    print("悬空引用 COMMIT -> 被拒:", e)
print("结论: 环引用 键值交换 先子后父这类暂时非法序列 靠 DEFERRABLE INITIALLY DEFERRED 才写得进去")
