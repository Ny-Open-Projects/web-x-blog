---
title: [Q1933] COLLATE 与大小写: 三套规则各管各的
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1933 · COLLATE 与大小写: 三套规则各管各的

> 难度:★★☆☆ | 标签:SQL, 字符集

**问**:同一个字符串等值查询, 换个数据库或换个列定义结果就不一样了, 这背后是什么机制?

**答**:字符串比较行为由排序规则 COLLATE 决定, 常见的 BINARY 按字节比较、大小写敏感,NOCASE 对 ASCII 折叠大小写。规则可以声明在列定义上, 也可以在单个表达式上用 COLLATE 覆盖, 表达式级优先于列级。最容易踩的坑是 LIKE:SQLite 的 LIKE 默认对 ASCII 不区分大小写, 与等值比较规则不同源, 出现等值查不到而 LIKE 查得到的精神分裂。迁移库时 collation 差异还会影响唯一约束的判定, Apple 与 apple 在 NOCASE 下是重复值。排查大小写问题永远先问一句:这个比较用的是哪个 collation。

```python
# file: code/04_数据库与缓存/q1933_collate_case.py
"""COLLATE 与大小写: 等值 排序与 LIKE 的三套规则"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t(word TEXT COLLATE NOCASE)")
conn.executemany("INSERT INTO t VALUES(?)", [("Apple",), ("banana",), ("APPLE",), ("Banana",)])

# 列声明 NOCASE 后, 索引与等值比较都不区分大小写
n = conn.execute("SELECT COUNT(*) FROM t WHERE word = 'apple'").fetchone()[0]
print("NOCASE 列等值查 apple ->", n, "行")
b = conn.execute("SELECT COUNT(*) FROM t WHERE word = 'apple' COLLATE BINARY").fetchone()[0]
print("同查询表达式级 BINARY ->", b, "行  查询侧可覆盖列侧规则")

# 默认 BINARY 的表: 等值比较区分大小写
conn.execute("CREATE TABLE t2(word TEXT)")
conn.executemany("INSERT INTO t2 VALUES(?)", [("Apple",), ("apple",)])
c = conn.execute("SELECT COUNT(*) FROM t2 WHERE word = 'APPLE'").fetchone()[0]
print("BINARY 列等值查 APPLE ->", c, "行  大小写敏感")

# LIKE 在 SQLite 默认对 ASCII 不区分大小写, 与等值比较规则不同源
l = conn.execute("SELECT COUNT(*) FROM t2 WHERE word LIKE 'apple'").fetchone()[0]
print("BINARY 列 LIKE apple  ->", l, "行  LIKE 另有一套大小写规则")

# ORDER BY 的排序规则决定字典序
print("BINARY 排序:", [r[0] for r in conn.execute("SELECT word FROM t2 ORDER BY word COLLATE BINARY")])
print("NOCASE 排序:", [r[0] for r in conn.execute("SELECT word FROM t2 ORDER BY word COLLATE NOCASE")])
print("结论: 等值与排序行为由列或表达式的 COLLATE 决定, LIKE 的大小写行为独立一套, 混用必踩坑")
```

**追问**:
- 唯一索引加 COLLATE NOCASE 有什么副作用?—— 判重变宽, 长度与字节不同的串会被拒, 索引体积与比较成本也会略增, 要确认业务确实接受大小写折叠。
- 中文场景 COLLATE 重要吗?—— 拼音序与二进制序差异明显, GBK 与 UTF-8 编码序也不同, 排序展示类需求要显式选规则。

---
