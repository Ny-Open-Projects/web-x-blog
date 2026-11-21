---
title: [Q2207] NULL 排序位置控制: NULLS FIRST/LAST 与 IS NULL 技巧
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2207 · NULL 排序位置控制: NULLS FIRST/LAST 与 IS NULL 技巧

> 难度:★★☆☆ | 标签:SQL, NULL, 排序

**问**:NULL 在 ORDER BY 里排最前还是最后?怎么按业务把它放到指定位置?

**答**:不同数据库默认不同,所以"默认位置"不可依赖。SQLite 把 NULL 视为最小值,ASC 排最前、DESC 排最后;Oracle 相反;PostgreSQL 提供 NULLS FIRST/LAST 子句,SQLite 3.30+ 也支持。可移植的写法是"技巧列"——ORDER BY (col IS NULL), col:第一键把 NULL 归到一组排后面(0 在前 1 在后),第二键在组内正常排序,任何数据库行为一致。还要注意 NULL 参与排序时与其他 NULL 彼此并列,多键排序才稳定;以及分页场景里 NULL 位置必须与索引键序对齐,否则翻页会漂移。

```python
# file: code/04_数据库与缓存/q2207_null_ordering.py
"""NULL 排序位置控制: NULLS FIRST/LAST 与 IS NULL 技巧"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE tasks(id INTEGER PRIMARY KEY, due TEXT)")
c.executemany("INSERT INTO tasks(due) VALUES(?)",
              [("2026-03-01",), (None,), ("2026-01-15",), (None,), ("2026-02-01",)])

def show(label, sql):
    rows = [r[0] if r[0] is not None else "NULL" for r in c.execute(sql)]
    print("%-24s -> %s" % (label, rows))

show("ORDER BY due ASC 默认", "SELECT due FROM tasks ORDER BY due ASC")
show("ORDER BY due DESC 默认", "SELECT due FROM tasks ORDER BY due DESC")
show("ASC NULLS LAST", "SELECT due FROM tasks ORDER BY due ASC NULLS LAST")
show("DESC NULLS FIRST", "SELECT due FROM tasks ORDER BY due DESC NULLS FIRST")
show("技巧 IS NULL 升序", "SELECT due FROM tasks ORDER BY (due IS NULL), due ASC")
show("技巧 IS NULL 降序", "SELECT due FROM tasks ORDER BY (due IS NULL), due DESC")
print("SQLite 视 NULL 为最小值, 老版本没有 NULLS LAST 时用 IS NULL 技巧, 行为跨库一致")
```

**追问**:
- IS NULL 技巧能用上索引吗?—— ORDER BY (col IS NULL), col 是表达式排序,普通索引不匹配,要保证有序需要函数索引或生成列,数据量大时优先 NULLS LAST。
- 为什么分页要关心 NULL 位置?—— keyset 分页的比较条件 WHERE (due, id) > (锚点) 在 NULL 上三值逻辑会失真,含 NULL 列分页要么过滤要么填哨兵值。

---
