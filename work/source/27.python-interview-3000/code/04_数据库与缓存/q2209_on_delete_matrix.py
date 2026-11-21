"""ON DELETE 行为表: 五种级联动作在删除父行后的实际效果"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("PRAGMA foreign_keys=ON")

actions = [
    ("CASCADE",     "ON DELETE CASCADE"),
    ("SET NULL",    "ON DELETE SET NULL"),
    ("SET DEFAULT", "ON DELETE SET DEFAULT"),
    ("RESTRICT",    "ON DELETE RESTRICT"),
    ("NO ACTION",   "ON DELETE NO ACTION"),
]
for i, (name, action) in enumerate(actions, 1):
    tag = "c%d" % i
    c.execute("CREATE TABLE parent_%s(id INTEGER PRIMARY KEY)" % tag)
    c.execute("CREATE TABLE child_%s(pid INTEGER DEFAULT 0 REFERENCES parent_%s(id) %s)"
              % (tag, tag, action))
    if name == "SET DEFAULT":
        c.execute("INSERT INTO parent_%s VALUES(0)" % tag)   # 默认值 0 本身也是合法父行
    c.execute("INSERT INTO parent_%s VALUES(1)" % tag)
    c.execute("INSERT INTO child_%s(pid) VALUES(1)" % tag)
    try:
        c.execute("DELETE FROM parent_%s WHERE id=1" % tag)
        row = c.execute("SELECT pid FROM child_%s" % tag).fetchone()
        outcome = "子行已级联删除" if row is None else "子行仍在, pid = %s" % row[0]
        print("%-12s -> 删除成功, %s" % (name, outcome))
    except sqlite3.IntegrityError as e:
        print("%-12s -> 删除被拒绝: %s" % (name, str(e)[:40]))
conn.commit()
print("前提是 PRAGMA foreign_keys=ON, SQLite 默认关闭时全部动作形同虚设")
