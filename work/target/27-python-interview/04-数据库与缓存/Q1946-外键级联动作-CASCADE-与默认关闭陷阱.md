---
title: [Q1946] 外键级联动作: CASCADE 与默认关闭陷阱
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1946 · 外键级联动作: CASCADE 与默认关闭陷阱

> 难度:★★☆☆ | 标签:外键, 数据完整性

**问**:ON DELETE CASCADE 和 SET NULL 分别什么行为?为什么很多人建了级联却发现根本没生效?

**答**:级联动作把删除传播规则声明在外键上:CASCADE 自动删除引用行, SET NULL 把引用列置空, RESTRICT 则拒绝删除有引用的父行, 让删除决定权回到应用层。最大的陷阱在 SQLite:foreign_keys 默认 OFF, 声明的级联与约束统统不生效, 删父行留下孤儿数据, 本文件对此做了正反对比演示;级联还是层层传递的, 删部门级联删员工, 员工上的 SET NULL 再把标签的引用清空。工程取舍:级联适合强归属关系如配置、日志,核心业务数据的删除建议 RESTRICT 加应用层显式清理, 避免一条误删 DELETE 连坐整条业务链。

```python
# file: code/04_数据库与缓存/q1946_fk_cascade.py
"""外键级联动作: CASCADE SET NULL 与默认关闭陷阱"""
import sqlite3

def build(fk_on):
    c = sqlite3.connect(":memory:")
    c.execute("PRAGMA foreign_keys = %s" % ("ON" if fk_on else "OFF"))
    c.executescript("""
    CREATE TABLE dept(id INTEGER PRIMARY KEY, name TEXT);
    CREATE TABLE emp(id INTEGER PRIMARY KEY, name TEXT, dept_id INTEGER
        REFERENCES dept(id) ON DELETE CASCADE);
    CREATE TABLE tag(id INTEGER PRIMARY KEY, emp_id INTEGER
        REFERENCES emp(id) ON DELETE SET NULL);
    INSERT INTO dept VALUES(1,'core'),(2,'web');
    INSERT INTO emp VALUES(10,'alice',1),(11,'bob',1),(12,'cindy',2);
    INSERT INTO tag VALUES(100,10),(101,11),(102,12);
    """)
    return c

# 陷阱: sqlite 默认 foreign_keys = OFF, 声明的级联根本不会发生
c_off = build(False)
c_off.execute("DELETE FROM dept WHERE id = 1")
print("外键关闭时删部门 -> 员工残留",
      c_off.execute("SELECT COUNT(*) FROM emp WHERE dept_id = 1").fetchone()[0], "人全部成为孤儿")

c_on = build(True)
c_on.execute("DELETE FROM dept WHERE id = 1")
print("外键开启时删部门 -> emp 剩",
      c_on.execute("SELECT COUNT(*) FROM emp").fetchone()[0], "人, tag 的 emp_id:",
      c_on.execute("SELECT emp_id FROM tag ORDER BY id").fetchall(), "级联层层传递")

# RESTRICT: 有员工的部门不允许删, 删除决定权回到应用层
c_on.executescript("""
CREATE TABLE dept2(id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE emp2(id INTEGER PRIMARY KEY, dept_id INTEGER
    REFERENCES dept2(id) ON DELETE RESTRICT);
INSERT INTO dept2 VALUES(1,'fin');
INSERT INTO emp2 VALUES(20, 1);
""")
try:
    c_on.execute("DELETE FROM dept2 WHERE id = 1")
    print("RESTRICT 删除 -> 成功")
except sqlite3.IntegrityError as e:
    print("RESTRICT 删除 -> 被拒:", e)
print("结论: sqlite 默认不启用外键 级联是声明式替代应用层删除循环的手段 但只覆盖删除与更新两种动作")
```

**追问**:
- 级联删除会有性能问题吗?—— 深层级联会放大为大量级联删除并逐行触发, 大批量清理应显式分批删子表再删父表。
- MySQL 需要这个开关吗?—— InnoDB 外键默认生效, 无此陷阱, 但建表语句里的引擎与 SQL_MODE 仍需确认。

---
