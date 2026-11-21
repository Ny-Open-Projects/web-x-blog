"""自增主键的空洞: 哪些操作留洞 哪些不留, 以及为什么不要回补"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE plain (id INTEGER PRIMARY KEY, amt INTEGER)")          # 普通自增
c.execute("CREATE TABLE strict (id INTEGER PRIMARY KEY AUTOINCREMENT, amt INTEGER)")

# 1) 回滚不消耗号段: SQLite 的 sqlite_sequence 在事务内, 回滚一起回滚
c.execute("BEGIN")
c.execute("INSERT INTO strict(amt) VALUES(1)")
c.execute("ROLLBACK")
c.execute("INSERT INTO strict(amt) VALUES(2)")
print("回滚后再插入: id=%d (SQLite 回滚不留洞; MySQL InnoDB 自增非事务性, 回滚即留洞)"
      % c.execute("SELECT id FROM strict").fetchone()[0])

# 2) 删最大行: 普通自增会复用, AUTOINCREMENT 会保留空洞
c.execute("INSERT INTO plain(amt) VALUES(10)")
c.execute("INSERT INTO plain(amt) VALUES(20)")
gone = c.execute("SELECT MAX(id) FROM plain").fetchone()[0]
c.execute("DELETE FROM plain WHERE id=?", (gone,))
c.execute("INSERT INTO plain(amt) VALUES(30)")
print("普通自增删最大行 id=%d 后: 新 id=%d (号被复用)" % (
    gone, c.execute("SELECT MAX(id) FROM plain").fetchone()[0]))
c.execute("INSERT INTO strict(amt) VALUES(10)")
c.execute("INSERT INTO strict(amt) VALUES(20)")
gone = c.execute("SELECT MAX(id) FROM strict").fetchone()[0]
c.execute("DELETE FROM strict WHERE id=?", (gone,))
c.execute("INSERT INTO strict(amt) VALUES(30)")
print("AUTOINCREMENT 删最大行 id=%d 后: 新 id=%d (%d 号成为永久空洞)" % (
    gone, c.execute("SELECT MAX(id) FROM strict").fetchone()[0], gone))

# 3) 手工回补空洞: 技术上可行, 但号段语义立刻变成"可占用"
c.execute("INSERT INTO strict(id, amt) VALUES(?, 999)", (gone,))
c.execute("INSERT INTO strict(amt) VALUES(40)")
print("回补 id=%d 后下一个自增 id=%d" % (
    gone, c.execute("SELECT MAX(id) FROM strict").fetchone()[0]))
try:
    c.execute("INSERT INTO strict(id, amt) VALUES(?, 888)", (gone,))   # 再占同号
except sqlite3.IntegrityError as e:
    print("回补到已占用号段 -> IntegrityError: %s" % e)
print("结论: 空洞是删除 失败 回滚的正常残留, 排序用时间列, 别用 id 判断连续性, 更别手工回补")
