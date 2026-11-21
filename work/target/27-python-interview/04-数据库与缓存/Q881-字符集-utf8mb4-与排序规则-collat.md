---
title: [Q881] 字符集 utf8mb4 与排序规则 collation 的坑
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q881 · 字符集 utf8mb4 与排序规则 collation 的坑

> 难度:★★★☆ | 标签:字符集, 排序规则

**问**:为什么 MySQL 的 utf8 不是真 UTF-8?排序规则 collation 会带来哪些意外?

**答**:MySQL 的 utf8 是历史遗留的三字节实现,存不下 emoji 与部分生僻字,写库直接报错或截断,必须用 utf8mb4(四字节)。排序规则(collation)决定字符比较与排序:utf8mb4_general_ci 与 utf8mb4_0900_ai_ci(8.0 默认)对大小写、重音、某些字符的相等判定不同,跨库迁移或 join 两个不同 collation 的列会报非法混排或无法走索引。工程要点:库表列统一字符集与 collation、连接参数显式指定 charset、索引长度限制(767/3072 字节)与 utf8mb4 的 4 倍膨胀要一起评估。SQLite 是 TEXT 存 UTF-8,排序默认二进制,可用 NOCASE 或自定义 collation。

```python
# file: code/04_数据库与缓存/q881_collation.py
"""演示 emoji 存储与内置 collation 对排序比较的影响"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (name TEXT)")
        conn.executemany("INSERT INTO t VALUES (?)",
                         [("apple",), ("Banana",), ("apple",), ("über",)])
        # 默认 BINARY: 大小写敏感
        print("BINARY 排序:", [r[0] for r in conn.execute("SELECT name FROM t ORDER BY name")])
        # NOCASE collation: 大小写不敏感比较
        print("NOCASE 排序:", [r[0] for r in conn.execute(
            "SELECT name FROM t ORDER BY name COLLATE NOCASE")])
        print("emoji 存储:", conn.execute(
            "SELECT length(?)", ("ok😀",)).fetchone()[0], "个字符(UTF-8 正常)")
        print("MySQL 对照: utf8 存 emoji 报错, 应统一 utf8mb4 + 0900_ai_ci")
```

**追问**:
- collation 不同导致 join 失败怎么处理?——统一两表列的 collation,或在连接条件显式 CONVERT/COLLATE,但会破坏索引,根治是统一建表规范。
- ci 后缀是什么意思?——case insensitive,比较时忽略大小写,所以 'Apple' 与 'apple' 相等,唯一索引下算重复值。

---
