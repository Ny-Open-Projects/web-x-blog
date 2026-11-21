"""列重命名的过渡: 视图垫片护住老代码"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, user_name TEXT NOT NULL)")
c.execute("INSERT INTO users VALUES(1, 'alice'), (2, 'bob')")

# 老代码依赖旧列名 (SELECT 显式列 / INSERT 带列清单的写法)
old_read = "SELECT user_name FROM users WHERE id = 1"
old_write = "INSERT INTO users(user_name) VALUES('carol')"

# 第一步: 重命名
c.execute("ALTER TABLE users RENAME COLUMN user_name TO username")
try:
    c.execute(old_read)
except sqlite3.OperationalError as e:
    print("重命名后老查询立即破裂: %s" % e)

# 第二步: 视图垫片不能占用真表名, 老表名让位给视图前先给真表改名
c.execute("ALTER TABLE users RENAME TO users_new")
c.execute("CREATE VIEW users AS SELECT id, username AS user_name FROM users_new")
print("老读路径经垫片视图恢复:", c.execute(old_read).fetchone()[0])
try:
    c.execute(old_write)          # SQLite 允许对单表视图做有限 DML
    print("老写路径经垫片视图: carol 已写入 ->", c.execute(
        "SELECT username FROM users_new WHERE username='carol'").fetchone()[0])
except sqlite3.OperationalError as e:
    print("垫片视图不接受该写法: %s (写路径需双写或 INSTEAD OF 触发器)" % e)

# 第三步: 全部代码切换到 username 后, 收缩阶段拆掉垫片
c.execute("DROP VIEW users")
c.execute("ALTER TABLE users_new RENAME TO users")
print("收缩后表:", [r[1] for r in c.execute("PRAGMA table_info(users)")])
print("结论: 重命名的事故面是'所有引用旧列名的语句', 过渡三步是")
print("      改名 -> 垫片视图兼容读写 -> 全量切换后拆垫片; 顺序错了就是线上故障")
