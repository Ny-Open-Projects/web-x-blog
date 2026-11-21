---
title: [Q2744] 大表 join 的驱动序实测: 谁先进扫描循环谁定生死
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2744 · 大表 join 的驱动序实测: 谁先进扫描循环谁定生死

> 难度:★★★★ | 标签:JOIN, 调优

**问**:两张表 join,一张 3 万行一张 100 行,谁当驱动表重要吗?怎么验证?

**答**:重要,而且可以量化。嵌套循环 join 的代价约等于"驱动侧行数 × 对侧每次探测的代价":驱动侧带着高选择性过滤、对侧有索引时,总代价是几千次索引探测;反过来驱动小表、对侧无索引,就是小表每行都把大表全扫一遍,行数相乘直接放大百倍。验证手段是实测加钉序:优化器通常自己选驱动序,但依赖统计信息;用 CROSS JOIN(SQLite)/STRAIGHT_JOIN(MySQL)可以把顺序钉死做对照实验,定位"优化器选错"的场景。规律只有一条:先用过滤条件把驱动侧削到最小,再保证对侧连接列有索引,两者缺一个都要付出相乘的代价。

```python
# file: code/04_数据库与缓存/q2744_join_drive_order.py
"""大表 join 的驱动序实测: CROSS JOIN 钉住顺序, 驱动侧与索引共同决定代价"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE big (id INTEGER PRIMARY KEY, k INTEGER)")
c.execute("CREATE TABLE small (id INTEGER PRIMARY KEY, tag TEXT)")
c.executemany("INSERT INTO big VALUES(?,?)", [(i, i % 1000) for i in range(1, 30001)])
c.executemany("INSERT INTO small VALUES(?,?)", [(i, "t%d" % i) for i in range(1, 101)])

def drive(label, sql):
    t0 = time.perf_counter()
    n = c.execute(sql).fetchone()[0]
    print("%s: %d 行, %.1f ms" % (label, n, (time.perf_counter() - t0) * 1000))

# 1) big 驱动: 3 万行先过滤 k<=100 再逐行探测 small 主键
drive("big 驱动, 过滤后探测 small",
      "SELECT COUNT(*) FROM big CROSS JOIN small WHERE big.k <= 100 AND small.id = big.k")
# 2) small 驱动, big.k 无索引: 100 行各触发一次 3 万行全扫
drive("small 驱动, big.k 无索引",
      "SELECT COUNT(*) FROM small CROSS JOIN big WHERE big.k = small.id")
# 3) small 驱动, big.k 有索引: 100 次索引探测
c.execute("CREATE INDEX idx_big_k ON big(k)")
drive("small 驱动, big.k 有索引",
      "SELECT COUNT(*) FROM small CROSS JOIN big WHERE big.k = small.id")
print("规律: 驱动序由过滤选择性与对侧索引共同决定, 优化器选错时用 CROSS JOIN 钉序保命")
```

**追问**:
- 优化器为什么可能选错?—— 统计信息过期、绑定变量导致估算失真、或代价模型没考虑数据倾斜,实测钉序是最后的兜底。
- 大表对大表怎么办?—— 嵌套循环不再合适,考虑哈希 join 或先把两表各自过滤到小结果集再 join。

---
