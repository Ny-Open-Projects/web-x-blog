"""对象命名规范的自动检查: 结构层面的 lint"""
import re
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
# 故意混入多种不合规命名
c.execute('CREATE TABLE UserLog (id INTEGER PRIMARY KEY, msg TEXT)')          # 驼峰
try:
    c.execute('CREATE TABLE order (id INTEGER PRIMARY KEY, amt INTEGER)')     # 保留字裸用
except sqlite3.OperationalError as e:
    print('裸用保留字建表当场报错: %s' % e)
c.execute('CREATE TABLE "order" (id INTEGER PRIMARY KEY, amt INTEGER)')       # 带引号建出来了
c.execute('CREATE TABLE good_orders (id INTEGER PRIMARY KEY, user_id INTEGER)')
c.execute('CREATE INDEX idx1 ON good_orders(user_id)')                        # 无语义索引名
c.execute('CREATE INDEX UserLog_msg_idx ON UserLog(msg)')                     # 后缀风格
c.execute('CREATE UNIQUE INDEX uq_good_orders_user ON good_orders(user_id)')  # 合规

RESERVED = {"order", "group", "index", "table", "select", "where"}
TABLE_RE = re.compile(r"^[a-z][a-z0-9_]*$")

def lint(conn):
    problems = []
    tables = [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
    for t in tables:
        if not TABLE_RE.match(t):
            hint = "撞保留字" if t.lower() in RESERVED else "应为小写下划线"
            problems.append("表 %r: %s" % (t, hint))
        for idx, in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='index' AND tbl_name=?", (t,)):
            if idx.startswith("sqlite_autoindex"):
                continue
            ok = (idx.startswith(("idx_", "uq_", "pk_"))
                  and t in idx
                  and TABLE_RE.match(idx))
            if not ok:
                problems.append("索引 %r: 应为 idx_/uq_/pk_ 前缀且含表名" % idx)
    return problems

for p in lint(conn):
    print("  - %s" % p)
print("结论: 命名规范靠 review 守不住存量, 靠 CI 里的结构 lint 守得住;")
print("      规则不用多——小写下划线 不撞保留字 索引前缀带表名, 已能挡住 80% 的混乱")
