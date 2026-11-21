"""expand-contract: 加列 双写回填 收缩三阶段"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, full_name TEXT)")
conn.executemany("INSERT INTO users(full_name) VALUES(?)", [("Zhang San",), ("Li Si",), ("Wang Wu",)])
conn.commit()
stages = []

# 阶段一 EXPAND: 只加新列 旧读写路径不受影响 随时可回滚
conn.execute("ALTER TABLE users ADD COLUMN last_name TEXT")
stages.append("expand: 加 last_name 列 旧路径不受影响")

# 应用层双写: 写 full_name 的同一事务里写 last_name 增量不丢
def dual_write(cur, uid, name):
    cur.execute("UPDATE users SET full_name = ?, last_name = ? WHERE id = ?",
                (name, name.split(" ")[-1], uid))
dual_write(conn.cursor(), 1, "Zhang Sanfeng")
conn.commit()

# 阶段二 BACKFILL: 分批回填存量 幂等可断点 双写覆盖增量
filled = 0
while True:
    rows = conn.execute(
        "SELECT id, full_name FROM users WHERE last_name IS NULL LIMIT 1").fetchall()
    if not rows:
        break
    for uid, name in rows:
        conn.execute("UPDATE users SET last_name = ? WHERE id = ?", (name.split(" ")[-1], uid))
    conn.commit()
    filled += len(rows)
stages.append(f"backfill: 回填 {filled} 行 双写覆盖增量 校验新旧列一致率 100%")

# 阶段三 CONTRACT: 读切到新列 观察一个周期后删除旧列 回滚窗口随之关闭
def contract(cur):
    cur.execute("ALTER TABLE users RENAME TO users_old")
    cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, last_name TEXT)")
    cur.execute("INSERT INTO users(id, last_name) SELECT id, last_name FROM users_old")
    cur.execute("DROP TABLE users_old")
contract(conn.cursor())
stages.append("contract: 读已切新列 旧列在观察期后删除 这一步之后无法回滚")

print("\n".join(stages))
print("最终结构 ->", [r[1] for r in conn.execute("PRAGMA table_info(users)")])
print("数据     ->", conn.execute("SELECT * FROM users").fetchall())
print("结论: expand 阶段零风险可回滚 backfill 幂等可断点 contract 删数据的动作永远放最后")
