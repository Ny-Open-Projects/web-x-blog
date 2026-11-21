"""批量导入的唯一性兜底三层法: 预查重 + 唯一约束 + 冲突补偿"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT UNIQUE)")
conn.execute("INSERT INTO users(email) VALUES('a@x')")
conn.execute("INSERT INTO users(email) VALUES('b@x')")

incoming = ["c@x", "a@x", "d@x", "b@x", "c@x"]

# 第一层: 预查重, 让可预见的冲突不进库
existing = {r[0] for r in conn.execute("SELECT email FROM users")}
seen, fresh, dupes = set(), [], []
for e in incoming:
    if e in existing or e in seen:
        dupes.append(e)
    else:
        fresh.append(e)
        seen.add(e)

# 第二层: 唯一约束兜底, 并发与竞态下的最后防线
for e in fresh:
    try:
        conn.execute("INSERT INTO users(email) VALUES(?)", (e,))
    except sqlite3.IntegrityError as err:
        dupes.append(e)
        print("约束拦截:", err)

# 第三层: 冲突补偿, 被拒记录进差异清单, 不中断整批
total = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
print(f"导入完成: 库内 {total} 行, 重复拒绝 {dupes}")
print("三层缺一不可: 预查重省成本, 约束保底线, 补偿保吞吐")
