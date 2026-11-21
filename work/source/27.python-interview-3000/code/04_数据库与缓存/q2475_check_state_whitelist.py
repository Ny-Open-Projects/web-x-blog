"""状态列的 CHECK 白名单: 数据库层兜底, 以及新增状态要重建表的迁移代价"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    state TEXT NOT NULL DEFAULT 'pending'
    CHECK (state IN ('pending', 'running', 'done', 'failed'))
)""")
c.execute("INSERT INTO tasks(state) VALUES('pending'), ('running'), ('done')")

# 白名单拦截非法状态, 应用层失守也有防线
try:
    c.execute("INSERT INTO tasks(state) VALUES('runing')")   # 手滑的拼写
except sqlite3.IntegrityError as e:
    print("非法状态被 CHECK 拦截: %s" % e)

# 迁移代价: SQLite 不支持 ALTER 修改 CHECK, 新增状态必须重建表
try:
    c.execute("ALTER TABLE tasks ADD CONSTRAINT dummy CHECK (1=1)")
except sqlite3.OperationalError as e:
    print("ALTER 改 CHECK 不可行: %s" % e)

print("-- 走重建表流程: 建新表 -> 拷数据 -> 改名 --")
c.execute("""CREATE TABLE tasks_new (
    id INTEGER PRIMARY KEY,
    state TEXT NOT NULL DEFAULT 'pending'
    CHECK (state IN ('pending', 'running', 'done', 'failed', 'cancelled'))
)""")
c.execute("INSERT INTO tasks_new SELECT id, state FROM tasks")
c.execute("DROP TABLE tasks")
c.execute("ALTER TABLE tasks_new RENAME TO tasks")
c.execute("INSERT INTO tasks(state) VALUES('cancelled')")
print("重建后状态集合:", [r[0] for r in c.execute("SELECT DISTINCT state FROM tasks ORDER BY state")])

print("结论: CHECK 白名单防脏数据有效, 但枚举演进要付出重建表代价,")
print("      高频新增的状态值放字典表, 低频稳定的状态值才值得 CHECK 硬编码")
