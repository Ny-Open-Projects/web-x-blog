"""唯一索引的上线预检: 先查重 分批清理 再建约束"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT)")
seed = ["a@x.com", "b@x.com", "c@x.com", "a@x.com", "b@x.com", "a@x.com", "d@x.com"]
c.executemany("INSERT INTO users(email) VALUES(?)", [(e,) for e in seed])

# 直接建唯一索引: 数据不干净当场翻车
try:
    c.execute("CREATE UNIQUE INDEX uq_users_email ON users(email)")
except sqlite3.IntegrityError as e:
    print("直接建唯一索引: %s" % e)

# 预检: 找出重复组与重复量
dupes = c.execute("""SELECT email, COUNT(*) n, GROUP_CONCAT(id) ids
                     FROM users GROUP BY email HAVING n > 1 ORDER BY n DESC""").fetchall()
print("预检发现 %d 个重复组:" % len(dupes))
for email, n, ids in dupes:
    print("  %-9s x%d, 行号 %s" % (email, n, ids))

# 清理: 每组保留最小 id, 其余进归档 (生产里这一步常常要人工裁决)
c.execute("""DELETE FROM users WHERE id NOT IN
             (SELECT MIN(id) FROM users GROUP BY email)""")
removed = conn.total_changes
c.execute("CREATE UNIQUE INDEX uq_users_email ON users(email)")
n = c.execute("SELECT COUNT(*) FROM users").fetchone()[0]
print("清理重复后建索引成功, 剩 %d 行, 共删除 %d 行" % (n, removed - len(seed)))
try:
    c.execute("INSERT INTO users(email) VALUES('a@x.com')")
except sqlite3.IntegrityError as e:
    print("后续重复写入被唯一索引拦截: %s" % e)
print("结论: 唯一约束的上线顺序是'预检 -> 清理 -> 建索引 -> 回归验证',")
print("      预检报告本身就是业务讨论材料: 谁是主数据 谁是脏数据, 不能由脚本拍板")
