---
title: [Q2514] 对象命名规范的自动检查: 结构 lint
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2514 · 对象命名规范的自动检查: 结构 lint

> 难度:★★★☆ | 标签:规范, 治理

**问**:命名规范写进了 wiki,为什么线上还是一堆 index1、UserLog?

**答**:因为 review 只能守增量,守不住存量,更守不住"绕过 review 的人"。解法是把命名规范做成结构 lint:规则用代码表达——表名小写下划线、不撞保留字、索引名 idx_/uq_/pk_ 前缀且包含表名——脚本扫 sqlite_master/information_schema 输出违规清单。实测:混入的驼峰表 UserLog、保留字表 order(裸用建表当场报错,带引号建出来的靠 lint 抓)、无语义索引 idx1、后缀风格索引 UserLog_msg_idx 全部落网。lint 挂进 CI 与巡检后,规范从"口头约定"变成"机器契约",新对象过门禁,存量对象限期整改。

```python
# file: code/04_数据库与缓存/q2514_naming_lint.py
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
```

**追问**:
- 规则要不要覆盖字段名?—— 要,规则同源(小写下划线、不撞类型后缀如 _at/_cnt 语义);但字段量大,先卡表和索引这两个影响面最大的。
- 违规了是 fail 还是 warn?—— 新对象 fail(CI 门禁),存量对象 warn 加宽限期,不然第一次接入就全网飘红没人修。

---
