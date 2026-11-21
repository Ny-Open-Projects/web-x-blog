---
title: [Q904] 唯一索引与普通索引: change buffer 的取舍
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q904 · 唯一索引与普通索引: change buffer 的取舍

> 难度:★★★☆ | 标签:索引, InnoDB

**问**:同一个列,建唯一索引还是普通索引?写多读少场景差在哪?

**答**:普通索引写操作可利用 change buffer:目标页不在 buffer pool 时,把"插入索引记录"缓存起来,等页被读入时再合并,减少随机 IO,写密集场景收益明显。唯一索引不行——插入前必须判断唯一性,必须把页读进来校验,change buffer 无用武之地,所以"写多读少、业务能保证唯一"时普通索引更快。但决策权通常不在性能:业务语义需要唯一约束(手机号、订单号)就必须唯一索引,唯一性在应用层校验存在竞态不可靠。两者读性能几乎一致。SQLite/PG 里 change buffer 概念不同, PG 用 HOT 更新,SQLite 无此机制,面试按 MySQL 讲。

```python
# file: code/04_数据库与缓存/q904_unique_vs_normal.py
"""演示唯一约束兜底重复写入, 说明唯一索引的业务价值"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE signup (id INTEGER PRIMARY KEY, phone TEXT)")
        conn.execute("CREATE UNIQUE INDEX idx_phone ON signup (phone)")

        def signup(phone):
            try:
                conn.execute("INSERT INTO signup (phone) VALUES (?)", (phone,))
                conn.commit()
                return "ok"
            except sqlite3.IntegrityError:
                return "duplicate"

        print(signup("13800000001"))
        print(signup("13800000001"))   # 并发双击提交, 数据库层兜底
        print("说明: 应用层判重有竞态, 唯一索引是最终防线, 代价是失去 change buffer 加速")
```

**追问**:
- change buffer 什么时候反而有害?——写完立刻高频读的表(合并频繁)或唯一索引表,缓存合并开销不划算,可用 innodb_change_buffering 控制。
- 唯一索引冲突怎么优雅处理?——捕获冲突转 upsert(DO UPDATE/IGNORE)或返回业务错误,不要先 SELECT 后 INSERT。

---
