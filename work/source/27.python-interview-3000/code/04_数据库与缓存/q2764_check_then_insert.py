"""先查后插的竞态: 检查与插入之间的窗口, 只有唯一约束封得住"""
import os
import sqlite3
import tempfile

dbpath = os.path.join(tempfile.mkdtemp(), "race.db")
a = sqlite3.connect(dbpath, isolation_level=None)
b = sqlite3.connect(dbpath, isolation_level=None)
a.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, email TEXT UNIQUE)")

def check_only(conn, email):
    hit = conn.execute("SELECT 1 FROM user WHERE email=?", (email,)).fetchone()
    return "已存在" if hit else "不存在"

print("第 1 步 b 预查:", check_only(b, "bob@x.com"), "(b 认为可以注册)")
a.execute("INSERT INTO user(email) VALUES(?)", ("bob@x.com",))   # 第 2 步 a 抢先落库
print("第 2 步 a: INSERT 提交成功")
try:
    b.execute("INSERT INTO user(email) VALUES(?)", ("bob@x.com",))  # 第 3 步 b 才真正写入
    print("第 3 步 b: 竟然插入成功 (若无唯一约束, 这就是重复数据)")
except sqlite3.IntegrityError as e:
    print("第 3 步 b: INSERT 撞唯一约束 -> %s" % e)
print("教训: b 的预查没有任何保护力, 唯一约束才是竞态窗口上唯一的闸门")
print("正确姿势: 不预查, 直接 INSERT 并处理 IntegrityError 或 ON CONFLICT")
a.close()
b.close()
