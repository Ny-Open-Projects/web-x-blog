"""提交时机与可见性: 未提交的数据对别人不存在"""
import sqlite3
import tempfile
import os

db = os.path.join(tempfile.mkdtemp(), "vis.db")
writer = sqlite3.connect(db)
reader = sqlite3.connect(db)
w = writer.cursor()
r = reader.cursor()
r.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v TEXT)")   # 建表即提交(writer 默认自动开事务)

# 阶段一: writer 写入但未提交
w.execute("INSERT INTO t(v) VALUES('uncommitted')")
seen = r.execute("SELECT COUNT(*) FROM t").fetchone()[0]
print("写入未提交时, reader 看到行数: %d   <- 未提交即不可见" % seen)

# 阶段二: 提交的瞬间, 可见性对后续读生效
w.execute("COMMIT")
seen = r.execute("SELECT COUNT(*) FROM t").fetchone()[0]
print("提交后, reader 看到行数:        %d   <- 不需要重启连接" % seen)

# 阶段三: 回滚让写入像没发生过
w.execute("BEGIN")
w.execute("INSERT INTO t(v) VALUES('to-rollback')")
w.execute("ROLLBACK")
seen = r.execute("SELECT COUNT(*) FROM t").fetchone()[0]
print("回滚后, reader 看到行数:        %d   <- rollback 清空未提交痕迹" % seen)

# 阶段四: writer 自己在事务内能看到自己的写 (读己之写)
w.execute("BEGIN")
w.execute("INSERT INTO t(v) VALUES('own-write')")
own = w.execute("SELECT COUNT(*) FROM t").fetchone()[0]
other = r.execute("SELECT COUNT(*) FROM t").fetchone()[0]
print("事务内: writer 自见 %d 行, reader 仍见 %d 行" % (own, other))
w.execute("COMMIT")
print("结论: 可见性以 COMMIT 为界, 这是所有隔离级别讨论的地基;")
print("      长 INSERT 事务之所以危险, 正是这一大段'对世界不可见'的数据积压在事务里")
writer.close()
reader.close()
