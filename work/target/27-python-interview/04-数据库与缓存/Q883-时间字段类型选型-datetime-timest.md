---
title: [Q883] 时间字段类型选型: datetime / timestamp / bigint
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q883 · 时间字段类型选型: datetime / timestamp / bigint

> 难度:★★★☆ | 标签:数据类型, 时区

**问**:MySQL 里存时间用 datetime 还是 timestamp?存 epoch bigint 呢?

**答**:datetime 是"墙上时间",范围 1000-9999 年,8 字节,与时区无关——存什么读什么;timestamp 是 UTC 存储、按会话时区显示,范围到 2038 年(32 位秒数),写入门限校验,自动时区转换是优点也是坑。bigint 存 epoch 毫秒:比较排序快、跨语言无歧义,但可读性差、无内建日期函数(SQLite 常见做法)。选型建议:业务时间(生日、营业时间)用 datetime/DATE,需要多时区展示或自动更新语义用 timestamp 并统一 UTC 会话,日志类高频字段可 bigint。原则:全库统一一种约定,别混用。

```python
# file: code/04_数据库与缓存/q883_time_types.py
"""sqlite 演示 ISO 文本与 epoch 两种存储的时区行为与范围查询"""
import sqlite3
import time as t

if __name__ == "__main__":
    now = int(t.time())
    with sqlite3.connect(":memory:") as conn:
        conn.execute("""CREATE TABLE ev (id INTEGER PRIMARY KEY,
                        iso TEXT, epoch INT)""")
        conn.executemany("INSERT INTO ev (iso, epoch) VALUES (?, ?)",
                         [("2026-11-01 10:00:00", now - 3600),
                          ("2026-11-01 11:00:00", now),
                          ("1970-01-01 00:00:01", 1)])
        print("epoch 范围查(近两小时):",
              conn.execute("SELECT count(*) FROM ev WHERE epoch >= ?",
                           (now - 7200,)).fetchone()[0])
        print("ISO 范围查:",
              conn.execute("SELECT count(*) FROM ev WHERE iso >= '2026-11-01'").fetchone()[0])
        print("epoch 可读化:", conn.execute(
            "SELECT datetime(epoch, 'unixepoch', '+8 hours') FROM ev WHERE epoch = 1").fetchone())
        print("MySQL 对照: timestamp 2038 上限与自动时区转换是选型分水岭")
```

**追问**:
- timestamp 的 ON UPDATE CURRENT_TIMESTAMP 是什么?——行更新时自动刷新该列,常用于 updated_at;但这个"魔法"隐式易被忽略,团队规范里常改用应用层统一维护。
- 为什么时区坑多发生在显示层?——存 UTC 是干净的,坑在读出后用本地默认时区渲染,Python 里坚持 datetime.fromtimestamp(ts, tz=utc) 显式转换。

---
