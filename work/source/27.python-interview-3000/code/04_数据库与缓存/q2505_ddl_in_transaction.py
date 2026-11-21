"""事务中的 DDL: SQLite 里可回滚, MySQL 里隐式提交"""
import sqlite3
import tempfile
import os

db = os.path.join(tempfile.mkdtemp(), "ddl.db")
conn = sqlite3.connect(db, isolation_level=None)
c = conn.cursor()
c.execute("CREATE TABLE data (id INTEGER PRIMARY KEY, v TEXT)")
c.execute("INSERT INTO data(v) VALUES('a'), ('b')")

# SQLite: DDL 也是事务性语句, 可以和数据一起回滚
c.execute("BEGIN")
c.execute("CREATE TABLE tmp_stage (id INTEGER PRIMARY KEY, v TEXT)")
c.execute("INSERT INTO tmp_stage SELECT id, v FROM data")
c.execute("DROP TABLE data")                      # 迁移脚本里常见的危险动作
tables = [r[0] for r in c.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
print("事务内建了 tmp_stage 又 DROP 了 data, 此刻表清单: %s" % tables)
c.execute("ROLLBACK")
tables = [r[0] for r in c.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
n = c.execute("SELECT COUNT(*) FROM data").fetchone()[0]
print("ROLLBACK 之后表清单: %s, data 行数 %d  <- DDL 与数据一起被回滚" % (tables, n))

# 但要小心: 连接默认的隐式提交行为因驱动而异, 手工混用容易踩出意外提交点
c.execute("BEGIN")
c.execute("INSERT INTO data(v) VALUES('c')")
c.execute("CREATE TABLE log (id INTEGER PRIMARY KEY, msg TEXT)")
c.execute("COMMIT")
tables = [r[0] for r in c.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
print("DDL 与 DML 同事务一起提交: %s, data 行数 %d" % (
    tables, c.execute("SELECT COUNT(*) FROM data").fetchone()[0]))
print("结论: 迁移工具喜欢 SQLite/PG 这类事务性 DDL——失败即整体回滚;")
print("      MySQL 的 DDL 会隐式提交, '改表+改数据'混在一个事务里是经典事故源")
conn.close()
