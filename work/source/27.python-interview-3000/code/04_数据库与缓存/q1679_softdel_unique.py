"""软删除与唯一索引冲突: 注销用户占住邮箱的三种解法"""
import sqlite3

conn = sqlite3.connect(":memory:")

# 方案A: 全局 UNIQUE(email) 加软删除列 -> 注销行仍然占坑
conn.executescript("""
CREATE TABLE users_a(id INTEGER PRIMARY KEY, email TEXT UNIQUE, deleted_at TEXT);
INSERT INTO users_a(email, deleted_at) VALUES('bob@x.com', '2026-01-01');
""")
try:
    conn.execute("INSERT INTO users_a(email) VALUES('bob@x.com')")
    conn.commit()
except sqlite3.IntegrityError as e:
    print("方案A 重复注册被拒:", e, "-> 已注销用户挡住新用户")

# 方案B: 唯一索引带上 deleted_at, 但 NULL 互不相等使约束失效
conn.executescript("""
CREATE TABLE users_b(id INTEGER PRIMARY KEY, email TEXT, deleted_at TEXT);
CREATE UNIQUE INDEX ub ON users_b(email, deleted_at);
INSERT INTO users_b(email, deleted_at) VALUES('bob@x.com', '2026-01-01');
""")
conn.execute("INSERT INTO users_b(email) VALUES('bob@x.com')")   # deleted_at 为 NULL
conn.commit()
print("方案B 绕过: deleted_at 为 NULL 的 bob 并存",
      conn.execute("SELECT COUNT(*) FROM users_b WHERE email='bob@x.com'").fetchone()[0], "行")

# 方案C: 部分唯一索引只约束活跃行 (PG 与 SQLite 支持; MySQL 无部分索引)
conn.executescript("""
CREATE TABLE users_c(id INTEGER PRIMARY KEY, email TEXT, deleted_at TEXT);
CREATE UNIQUE INDEX uc ON users_c(email) WHERE deleted_at IS NULL;
INSERT INTO users_c(email) VALUES('bob@x.com');
""")
try:
    conn.execute("INSERT INTO users_c(email) VALUES('bob@x.com')")
    conn.commit()
except sqlite3.IntegrityError:
    print("方案C 拦截活跃邮箱的重复注册 -> OK")
conn.execute("UPDATE users_c SET deleted_at='2026-11-05' "
             "WHERE email='bob@x.com' AND deleted_at IS NULL")
conn.execute("INSERT INTO users_c(email) VALUES('bob@x.com')")
conn.commit()
print("方案C 注销后重注册成功, 活跃 bob 行数:",
      conn.execute("SELECT COUNT(*) FROM users_c "
                   "WHERE email='bob@x.com' AND deleted_at IS NULL").fetchone()[0])
print("MySQL 等价方案: 唯一键用 deleted_flag 整数位, 活跃为 0, 注销改写为行 id, 组合重新唯一")
